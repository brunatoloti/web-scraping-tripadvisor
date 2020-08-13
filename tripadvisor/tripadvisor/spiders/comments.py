import scrapy
from ..items import TripadvisorItem


class CommentsSpider(scrapy.Spider):
    name = 'comments'
    allowed_domains = ['tripadvisor.com.br']
    start_urls = ['https://www.tripadvisor.com.br/Attraction_Review-g303441-d553398-Reviews-Parque_Barigui-Curitiba_State_of_Parana.html']

    def parse(self, response):
        item = TripadvisorItem()
        comments_squares = response.xpath("//div[@class='Dq9MAugU T870kzTX LnVzGwUB']")
        for square in comments_squares:
            item["comment_author"] = square.xpath(".//div[@class='_2fxQ4TOx']/span/a/text()").get()
            item["address_author"] = square.xpath(".//span[@class='default _3J15flPT small']/text()").get()
            item["comment_title"] = square.xpath(".//div[@class='glasR4aX']/a//span/text()").get()
            item["comment_body"] = square.xpath(".//div[@class='cPQsENeY']/q/span/text()").get()
            item["comment_date"] = square.xpath(".//span[@class='_34Xs-BQm']/text()").get()
            yield item  #amarro a info que estou extraindo ao arquivo items.py
        
        next_page = response.xpath("//a[@class='ui_button nav next primary ' and text()='Próximas']/@href").get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)