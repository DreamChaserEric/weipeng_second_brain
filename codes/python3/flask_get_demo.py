# # Get-百度页面
# from flask import Flask
# import requests


# app = Flask(__name__)
# url = 'http://www.baidu.com'

# @app.route('/get')
# def get():
#     r = requests.get(url)
#     r.encoding = 'utf-8'
#     return r.text

# # app.run(debug=True)


# # Get-断言
# __author__ = 'catleer'
# from flask import Flask
# import requests


# app = Flask(__name__)
# url = 'http://www.baidu.com'

# def get_assert():
#     r = requests.get(url)
#     if r.status_code == 200:
#         return True
#     else:
#         return False

# @app.route('/get')
# def get():
#     if get_assert():
#         return '通过'
#     else:
#         return '失败'
        
# # app.run(debug=True) 


# 对Get请求进行基本的异常处理
import re
from flask import Flask
import requests


app = Flask(__name__)

url1 = 'https://www.jianshu.com/u/39cef8a56bf9'
url = 'http://www'


def get_assert(url):
    # 判断url是否合法，需要了解url的构成，用正则匹配进行判断
    # url的构成：协议、域名、端口、虚拟目录、文件名、参数部分等  其中：协议、域名是必须存在的
    # 协议为：http或https  域名为：xxx.xxxx.xxx 端口为：数字
    
    if not re.match(r'^https?://[^\s]\*\.[^\s]\*\.[com|cn|net].\*', url):
        return 'URL不合法,无法执行接口用例'
        
    r = requests.get(url)
    r.encoding = 'utf-8'
    
    if r.status_code == 200:
        return True
    else:
        return r.text


@app.route('/get')
def get():
    if get_assert(url) == True:
        return '通过'
    else:
        return '失败' + ',' + '失败原因：' + get_assert(url)

app.run(host='0.0.0.0')