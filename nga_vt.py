import requests
import time
import re
from lxml import etree
import nga


def get_post():
    global dic
    global t_titles
    global t_urls
    header = {
        'User-Agent': '',
        'Cookie': ''
    }
    url = 'https://bbs.nga.cn/thread.php?fid=-60204499'
    response = requests.get(url, headers=header)
    html = etree.HTML(response.text)
    t_titles = html.xpath('//a[contains(@id,"t_tt")]/text()')
    t_urls = html.xpath('//a[contains(@id,"t_tt")]//@href')
    dic = dict(zip(t_titles, t_urls))


def save_post():
    for t_title in t_titles:
        if '专楼' not in t_title:
            nga.main(int(re.findall(r"\d+", dic[t_title])[0]))
            time.sleep(1)


def start():
    var = 1
    while var == 1:
        get_post()
        # insert_sql()
        save_post()


if __name__ == '__main__':
    start()
