import requests
import re

url = 'http://www.renren.com/438718956/profile'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

cookies = 'anonymid=jjzsg57lij4a0v; depovince=GUZ; _r01_=1; JSESSIONID=abcjSoAVQRNdKhGzNQmtw; ick_login=677bb014-6e4c-49eb-a750-3c276acd8fb6; first_login_flag=1; ln_uact=13120120193; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20150122/0020/h_main_EV5v_537400006359195a.jpg; jebe_key=653e4f6d-748a-4acd-a026-68a770c87b07%7C1f761d9c8741e5f9db45b82beaa3e5c0%7C1532442103424%7C1%7C1532442109240; _de=7C29999F6ABEF93417E906AB286F0AF5; id=438718956; ver=7.0; jebecookies=7646ac99-a58f-4116-8a45-24bf325bf09f|||||; p=1aab02cd726753d905c446a9619288df6; t=9f6492b5dfa92d3f2b58bcf4a6951e196; societyguester=9f6492b5dfa92d3f2b58bcf4a6951e196; xnsid=3097b007; loginfrom=null; wp=1; wp_fold=1'


temp = {}
for i in cookies.split('; '):
    key = i.split('=')[0]
    value = i.split('=')[-1]
    temp[key] = value

resp = requests.get(url, headers=headers, cookies=temp)
print(re.findall('风雨', resp.content.decode()))
