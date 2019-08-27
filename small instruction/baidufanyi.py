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

    f = open('qu-n.txt', 'r')
    query = str(f.readlines())
    f.close()



    ret = baidu_fanyi(query)
    ret = ''.join(ret)
    #ret = str([c.strip() for c in ret] ) # 采用strip（）方法可以去掉最后的“\n”
    with open('PEDV表位.txt', 'w') as f:

        f.write(ret)
    print(ret)
    # 苹果
