from subprocess import *

def ping(ip):
    p = Popen(['ping', ip],
          stdin=PIPE,
          stdout=PIPE,
          shell=True
          )
    p.wait()
    strInfo = p.stdout.read().decode("gbk")
    connected = strInfo.find("丢失 = 0") > 0
    strStat = strInfo[strInfo.find('统计信息'):]
    if(connected):
        return ip + "connected！"
    else:
        return ip + "disconnected！\r\n" + strStat

ips =['10.254.5.152','10.254.5.153','10.254.5.154','10.254.5.155','10.254.5.156','10.254.5.157',
      '10.254.5.158','10.254.5.159','10.254.5.160','10.254.5.161','10.254.5.162','10.254.5.163',
      '10.254.5.164','10.254.5.165','10.254.5.166','10.254.5.167','10.254.5.171','10.254.5.172',
      '10.254.5.177','10.254.5.178','10.254.5.179','10.254.5.180']
mp = map(ping,ips)
for result in mp:
    print(result)
