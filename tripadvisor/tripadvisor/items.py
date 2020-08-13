# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TripadvisorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    comment_author = scrapy.Field()
    address_author = scrapy.Field()
    comment_title = scrapy.Field()
    comment_body = scrapy.Field()
    comment_date = scrapy.Field()
