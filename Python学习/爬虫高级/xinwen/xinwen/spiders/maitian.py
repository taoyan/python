# -*- coding: utf-8 -*-
import scrapy


class MaitianSpider(scrapy.Spider):
    name = 'maitian'
    allowed_domains = ['maitian.com']
    start_urls = ['http://bj.maitian.cn/esfall/PG1']

    def parse(self, response):
        for zufang_item in response.xpath('//div[@class="list_title"]'):
            yield {
                'title':zufang_item.xpath('./h1/a/text()').extract_first().strip(),
                'price': zufang_item.xpath('./div[@class="the_price"]/ol/strong/span/text()').extract_first().strip(),
                'area': zufang_item.xpath('./p/span/text()').extract_first().replace("m",'').strip(),
                'district': zufang_item.xpath('./p//text()').re(r'昌平|朝阳|东城|大兴|丰台|海淀|石景山').extract_first().strip(),
            }
            next_page_url = response.xpath('//div[@id-"page_"]')
            if next_page_url is not None:
                yield scrapy.Request(response.urljoin(next_page_url))
