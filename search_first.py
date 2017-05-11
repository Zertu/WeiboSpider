# coding:utf-8
from tasks import search

if __name__ == '__main__':
    # 由于celery的定时器有延迟，所以第一次需要手动
    search.excute_search_task()