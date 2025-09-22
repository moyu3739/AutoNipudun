以下是客户端请求：
```
POST /wxn/beginCharge HTTP/1.1
Host: www.szlzxn.cn
Connection: keep-alive
Content-Length: 273
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf2541022) XWEB/16467 Flue
content-type: application/x-www-form-urlencoded; charset=UTF-8
Accept: */*
Origin: http://www.szlzxn.cn
Referer: http://www.szlzxn.cn/wx/indexn.html?openId=ouis3uOrvdmYNbSiOtUHD54vutjU&areaid=6&employeeId=1010194&accountmoney=792&temp=temp&dt=1758525926346
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=0618C19CD917E6C83A1490FCB5D4CBF1

msgflag=0027947454%23530027947401803480250922200831099&devaddress=50559153&port=03&money=7&areaId=6&openId=ouis3uOrvdmYNbSiOtUHD54vutjU&beforemoney=792&devtypeid=40&fullStop=0&payType=1&safeOpen=0&safeCharge=9&edtType=0&efee=110&eCharge=55&serviceCharge=55&userId=0&yuan7=0
```


以下是主机返回：
```
HTTP/1.1 200 
x-frame-options: SAMEORIGIN
Access-Control-Allow-Origin: http://www.szlzxn.cn
Access-Control-Allow-Headers: origin, content-type, accept, x-requested-with, sid, mycustom, smuser
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Max-Age: 3600
Access-Control-Allow-Credentials: true
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
Date: Mon, 22 Sep 2025 12:08:37 GMT
Keep-Alive: timeout=20
Connection: keep-alive

{"success":true,"msg":".....................","obj":null}
```