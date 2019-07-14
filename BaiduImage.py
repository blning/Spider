# !/usr/bin/env python  
# -*- coding:utf-8 -*-

import os
import requests
import re
import urllib.parse as up

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Referer': 'http://image.baidu.com/'}       # 解决百度图片的防盗链

def get_html(url):         # 获取网页内容
    reponse = requests.get(url, headers=headers)
    if reponse.status_code == 200:
        return reponse.text
    else:
        return None


def parse_html(html):               # 解析页面内容
    pattern = 'middleURL":"(.*?)"'
    res = re.findall(pattern, html)
    print(res)
    return res


def create_path():                  # 构建文件存储路径
    path = os.getcwd() + '/image/'
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def download_image(L):    # 下载图片
    path = create_path()
    for image_url in L:
        image_name = path + image_url[-20:]

        rep = requests.get(image_url)
        with open(image_name, 'wb') as f:
            f.write(rep.content)
        print('已下载：', image_name)


def main():
    keyWord = input('请输入您要查找的内容：')

    keyWords = {'queryWord': keyWord}
    Words = {'word': keyWord}

    QueryWord = up.urlencode(keyWords)
    Word = up.urlencode(Words)

    for i in range(2):
        pn = i * 30
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&{}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&{}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=star&pn={}&rn=30'.format(QueryWord, Word, pn)

        html = get_html(url)
        if html:
            L = parse_html(html)
            download_image(L)


if __name__ == '__main__':
    main()