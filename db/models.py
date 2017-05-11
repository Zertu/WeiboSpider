# -*-coding:utf-8 -*-
from sqlalchemy import Column, INTEGER, String
from db.basic_db import Base


class LoginInfo(Base):
    # 登录账号表 login_info
    __tablename__ = 'login_info'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String(100))
    password = Column(String(200))
    enable = Column(INTEGER, default=1)


class User(Base):
    # 用户表 wbuser
    __tablename__ = 'wbuser'
    # 这里需要设置默认值，否则空的话可能会存储None，可能会引发未catch的异常
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    uid = Column(String, unique=True)
    name = Column(String(200), default='')
    gender = Column(INTEGER, default=0)
    birthday = Column(String(200), default='')
    location = Column(String(100), default='')
    description = Column(String(500), default='')
    register_time = Column(String(200), default='')
    verify_type = Column(INTEGER, default=0)
    verify_info = Column(String(300), default='')
    follows_num = Column(INTEGER, default=0)
    fans_num = Column(INTEGER, default=0)
    wb_num = Column(INTEGER, default=0)
    level = Column(INTEGER, default=0)
    tags = Column(String(500), default='')
    work_info = Column(String(500), default='')
    contact_info = Column(String(300), default='')
    education_info = Column(String(300), default='')
    head_img = Column(String(500), default='')


class SeedIds(Base):
    # 种子用户表 seed_ids
    __tablename__ = 'seed_ids'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    uid = Column(String, unique=True)
    is_crawled = Column(INTEGER, default=0)
    other_crawled = Column(INTEGER, default=0)


class KeyWords(Base):
    # 关键词搜索表 keywords
    __tablename__ = 'keywords'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    keyword = Column(String, unique=True)
    enable = Column(INTEGER, default=1)


class WeiboData(Base):
    # 微博信息表 weibo_data
    __tablename__ = 'weibo_data'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    weibo_id = Column(String, unique=True)
    weibo_cont = Column(String(6000), default='')
    repost_num = Column(INTEGER, default=0)
    comment_num = Column(INTEGER, default=0)
    praise_num = Column(INTEGER, default=0)
    uid = Column(String(20))
    is_origin = Column(INTEGER, default=1)
    device = Column(String(200), default='')
    weibo_url = Column(String(300))
    create_time = Column(String(200))


class KeywordsWbdata(Base):
    # 微博信息关键词联系表 keywords_wbdata
    __tablename__ = 'keywords_wbdata'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    keyword_id = Column(INTEGER)
    wb_id = Column(String(200))



