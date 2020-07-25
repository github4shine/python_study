import scrapy
import time
from ..items import LianjiaItem
from selenium import webdriver

class SzestateSpider(scrapy.Spider):
    name = 'szestate'
    allowed_domains = ['sz.lianjia.com']
    start_urls = ['https://sz.lianjia.com/ershoufang/']
    for page in range(2,3):
        start_urls.append('https://sz.lianjia.com/ershoufang/pg'+str(page))
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        option.add_argument('--headless')
        self.browser = webdriver.Chrome(options  = option)
    def infoParse(self, response):
        #time.sleep(2)
        item = LianjiaItem()
        item['CommunityArea'] = response.xpath("//div[@class ='areaName']/span[2]/a[2]/text()").get()
        item['communityName'] = response.xpath("//div[@class='communityName']/a[1]/text()").get()
        item['buildYear'] = response.xpath("//div[@class='houseInfo']/div[3]/div[2]/text()").get()
        item['houseType'] = response.xpath("//div[@class='introContent']/div[1]/div[2]/ul/li[1]/text()").get()
        item['floor'] = response.xpath("//div[@class='introContent']/div[1]/div[2]/ul/li[2]/text()").get()
        item['area'] = response.xpath("//div[@class='introContent']/div[1]/div[2]/ul/li[3]/text()").get()
        item['houseTypeStruct'] = response.xpath("//div[@class='introContent']/div[1]/div[2]/ul/li[4]/text()").get()
        item['InArea'] = response.xpath("//div[@class='introContent']/div[1]/div[2]/ul/li[5]/text()").get()
        item['buildType'] = response.xpath("//div[@class='introContent']/div[1]/div[2]/ul/li[6]/text()").get()
        item['houseDirection'] = response.xpath("//div[@class='introContent']/div[1]/div[2]/ul/li[7]/text()").get()
        item['buildStruct'] = response.xpath("//div[@class='introContent']/div[1]/div[2]/ul/li[8]/text()").get()
        item['decorateInfo'] = response.xpath("//div[@class='introContent']/div[1]/div[2]/ul/li[9]/text()").get()
        item['liftScale'] = response.xpath("//div[@class='introContent']/div[1]/div[2]/ul/li[10]/text()").get()
        item['hasLift'] = response.xpath("//div[@class='introContent']/div[1]/div[2]/ul/li[11]/text()").get()
        item['showTime'] = response.xpath("//div[@class='introContent']/div[2]/div[2]/ul/li[1]/span[2]/text()").get()
        item['propotyType'] = response.xpath("//div[@class='introContent']/div[2]/div[2]/ul/li[2]/span[2]/text()").get()
        item['lastTransTime'] = response.xpath("//div[@class='introContent']/div[2]/div[2]/ul/li[3]/span[2]/text()").get()
        item['houseUseType'] = response.xpath("//div[@class='introContent']/div[2]/div[2]/ul/li[4]/span[2]/text()").get()
        item['TransYear'] = response.xpath("//div[@class='introContent']/div[2]/div[2]/ul/li[5]/span[2]/text()").get()
        item['propertyOwn'] = response.xpath("//div[@class='introContent']/div[2]/div[2]/ul/li[6]/span[2]/text()").get()
        item['pledge'] = response.xpath("//div[@class='introContent']/div[2]/div[2]/ul/li[7]/span[2]/text()").get()
        item['mark'] = response.xpath("//div[@class='introContent']/div[2]/div[2]/ul/li[8]/span[2]/text()").get()
        yield item

    def parse(self, response):
        urls = response.xpath('//a[contains(@class,"LOGCLICKDATA")]/@href').getall()
        #time.sleep(2)
        for url in urls:
            time.sleep(2)
            yield scrapy.Request(url,callback=self.infoParse)

    def closed(self,spider):
        self.browser.quit()