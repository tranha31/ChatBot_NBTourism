import scrapy
from dulichnb.items import DulichnbItem

class LehoiSpider(scrapy.Spider):
    name = 'lehoi'
    allowed_domains = ['dulichninhbinh.com.vn']
    start_urls = ["https://dulichninhbinh.com.vn/index.php/cat/1002"]

    def parse(self, response):
        for item_url in response.css('#frmseach_doc > section > div > div.cat-section-content > div > div.col > div > div > a.item-title-link ::attr(href)').extract():
            content = scrapy.Request(response.urljoin(item_url), callback=self.parse_content, dont_filter=True)
            yield content

    def parse_content(self, response):
        item = DulichnbItem()
        content = ""
        tmp = response.css('#page-content > div > div.page-left-content.col-lg-9.col-md-9.col-sm-12.col-xs-12 > div.item-list-panel.row > div > div:nth-child(1) > h1 ::text').extract_first()
        tmp = tmp.strip()
        content = content + tmp + ". "

        tmp2 = response.css("#page-content > div > div.page-left-content.col-lg-9.col-md-9.col-sm-12.col-xs-12 > div.item-list-panel.row > div > div:nth-child(1) > div.item-content-summery ::text").extract_first()
        tmp2 = tmp2.strip()
        content = content + tmp2 + ". "
        for p in response.css('#page-content > div > div.page-left-content.col-lg-9.col-md-9.col-sm-12.col-xs-12 > div.item-list-panel.row > div > div:nth-child(1) > div.item-content-content > p ::text').extract():
            p = p.strip()
            content = content + p + " "
        
        item['content'] = content
        yield item