import requests
import hashlib
import random

appid = '20190225000270928'  # 你的appid
secretKey = 'dliP7qGJN0N5GdJsKeXc'  # 你的密钥

def baidu_fanyi(query):
    salt = random.randint(1, 10)  # 随机数
    code = appid + query + str(salt) + secretKey
    sign = hashlib.md5(code.encode()).hexdigest()  # 签名

    api = "http://api.fanyi.baidu.com/api/trans/vip/translate"

    data = {
        "q": query,
        "from": "auto",
        "to": "auto",
        "appid": appid,
        "salt": salt,
        "sign": sign
    }

    response = requests.post(api, data)

    try:
        result = response.json()
        dst = result.get("trans_result")[0].get("dst")

    except Exception as e:
        dst = query

    finally:
        return dst

if __name__ == '__main__':

    query = input("请输入英文或中文：\n   -->: ")
    ret = baidu_fanyi(query)

    print('   翻译后：'+ ret)
    # 苹果
