# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
import scrapy
import os
from urllib.parse import urlparse
import time
class FetchpptimgPipeline():
    def process_item(self, item, spider):
        return item

class FetchpptFilePipeline(FilesPipeline):
    pass

class FetchpptimgPipeline1(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        file_path = './files/' + str(time.time()) + ".png"
        print(file_path)
        return file_path

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        print("completed")
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        adapter = ItemAdapter(item)
        adapter['image_paths'] = image_paths
        return item