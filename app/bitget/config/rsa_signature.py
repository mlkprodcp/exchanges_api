import base64
import json
import time
import base64
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

def get_timestamp():
    return int(time.time() * 1000)


def rsa_sign(message, private_key):
  pri_key = RSA.importKey(private_key)
  encoded_param = SHA256.new(bytes(message, encoding='utf-8'))
  sign_str = PKCS1_v1_5.new(pri_key).sign(encoded_param)
  return base64.b64encode(sign_str).decode()


def pre_hash(timestamp, method, request_path, body):
    return str(timestamp) + str.upper(method) + request_path + body


def parse_params_to_str(params):
    params = [(key, val) for key, val in params.items()]
    params.sort(key=lambda x: x[0])
    from urllib.parse import urlencode
    url = '?' +urlencode(params)
    if url == '?':
        return ''
    return url

''' public key
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8WM0zrSfUr9w0TxcZYbk
FTq3dWes0csI2cz02a4l3ruJq+3ULi0ArN2ZXvIRqynNglGDQHh3xll/9Y3HwxEN
viAtBVpbtLTXAy/iyl4HBNlpMqKLzB5vFD+CZs5PnLm/dPclRT5mTFlHLETzYm8Z
4NntP0X+0Le0HKYPIhkPlf8AShbrphHQ+PZpRTZtrKHN6N5+iUOeJ5cX15faONL9
RqUzl9UtFOV8TMFBbA6h3NRUMLqKRO+YjXC78NaT7+ZVkqf4kIv6mf6CVUOAM72P
+f1FKvZDaZzPrHfxzreia/Yfi9GB23qAwn8d4S/Ez+x3oCA0NFtVS/xMox7rFQB8
0wIDAQAB
-----END PUBLIC KEY-----
'''


if __name__ == '__main__':
    private_key = '''
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDxYzTOtJ9Sv3DR
PFxlhuQVOrd1Z6zRywjZzPTZriXeu4mr7dQuLQCs3Zle8hGrKc2CUYNAeHfGWX/1
jcfDEQ2+IC0FWlu0tNcDL+LKXgcE2WkyoovMHm8UP4Jmzk+cub909yVFPmZMWUcs
RPNibxng2e0/Rf7Qt7Qcpg8iGQ+V/wBKFuumEdD49mlFNm2soc3o3n6JQ54nlxfX
l9o40v1GpTOX1S0U5XxMwUFsDqHc1FQwuopE75iNcLvw1pPv5lWSp/iQi/qZ/oJV
Q4AzvY/5/UUq9kNpnM+sd/HOt6Jr9h+L0YHbeoDCfx3hL8TP7HegIDQ0W1VL/Eyj
HusVAHzTAgMBAAECggEALU418KAFEUZeOd9O5j1ZnMRu/4msbZnieOKXiC2/7Nyd
G9hhDSOkL03ORfxAJbSMXmvHKzgRHvjYY/Gu7yVJw4gNeyY49SNGAdKgieP5BEd8
D6VjgLWrmozLAFmzppJUZXMnmyX5lFXjXmM4nR6GKGYuucP87ha0pvXh/D/g5YFg
L3Q3WUBm+2/3igBBefFK8PZ6adw0ht6EI60YUZOjVai6QzDToav48XhkrmYTUNEH
iqtuDsGVcwpktLQ3HcxZelaAGiWiK/xL3iZ3hfS+ux2ARa6yevMOn/rRt2uV8HeY
s6gnqeXDIZzH9Je3mJFyAIxskJ1jHnP4ywHq+EWhJQKBgQD4vCRN1naYaJvIBBjv
1/cfeLqkxZpfdjgpWEa1KxFAB6KRLjg0HFcbMIZZYCa7qUeLJlcWkrQ/t5K7oQYw
M8ZwYRaKHToXEJT+pZPWj9NQWzz7v8EOHLRDknyuYYJKi/PQJbp6VHoNrExBUIv3
F0yBIwr8Us/ZCCW0w8maOnvwXQKBgQD4cCA9pidYKPsnk6PC/EREZQ8qeiu/+fkg
9nuHYJG84tpNVYm5mRFbuJsOMxRUJ34VoAyhGBVm9DGb5BzbcjX993NZRWHtqM7X
aiqmBUTMYCytysHSezGgrG1spod4keEhzfIUxfB0boRUUiB+6PXSa9dvXY4dACpm
Eb8QGl4O7wKBgD8Y8xivy9vzxXji2TSWk4DvTmGYIwYOZkbOtvkkWLbmeO3dTLKj
cdFa6OnpQ0odsiFxc2wtgP4c4mMogPpfV/qQFnio22CYe0Nx22P1jkR3MKwoQ6AB
1hTCJ1DROY0RnaLyvzBjF6c6SwnSlf7zcRvdON8zXriOoYoOlKjEJ0adAoGBAOXt
cAlec19mXjucqp1VOCFMnqKje0YrpeRZ+q2qNHdqRLv6BIMfJS+MRQT5RUE1Y73D
6KxXS8eDDT7H+eUnaMzpbXobeqyn5Pb9LQeGLMwx3mfiFUwl9CJOMt+xqANwj7nn
jrqnDwnTFumrMKQEGy5p3HMXVOWGN7dLiVbv8ElFAoGAWPkdlEEelXmmKFdkgz4N
s5KPjNM0qq6fR4ADaWQe/QZTQprsvl9/h/cjSnGNuqZcOAlp9vRqkoVugRARbFH5
bO/G2aejwLiY3TiVU9O7QDOCH/a5JioDEv7ntI/6aMPCsvXIW5z1VKV0sePjYR5i
DlCRbuC07Ng/cKJ7oPU1E3A=
-----END PRIVATE KEY-----
'''

# EXCANPLES_REQUESTS
"""
    timestamp = get_timestamp()
    request_path = "/api/v2/mix/order/place-order"
    # POST
    params = {"symbol": "TRXUSDT", "marginCoin": "USDT", "price": 0.0555, "size": 551, "side": "buy", "orderType": "limit", "force": "normal"}
    body = json.dumps(params)
    sign = rsa_sign(pre_hash(timestamp, "POST", request_path, str(body)), private_key)
    print(sign)


    # GET
    body = ""
    request_path = "/api/v2/mix/account/account"
    params = {"symbol": "TRXUSDT", "marginCoin": "USDT"}
    request_path = request_path + parse_params_to_str(params) # Need to be sorted in ascending alphabetical order by key
    sign = rsa_sign(pre_hash(timestamp, "GET", request_path, str(body)), private_key)
    print(sign)
    
"""