import requests
from flask import Flask
from flask import request
from flask.json import jsonify
import yaml
import json
from xml.dom.minidom import parseString
from yamlTool import yamlUtil
from xmlTool import xmlUtil

def Post_webService(url,header,data):
    req = requests.post(url,data=data,headers=header)
    ret = req.content.decode(encoding=req.encoding)
    return ret
#url =  "http://127.0.0.1:7090/WebService1.asmx/HelloWorld"
#data = {"StudentName":"这是一个postData","PassWord":"pwd"}
#header = {"Content-Type": "application/x-www-form-urlencoded"}
#r=Post_webService(url,header,data)
url =  "http://127.0.0.1:7090/WebService1.asmx"

header = {"Content-Type": "text/xml; charset=utf-8","SOAPAction": "http://tempuri.org/HelloWorld"}

app= Flask(__name__)
#app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
app.config['JSON_AS_ASCII'] = False
@app.route('/setValue', methods= ['POST'])
def setValue():
    yamlutil = yamlUtil()
    xml_body_dic = yamlutil.getFuncInfoJson(json.loads(request.json))
    xml_body = '''<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body></soap:Body></soap:Envelope>'''
    xmlutil = xmlUtil(xml_body)
    str_xml = xmlutil.BuildSoapEnvelop(xml_body_dic).encode('utf-8')
    header['SOAPAction'] = "http://tempuri.org/" + xml_body_dic['funName']
    retContent = Post_webService(url,header,str_xml)
    return jsonify({"statu":"success!",'ret':retContent}) , 201
    
if __name__=='__main__':
    app.run(host='0.0.0.0',port = 5000)
