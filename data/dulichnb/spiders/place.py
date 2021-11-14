import scrapy
from dulichnb.items import DulichnbItem

class PlaceSpider(scrapy.Spider):
    name = 'place'
    allowed_domains = ['dulichninhbinh.com.vn']
    start_urls = []

    def start_requests(self):
        for i in range(1, 4):
            page = 'https://dulichninhbinh.com.vn/cat/1001/'+str(i)
            self.start_urls.append(page)
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)


    def parse(self, response):
        for item_url in response.css('#frmseach_doc > section > div > div.cat-section-content > div > div.col > div > div > a.item-title-link ::attr(href)').extract():
            content = scrapy.Request(response.urljoin(item_url), callback=self.parse_content, dont_filter=True)
            yield content

    def parse_content(self, response):
        item = DulichnbItem()
        content = ""
        tmp = response.css('#page-content > div > div.page-left-content.col-lg-9.col-md-9.col-sm-12.col-xs-12 > div.item-list-panel.row > div > div:nth-child(1) > div.item-content-summery ::text').extract_first()
        tmp = tmp.strip()
        content = content + tmp + ". "
        for p in response.css('#page-content > div > div.page-left-content.col-lg-9.col-md-9.col-sm-12.col-xs-12 > div.item-list-panel.row > div > div > div.item-content-content > p ::text').extract():
            p = p.strip()
            content = content + p + " "
        
        item['content'] = content
        yield item
