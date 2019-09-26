import pymssql
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import uuid
import os
import json
import schedule
import logging
import logging.handlers as handlers
import time


#初始化日志
logging.basicConfig()
mylog = logging.getLogger('mylog')
mylog.setLevel(logging.DEBUG)
formater = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
logfilehandler = handlers.TimedRotatingFileHandler("logs/myapp.log", when='D', interval=1, backupCount=30, encoding='utf-8')
logfilehandler.suffix = "%Y-%m-%d.log"
logfilehandler.setFormatter(formater)
mylog.addHandler(logfilehandler)

def read_script():
    with open("script.sql",'r',encoding='UTF-8-sig') as sql_script:
        sql =sql_script.read()
    return sql

def read_config():
    with open("config.json",'rb') as json_file:
        config = json.load(json_file)
    return config

def update_config(config):
    with open("config.json", 'w') as json_file:
        json.dump(config, json_file, indent=2)
    return None

config = read_config()

def extract_data():
    export_path = config["export_path"] #配置的导出主路径
    if not os.path.exists(export_path):
        os.mkdir(export_path)
    save_path = export_path + "/" + datetime.now().strftime('%Y-%m') #每月的导出路径
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    conn = pymssql.connect(config['server'], config['user'], config['password'], config['database'])
    pre_date = datetime.now() + relativedelta(months=-1)
    pre_date_str = pre_date.strftime('%Y-%m')
    if(config['month_default_length'] == '1'):
        pre_date_str = pre_date_str.replace('-0','-')
    start_date = pre_date_str +"-01"
    end_date = pre_date_str + "-32"
    sql = read_script().format(start_date,end_date)  #读取sql语句脚本
    mylog.info('开始读取数据库')
    df = pd.read_sql(sql,conn) #将数据库脚本读取成dataFrame
    file_suffix = config["export_suffix"]
    export_file_path = save_path +"/"+ str(uuid.uuid1()) + file_suffix
    if(file_suffix == ".csv"):
        df.to_csv(export_file_path, index=None)
    else:
        writer = pd.ExcelWriter(export_file_path)
        df.to_excel(writer,sheet_name = "data") #导出成excel
        writer.save()
    return True

def schedule_job():
    mylog.info("任务正常执行")
    if datetime.now().day == int(config['export_day']): #每月设定日期执行
        mylog.info("开始执行导出")
        try:
            extract_data()
        except Exception as ex:
            mylog.error(ex)
        mylog.info("完成导出数据操作")

if __name__=="__main__":
    mylog.info("服务启动")
    schedule.every().day.at(config['export_time']).do(schedule_job)#设置计划，每天设置的时间点
    while True:
        schedule.run_pending()
        time.sleep(20)
