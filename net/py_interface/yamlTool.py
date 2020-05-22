from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
class yamlUtil:
    def __init__(self):
        self.yml_info = load(open('application.yml','r',encoding='utf-8'),Loader=Loader)
    def getFuncInfoJson(self, request_json): #将请求的json通过配置文件转换对照成xml_dic
        funInfo_dic = {}
        param_dic = {}
        funcNode = self.yml_info[request_json['serviceCode']]
        funName = funcNode.get('funName',None)
        if(funName is not None):
            funInfo_dic['funName'] = funName
        paramNode = funcNode['params']
        for pKey in paramNode.keys():
            pNode = paramNode[pKey]
            pName = pNode.get('pName',None)
            pType = pNode.get('pType',None)
            pDict = pNode.get('dic',None)
            paramValue =request_json['params'][pName]
            if(pDict is not None):
                pDict = self.yml_info.get(pDict,None)
                if(type(pDict) is dict):
                    dic_value = pDict.get(paramValue,None)
                    if(dic_value is None):
                        dic_value = pDict.get('default',None)
                    if(dic_value is not None):
                        paramValue = dic_value
            if(pType is None):
                param_dic[pKey] = paramValue
            if(pType is not None):
                param_dic[pKey] = {pType : paramValue}
        funInfo_dic['params'] = param_dic
        return funInfo_dic

if(__name__ == '__main__'):
    request_json_dic = {"serviceCode": "S001", "params": {"stu": "张三", "pwd": "ysd", "age": "unkown", "course": ["数学", "语文", "英语"]}}
    yamlutil = yamlUtil()
    xml_body_dic = yamlutil.getFuncInfoJson(request_json_dic)
    print(xml_body_dic)