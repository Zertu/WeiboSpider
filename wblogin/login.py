# -*-coding:utf-8 -*-
import re
import time
import base64
import binascii
from urllib.parse import quote_plus
import requests
import rsa
from headers import headers
from page_parse.basic import is_403
from logger.log import crawler, other
from db.login_info import freeze_account
from db.redis_db import Cookies


def get_encodename(name):
    # 如果用户名是手机号，那么需要转为字符串才能继续操作
    username_quote = quote_plus(str(name))
    username_base64 = base64.b64encode(username_quote.encode("utf-8"))
    return username_base64.decode("utf-8")


# 预登陆获得 servertime, nonce, pubkey, rsakv
def get_server_data(su, session):
    pre_url = "http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su="
    pre_url = pre_url + su + "&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)&_="
    prelogin_url = pre_url + str(int(time.time() * 1000))
    pre_data_res = session.get(prelogin_url, headers=headers)

    sever_data = eval(pre_data_res.content.decode("utf-8").replace("sinaSSOController.preloginCallBack", ''))

    return sever_data


# 这一段用户加密密码，需要参考加密文件
def get_password(password, servertime, nonce, pubkey):
    rsa_publickey = int(pubkey, 16)
    key = rsa.PublicKey(rsa_publickey, 65537)  # 创建公钥,
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)  # 拼接明文js加密文件中得到
    message = message.encode("utf-8")
    passwd = rsa.encrypt(message, key)  # 加密
    passwd = binascii.b2a_hex(passwd)  # 将加密信息转换为16进制。
    return passwd


# 使用post提交加密后的所有数据,并且获得下一次需要get请求的地址
def get_redirect(data, post_url, session):
    """
    :param data: 需要提交的数据，可以通过抓包来确定部分不变的
    :param post_url: post地址
    :param session:
    :return: 服务器返回的下一次需要请求的url
    """
    logining_page = session.post(post_url, data=data, headers=headers)
    login_loop = logining_page.content.decode("GBK")
    if '正在登录' or 'Signing in' in login_loop:
        pa = r'location\.replace\([\'"](.*?)[\'"]\)'
        return re.findall(pa, login_loop)[0]
    else:
        return ''


# 获取成功登陆返回的信息,包括用户id等重要信息,返回登陆session,存储cookies到redis
def get_session(name, password):
    session = requests.Session()
    su = get_encodename(name)

    sever_data = get_server_data(su, session)
    servertime = sever_data["servertime"]
    nonce = sever_data['nonce']
    rsakv = sever_data["rsakv"]
    pubkey = sever_data["pubkey"]

    sp = get_password(password, servertime, nonce, pubkey)

    # 提交的数据可以根据抓包获得
    data = {
        'encoding': 'UTF-8',
        'entry': 'weibo',
        'from': '',
        'gateway': '1',
        'nonce': nonce,
        'pagerefer': "",
        'prelt': 67,
        'pwencode': 'rsa2',
        "returntype": "META",
        'rsakv': rsakv,
        'savestate': '7',
        'servertime': servertime,
        'service': 'miniblog',
        'sp': sp,
        'sr': '1920*1080',
        'su': su,
        'useticket': '1',
        'vsnf': '1',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack'
    }
    post_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
    url = get_redirect(data, post_url, session)

    if url != '':
        rs_cont = session.get(url, headers=headers)
        login_info = rs_cont.text

        u_pattern = r'"uniqueid":"(.*)",'
        m = re.search(u_pattern, login_info)
        if m:
            if m.group(1):
                # 任意验证一个页面看能否访问，使用这个方法验证比较依赖外部条件，但是没找到更好的方式(有的情况下，
                # 账号存在问题，但是可以访问自己的主页，所以通过自己的主页验证账号是否正常不恰当)
                check_url = 'http://weibo.com/p/1005051764222885/info?mod=pedit_more'
                resp = session.get(check_url, headers=headers)

                if is_403(resp.text):
                    other.error('账号{}已被冻结'.format(name))
                    crawler.warning('账号{}已经被冻结'.format(name))
                    freeze_account(name)
                    return None
                other.info('本次登陆账号为:{}'.format(name))
                Cookies.store_cookies(name, session.cookies.get_dict())
                return session
            else:
                other.error('本次账号{}登陆失败'.format(name))
                return None
        else:
            other.error('本次账号{}登陆失败'.format(name))
            return None
    else:
        other.error('本次账号{}登陆失败'.format(name))
        return None
