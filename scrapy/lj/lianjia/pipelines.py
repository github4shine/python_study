# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pydispatch import dispatcher
from scrapy import signals
import time
import json
import pandas as pd
import numpy as np


class LianjiaPipeline:
    def __init__(self):
        self.columns = None
        self.arrays = []
        #dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def process_item(self, item, spider):
        dic = dict(item)
        if self.columns is None:
            self.columns = list(dic.keys())
        self.arrays.append(list(dic.values()))
        return item

    def spider_closed(self, spider):
        print("export excel")
        writer = pd.ExcelWriter(r"lianjia{0}.xlsx".format(
            time.strftime('%Y-%m-%d-%H-%M-%S')))
        df = pd.DataFrame(np.array(self.arrays), columns=self.columns)
        df.to_excel(writer, sheet_name="data", index=None)  # 导出成excel
        print(self.arrays)
        writer.save()
        writer.close()
