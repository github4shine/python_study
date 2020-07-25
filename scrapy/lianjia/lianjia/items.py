# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    communityName = scrapy.Field()
    CommunityArea = scrapy.Field()
    buildYear = scrapy.Field()
    houseType = scrapy.Field()
    floor =scrapy.Field()
    area = scrapy.Field()
    houseTypeStruct = scrapy.Field()
    InArea = scrapy.Field()
    buildType = scrapy.Field()
    houseDirection = scrapy.Field()
    buildStruct =scrapy.Field()
    decorateInfo = scrapy.Field()
    liftScale = scrapy.Field()
    hasLift = scrapy.Field()
    showTime = scrapy.Field()
    propotyType =scrapy.Field()
    lastTransTime = scrapy.Field()
    houseUseType = scrapy.Field()
    TransYear = scrapy.Field()
    propertyOwn =scrapy.Field()
    pledge = scrapy.Field()
    mark = scrapy.Field()
    pass
