# -*- coding: utf-8 -*-
import requests
import hashlib
import os

userid = os.getenv('USERID')
password = os.getenv('PASSWORD')
push_key = os.getenv('PUSH')

#登录
headers = {'Connection': 'keep-alive','Cache-Control': 'max-age=0','Upgrade-Insecure-Requests': '1','Origin': 'https://acm.webturing.com','Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'navigate','Sec-Fetch-User': '?1','Sec-Fetch-Dest': 'document','Referer': 'https://acm.webturing.com/loginpage.php','Accept-Language': 'zh-CN,zh;q=0.9',}

data = {'user_id':userid,'password':hashlib.md5(password.encode(encoding='UTF-8')).hexdigest(),'submit':'',}
response1 = requests.post('https://acm.webturing.com/login.php', headers=headers,data=data,allow_redirects=False)
#取cookies
s = response1.headers['Set-Cookie']
PHPSESSID = s[s.find('PHPSESSID')+10:s.find(';')+1]
#签到
cookies = {'PHPSESSID': PHPSESSID,'lastlang': '6',}
headers = {'Connection': 'keep-alive','Content-Length': '0','Accept': '*/*','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36','X-Requested-With': 'XMLHttpRequest','Origin': 'https://acm.webturing.com','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://acm.webturing.com/index.php','Accept-Language': 'zh-CN,zh;q=0.9',}
params = (('action', 'sign'),)
response = requests.post('https://acm.webturing.com/postFunction.php', headers=headers, params=params, cookies=cookies)
if not ('签到成功' in response.text):
    url_server = 'https://sc.ftqq.com/'+push_key+'.send?text=acm签到失败&desp=' + PHPSESSID
    requests.get(url_server)
print(response.text)