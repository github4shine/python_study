import urllib.request
import json
import urllib.parse
import http.client
import pandas as pd


def DownloadData(page):
    form={"specificationCode":'',"commonname":'',"companyName":'',"catalogname1":'',"catalogname2":'',"catalogname3":'',"_search":'false',"nd":1575642780762,"rows":50,"page":0,"sidx":'',"sord":'asc'}
    form["page"]=page
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("code.nhsa.gov.cn",8000)
    conn.request("POST", "/hc/stdPublishData/getStdPublishDataList.html", urllib.parse.urlencode(form), headers)
    response = conn.getresponse()
    return_data = response.read().decode()
    return return_data


def ExportData():
    df = pd.DataFrame()
    for i in range(606):
        return_data = DownloadData(i+1)
        json_data = json.loads(return_data)
        df = df.append(pd.DataFrame(json_data["rows"]))
    df.to_csv("d:\MaterialData.csv")
    writer = pd.ExcelWriter("d:\MaterialData.xlsx")
    df.to_excel(writer,sheet_name = "data") #导出成excel
    writer.save()

ExportData()
