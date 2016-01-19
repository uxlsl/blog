# -*- coding:utf-8 -*-
"""
用来启动在scrapinghub的spider,并把结果拿回来!
"""
import time
import requests
from scrapinghub import Connection


def movie_res_update(api_key, url, project, spider_name):
    """
    把数据从scrapinghub拿回来再传到服务器上
    :param url 推送的地址
    :param api_key shub要使用的api_key
    :param project 项目编号
    :param spider_name 的名字
    """
    conn = Connection(api_key)

    project = conn[project]
    job_id = project.schedule(spider_name)

    while True:
        job = project.job(job_id)
        if job.info['state'] == 'finished':
            break
        time.sleep(60)

    for item in job.items():
        r = requests.post(url, json=item)
        print(r.status_code)
