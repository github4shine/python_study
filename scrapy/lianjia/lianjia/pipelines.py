# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import time
import json 

class LianjiaPipeline:
    def __init__(self):
        self.json_str = ""

    def process_item(self, item, spider):
        self.json_str += json.dumps(dict(item), ensure_ascii=False) + "\n"
        return item
    
    def spider_closed(self, spider):
        writer = pd.ExcelWriter(r"d:\lianjia{0}.xlsx".format(time.strftime('%Y-%m-%d-%H-%M-%S')))
        df_new.to_excel(writer,sheet_name = "data",index=None) #导出成excel
        writer.save()

