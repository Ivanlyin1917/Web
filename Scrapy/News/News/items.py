# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
  title = scrapy.Field()
  ptime = scrapy.Field()
  articleText = scrapy.Field()
  UrlImg = scrapy.Field()
  author = scrapy.Field()