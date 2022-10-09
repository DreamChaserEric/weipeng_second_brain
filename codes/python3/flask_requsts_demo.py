import re

from flask import Flask
import requests
from requests import Request, Session

app = Flask(__name__)
url1 = 'https://www.jianshu.com/u/39cef8a56bf9'
url = 'http://httpbin.org/anything'
data = {'a': 'hi'}

def try_request(method, url, data,
                header={}, stream=True, verify=False,
                proxies={}, cert=None, timeout=100):

    if not re.match(r'^https?://[^\s]*\.[com|cn|net|org].*', url):
        return 'URL不合法,无法执行接口用例'
    s = Session()
    method = method.upper()
    req = Request(method, url,
                  data=data,
                  headers=header
                  )
    prepped = req.prepare()

    resp = s.send(prepped,
                  stream=stream,
                  verify=verify,
                  proxies=proxies,
                  cert=cert,
                  timeout=timeout
                  )
    resp.encoding = 'utf-8'
    if resp.status_code == 200:
        return True
    else:
        return resp.text

# method = 'get'
@app.route('/requests/<method>')
def get(method):
    if try_request(method, url, data) == True:
        return '<h1>请求方法, %s!请求结果：通过</h1>' % method
    else:
        return '失败' + ',' + '失败原因：' + try_request(method, url, data)

# app.run(debug=True)

app.run(host='0.0.0.0')