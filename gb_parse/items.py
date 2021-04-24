# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GbParseItem(scrapy.Item):
    pass

class Insta(scrapy.Item):
    _id = scrapy.Field()
    index= scrapy.Field()
    date_parse = scrapy.Field()
    data = scrapy.Field()
    img = scrapy.Field()


class InstaTag(Insta):
    pass


class InstaPost(Insta):
    pass


class InstaFollow(scrapy.Item):
    _id = scrapy.Field()
    date_parse = scrapy.Field()
    user_name = scrapy.Field()
    user_id = scrapy.Field()
    follow_name = scrapy.Field()
    follow_id = scrapy.Field()


class InstaUser(scrapy.Item):
    _id = scrapy.Field()
    index = scrapy.Field()
    date_parse = scrapy.Field()
    data = scrapy.Field()