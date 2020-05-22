from xml.dom.minidom import parseString
class xmlUtil:
    def __init__(self, xml_body):
        self.xml_body = xml_body
    def BuildSoapEnvelop(self, dic):
        xml_template_doc = parseString(self.xml_body)
        bodys = xml_template_doc.getElementsByTagName("soap:Body")
        if(len(bodys) == 0):
          return ""
        body = bodys[0]
        funNode = xml_template_doc.createElement(dic["funName"])
        funNode.setAttribute("xmlns", "http://tempuri.org/")
        param_dic = dic["params"]
        paramNodes = self.buildParam(param_dic, xml_template_doc)
        for node in paramNodes:
            funNode.appendChild(node)
        body.appendChild(funNode)
        return xml_template_doc.toprettyxml()  # 转成xml字符串

    def buildParam(self, paramDic,  xml_template_doc):
        paramNodes = []
        for key in paramDic.keys():
            param_value = paramDic[key]
            paramNode = xml_template_doc.createElement(key) #每个key生成一个节点
            if(type(param_value) is not dict): #如果value是不是字典，则直接生成text节点
                textNode = xml_template_doc.createTextNode(str(param_value))
                paramNode.appendChild(textNode)
                paramNodes.append(paramNode)
            else: #如果节点是字典
                for subkey in param_value.keys():
                    subparamValue = param_value[subkey]
                    if(type(subparamValue) is str):#如果子字典的value为str,则直接生成text节点
                        subparamNode = xml_template_doc.createElement(subkey) #为子字典key生成一个节点
                        textNode = xml_template_doc.createTextNode(subparamValue)
                        subparamNode.appendChild(textNode)
                        paramNode.appendChild(subparamNode)
                    if(type(subparamValue) is list):#如果子字典的value是一个列表，则生成subkey节点和text
                        for member in subparamValue:
                            subparamNode = xml_template_doc.createElement(subkey)
                            textNode = xml_template_doc.createTextNode(member)
                            subparamNode.appendChild(textNode)
                            paramNode.appendChild(subparamNode)
                paramNodes.append(paramNode)
        return paramNodes


if(__name__ == "__main__"):
    xml_body = '''<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body></soap:Body></soap:Envelope>'''
    dic = {"funName": "helloworld", "params": {"studentName": "张三", "Password": "ysd", "age": "12", "courses": {"string": ["数学", "语文", "英语"]}}}
    xmlutil = xmlUtil(xml_body)
    str_xml = xmlutil.BuildSoapEnvelop(dic)
    print(str_xml)
