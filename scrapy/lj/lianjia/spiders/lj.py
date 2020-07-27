import scrapy
from selenium import webdriver
from ..items import LianjiaItem
import time


class LjSpider(scrapy.Spider):
    name = 'lj'
    allowed_domains = ['sz.lianjia.com']
    start_urls = ['https://sz.lianjia.com/ershoufang']
    for page in range(2, 101):
        start_urls.append("https://sz.lianjia.com/ershoufang/pg" + str(page))

    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        option.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=option)
        self.base_url = "https://sz.lianjia.com"

    def parse(self, response):
        urls = response.xpath(
            '//a[contains(@class,"LOGCLICKDATA")]/@href').getall()
        # time.sleep(2)
        # next_url = self.base_url + response.xpath('//*[text()="下一页"]/@href').get()
        # print(next_url)
        for url in urls:
            time.sleep(2)
            yield scrapy.Request(url, callback=self.infoParse)
        # yield scrapy.Request(next_url, callback=self.parse)

    def infoParse(self, response):
        # time.sleep(2)
        item = LianjiaItem()
        item['CommunityArea'] = response.xpath(
            "//div[@class ='areaName']/span[2]/a[2]/text()").get()
        item['communityName'] = response.xpath(
            "//div[@class='communityName']/a[1]/text()").get()
        item['price'] = response.xpath("//div[@class='price ']/span[@class='total']/text()").get(
        ) + response.xpath("//div[@class='price ']/span[@class='unit']/span/text()").get()
        item['unitprice'] = response.xpath("//div[@class='unitPrice']/span['unitPriceValue']/text()").get(
        ) + response.xpath("//div[@class='unitPrice']/span['unitPriceValue']/i/text()").get()
        item['buildYear'] = response.xpath(
            "//div[@class='houseInfo']/div[3]/div[2]/text()").get()
        item['houseType'] = response.xpath(
            "//div[@class='introContent']/div[1]/div[2]/ul/li[1]/text()").get()
        item['floor'] = response.xpath(
            "//div[@class='introContent']/div[1]/div[2]/ul/li[2]/text()").get()
        item['area'] = response.xpath(
            "//div[@class='introContent']/div[1]/div[2]/ul/li[3]/text()").get()
        item['houseTypeStruct'] = response.xpath(
            "//div[@class='introContent']/div[1]/div[2]/ul/li[4]/text()").get()
        item['InArea'] = response.xpath(
            "//div[@class='introContent']/div[1]/div[2]/ul/li[5]/text()").get()
        item['buildType'] = response.xpath(
            "//div[@class='introContent']/div[1]/div[2]/ul/li[6]/text()").get()
        item['houseDirection'] = response.xpath(
            "//div[@class='introContent']/div[1]/div[2]/ul/li[7]/text()").get()
        item['buildStruct'] = response.xpath(
            "//div[@class='introContent']/div[1]/div[2]/ul/li[8]/text()").get()
        item['decorateInfo'] = response.xpath(
            "//div[@class='introContent']/div[1]/div[2]/ul/li[9]/text()").get()
        item['liftScale'] = response.xpath(
            "//div[@class='introContent']/div[1]/div[2]/ul/li[10]/text()").get()
        item['hasLift'] = response.xpath(
            "//div[@class='introContent']/div[1]/div[2]/ul/li[11]/text()").get()
        item['showTime'] = response.xpath(
            "//div[@class='introContent']/div[2]/div[2]/ul/li[1]/span[2]/text()").get()
        item['propotyType'] = response.xpath(
            "//div[@class='introContent']/div[2]/div[2]/ul/li[2]/span[2]/text()").get()
        item['lastTransTime'] = response.xpath(
            "//div[@class='introContent']/div[2]/div[2]/ul/li[3]/span[2]/text()").get()
        item['houseUseType'] = response.xpath(
            "//div[@class='introContent']/div[2]/div[2]/ul/li[4]/span[2]/text()").get()
        item['TransYear'] = response.xpath(
            "//div[@class='introContent']/div[2]/div[2]/ul/li[5]/span[2]/text()").get()
        item['propertyOwn'] = response.xpath(
            "//div[@class='introContent']/div[2]/div[2]/ul/li[6]/span[2]/text()").get()
        item['pledge'] = response.xpath(
            "//div[@class='introContent']/div[2]/div[2]/ul/li[7]/span[2]/text()").get()
        item['mark'] = response.xpath(
            "//div[@class='introContent']/div[2]/div[2]/ul/li[8]/span[2]/text()").get()
        yield item
    # when spider end ,browser quit

    def closed(self, spider):
        print('spider close,browser quit!')
        self.browser.quit()
