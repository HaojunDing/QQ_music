# -*- coding: utf-8 -*-
import scrapy
import re, json
from random import randint
from qqyinyue_peoject.items import qqyinyuePeojectItem

class QqyinyueSpider(scrapy.Spider):
    name = 'qqyinyue'
    allowed_domains = ['y.qq.com']
    start_urls = ['https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?g_tk=5381&uin=0&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&tpl=3&page=detail&type=top&topid=4&_=1536044673196']
    song_vkey_url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?&needNewCode=0&cid=205361747&songmid={}&filename=C400{}.m4a&guid={}'
    def parse(self, response):
        html = response.text
        req = re.compile(r'songmid":"(.*?)".*?songname":"(.*?)"')
        res = req.findall(html)
        for info in res:
            songmid = info[0]
            songname = info[1]
            vkey_url = self.song_vkey_url.format(songmid, songmid)
            info_html = scrapy.Request(url=vkey_url, callback=self.data_info)
            info_html.meta['songname'] = songname
            yield info_html

    def data_info(self,response):
        item = qqyinyuePeojectItem()
        vname = response.meta['songname']
        html = json.loads(response.text)
        vkey = html['data']['items'][0]['vkey']
        songmid = html['data']['items'][0]['songmid']
        filename = html['data']['items'][0]['filename']
        fromtag = randint(10,100)
        item['vname'] = vname
        item['vkey'] = vkey
        item['songmid'] = songmid
        item['filename'] = filename
        item['fromtag'] = fromtag
        yield item
