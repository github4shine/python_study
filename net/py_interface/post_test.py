import requests
import json
json_data =  {"serviceCode": "S001", "params": {"stu": "张三", "pwd": "ysd", "age": "other", "course": ["数学", "语文", "英语"]}} 
r = requests.post("http://127.0.0.1:5000/setValue",headers ={"content-type":"application/json"},json=json.dumps(json_data))
print(r.status_code)
print(r.content.decode('utf-8'))
