import scrapy
import urllib.parse
import json
import re
from tqqk.items import TqqkItem
from scrapy.downloadermiddlewares.retry import RetryMiddleware

class TqSpider(scrapy.Spider):
    name = 'tq'
    # allowed_domains = ['tianqi.2345.com/china.htm']
    start_urls = ['https://tianqi.2345.com/china.htm']

    def parse(self, response):
        urls=response.xpath('/html/body/div[7]/div[2]/div[2]/ul/li/a/@href').getall()
        for url in urls:
            new_url=response.urljoin(url)
            yield scrapy.Request(url=new_url,callback=self.parse_dq)
    def parse_dq(self,response):
        urls=response.css('.provincial-city-table ::attr(href)').getall()
        b = []
        if urls==[]:
            yield scrapy.Request(response.url,callback=self.parse_dq)
        else:
            # self.logger.debug(urls)
            for url in urls:
                a=str(str(url)[-9:-4])
                b.append(a)
        self.logger.debug(b)
        self.logger.debug(len(b))

                # years=[i+2011 for i in range(11)]
                # months=[i+1 for i in range(11)]
                # for year in years:
                #     for month in months:
                #         data={
                #             'areaInfo[areaId]':a,
                #             'areaInfo[areaType]':2,
                #             'date[year]':year,
                #             'date[month]':month,
                #         }
                #         url='https://tianqi.2345.com/Pc/GetHistory?'+urllib.parse.urlencode(data)
                        # yield scrapy.Request(url,callback=self.parse_tq)
    def parse_tq(self,response):
        data=json.loads(response.text)['data']
        if len(data)<10:
            yield scrapy.Request(response.url,callback=self.parse_tq)
        else:
            data=re.findall('<tr>(.*?)</tr>',data,re.S)
            diqu=re.findall('.*?%5D=(.*?)&areaInfo.*',response.url)[0]
            for i in data:
                day=re.findall('.*?<td>(.*?)</td>.*?"color:.*?>(.*?)</td>.*?"color:.*?>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*',i,re.S)
                if day==[]:
                    pass
                else:
                    oneday={
                        '??????':day[0][0],
                        '?????????':day[0][1],
                        '?????????':day[0][2],
                        '??????':day[0][3],
                        '????????????':day[0][4],
                        '??????':diqu
                    }
                    items=TqqkItem()
                    for field in items.fields:
                        items[field]=oneday[field]
                    yield items







