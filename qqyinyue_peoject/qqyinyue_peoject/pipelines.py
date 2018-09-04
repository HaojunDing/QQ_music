# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import os
class QqyinyuePeojectPipeline(object):
    def process_item(self, item, spider):
        return item


class qqyinyueDownloadPipeline(object):
    def process_item(self, item, spider):
        # print(item['filename'])
        if item['vkey'] != None:
            url = 'http://isure.stream.qqmusic.qq.com/{}?vkey={}&guid=3651300999&fromtag={}'.format(item['filename'],item['vkey'],item['fromtag'])
            fname = 'msdown/'
            if not os.path.exists(fname):
                os.mkdir(fname)
            if not os.path.exists(fname+item['vname']+'.mp3'):
                down = requests.get(url)
                with open(fname+item['vname']+'.mp3', 'wb') as f :
                    f.write(down.content)
                    print('下载:'+item['vname']+'完成!')