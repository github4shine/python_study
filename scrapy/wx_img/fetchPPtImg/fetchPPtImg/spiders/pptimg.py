import scrapy
from scrapy.mail import MailSender
from ..items import FetchpptimgItem

class PptimgSpider(scrapy.Spider):
    name = 'pptimg'
    allowed_domains = ['https://mp.weixin.qq.com/']
    start_urls = ['https://mp.weixin.qq.com/s/FW8BRyrD5CEbcSXsbz4msQ']

    def parse(self, response):
        #imgurls = response.css("img.rich_pages ::attr(data-src)").getall()
        #无法使用src来获取url ,因为url是通过data-src动态加载的
        imgurls = response.xpath('//img[contains(@class,"rich_pages")]/@data-src').getall()
        #print(imgurls)
        item = FetchpptimgItem(image_urls = imgurls[1:5])
        yield item