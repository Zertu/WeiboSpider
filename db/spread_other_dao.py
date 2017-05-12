# -*-coding:utf-8 -*-
from db import basic_db
from logger.log import storage


def save(sos):
    ins_count = 0
    insert_sql = (
        'insert into weibo_spread_other (user_id,user_screenname,user_province,user_city,user_location,'
        'user_description,user_url,user_profileimageurl,user_gender,user_followerscount,user_friendscount,'
        'user_statusescount,user_createdat,user_verifiedtype,user_verifiedreason,status_createdat,'
        'status_mid,status_source,status_repostscount,status_commentscount,upper_user_id,'
        'original_status_id,status_url) '
        " values (:user_id,:user_screenname,:user_province,:user_city,:user_location,"
        ":user_description,:user_url,:user_profileimageurl,:user_gender,:user_followerscount,"
        ":user_friendscount,:user_statusescount,:user_createdat,:user_verifiedtype,:user_verifiedreason,"
        ":status_createdat,:status_mid,:status_source,:status_repostscount,:status_commentscount,"
        ":upper_user_id,:original_status_id,:status_url)"
    )

    with basic_db.db_execute() as conn:

        for item in sos:
            if item.verify_type == '':
                item.verify_type = 0
            try:
                args = {
                    'user_id': item.id,
                    'user_url': item.blog_url,
                    'user_profileimageurl': item.headimg_url,
                    'user_screenname': item.screen_name.encode('gbk', 'ignore').decode('gbk'),
                    'user_province': item.province.encode('gbk', 'ignore').decode('gbk'),
                    'user_city': item.city.encode('gbk', 'ignore').decode('gbk'),
                    'user_location': item.location.encode('gbk', 'ignore').decode('gbk'),
                    'user_description': item.description.encode('gbk', 'ignore').decode('gbk'),
                    'user_gender': item.gender.encode('gbk', 'ignore').decode('gbk'),
                    'user_verifiedreason': item.verify_info.encode('gbk', 'ignore').decode('gbk'),
                    'status_source': item.device.encode('gbk', 'ignore').decode('gbk'),
                    'user_followerscount': int(item.followers_count),
                    'user_friendscount': int(item.friends_count),
                    'user_statusescount': int(item.status_count),
                    'status_repostscount': int(item.reposts_count),
                    'status_commentscount': int(item.comments_count),
                    'user_verifiedtype': item.verify_type,
                    'user_createdat': item.register_time,
                    'status_createdat': item.status_post_time,
                    'status_mid': item.mid,
                    'upper_user_id': item.upper_user_id,
                    'original_status_id': item.original_status_id,
                    'status_url': item.status_url,
                }
                basic_db.db_dml_parms(conn, insert_sql, args)
            except Exception as why:
                storage.error(item.__dict__)
                storage.error(why)
            else:
                ins_count += 1
        storage.info('一共插入了{ins}条数据'.format(ins=ins_count))



