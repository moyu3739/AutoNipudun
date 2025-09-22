import requests
import os

def BeginCharge(dev_addr: str, dev_port: str, cookie_jsessionid: str) -> tuple[bool, str | None]:
    """
    开启 `dev_addr` 设备的 `dev_port` 端口充电，返回是否成功开启
    """
    url = "http://www.szlzxn.cn/wxn/beginCharge"
    
    # 构建请求参数（基于成功会话示例）
    # 注意：部分参数可能需要根据实际情况动态获取或调整
    payload = {
        "devaddress": dev_addr,
        "port": dev_port,
        "money": "9",
        "areaId": "6",
        "openId": "ouis3uOrvdmYNbSiOtUHD54vutjU",
        "beforemoney": "999",
        "devtypeid": "40",
        "fullStop": "0",
        "payType": "1",
        "safeOpen": "0",
        "safeCharge": "9",
        "edtType": "0",
        "efee": "110",
        "eCharge": "55",
        "serviceCharge": "55",
        "userId": "0",
        "yuan7": "0"
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "http://www.szlzxn.cn/wx/indexn.html"
    }
    
    cookies = {
        "JSESSIONID": cookie_jsessionid
    }
    
    try:
        response = requests.post(url, data=payload, headers=headers, cookies=cookies)
        response_json = response.json()
        
        # 检查返回结果中的success字段
        return response_json.get("success", False), response_json.get("msg", None)
    except Exception as e:
        print(f"充电请求发送失败: {e}")
        return False, None
    

if __name__ == "__main__":
    print("AutoNipudun 脚本开始执行")

    # dev_addr = os.environ.get("DEV_ADDR", None)
    # dev_port = os.environ.get("DEV_PORT", None)
    # cookie_jsessionid = os.environ.get("COOKIE_JSESSIONID", None)
    # if dev_addr is None or dev_port is None or cookie_jsessionid is None:
    #     print("缺少环境变量")
    
    # print(f"准备为设备 {dev_addr} 的端口 {dev_port} 开启充电...")
    # print(f"JSESSIONID: {cookie_jsessionid}")

    # dev_addr = ""
    # dev_port = os.environ.get("DEV_PORT", None)
    # cookie_jsessionid = os.environ.get("COOKIE_JSESSIONID", None)

    # success, msg = BeginCharge(dev_addr, dev_port, cookie_jsessionid)
    # if success:
    #     print("充电开启成功")
    # else:
    #     print(f"充电开启失败: {msg}")

