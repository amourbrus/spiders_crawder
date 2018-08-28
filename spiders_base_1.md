### 爬虫基本 base---requests发送请求获取数据
**1,requests发送请求**
```python
response = requests.get(url, headers=headers)
```
**2,发送带参数的请求 ---- 百度一下为例**
```python
kw = {
    'wd': '天气'
}

# 发送带参数的请求
response = requests.get(url,headers=headers, params=kw)  # 参数**kwargs 会转为关键字参数
```
**3,tieba**
获取源码,不涉及解析
get_data
save_data
完成百度任意贴吧爬虫：任意的页数，保存文件
1,构造url
2,请求头
3,发送请求
4,保存文件
**4,金山翻译**
金山在线翻译,点击翻译选项
post请求，发送data数据（在header里有显示需传的参数）
url/请求头
发送请求，获取响应
**5，代理使用**
response1 = requests.get(url, headers=headers, proxies=proxy)
**6, 直接在请求头发送cookie**
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Cookie': 'anonymid=jjzsg57lij4a0v; depovince=GUZ; _r01_=1; JSESSIONID=abcjSoAVQRNdKhGzNQmtw; ick_login=677bb014-6e4c-49eb-a750-3c276acd8fb6; first_login_flag=1; ln_uact=13120120193; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20150122/0020/h_main_EV5v_537400006359195a.jpg; jebe_key=653e4f6d-748a-4acd-a026-68a770c87b07%7C1f761d9c8741e5f9db45b82beaa3e5c0%7C1532442103424%7C1%7C1532442109240; _de=7C29999F6ABEF93417E906AB286F0AF5; id=438718956; ver=7.0; jebecookies=7646ac99-a58f-4116-8a45-24bf325bf09f|||||; p=1aab02cd726753d905c446a9619288df6; t=9f6492b5dfa92d3f2b58bcf4a6951e196; societyguester=9f6492b5dfa92d3f2b58bcf4a6951e196; xnsid=3097b007; loginfrom=null; wp=1; wp_fold=1'
}

resp = requests.get(url, headers=headers)

```
**7, 单独传cookie**
需要做分割处理
resp = requests.get(url, headers=headers, cookies=temp)

**8,session**
```python
post_data = {
    'email': 'ihflzd',
    'password': 'fahhj23435'
}

session = requests.Session()
session.post(url, headers=headers, data=post_data)

```
**9,cookiejar**
解决第7条使用的分割问题，他可以动态获取cookie,并转换类型
```python
response = requests.get(url, headers=headers)
print(response.cookies)
cookiejar = response.cookies
# 动态的获取cookie并转换数据格式‘
cookie_dict = requests.utils.dict_from_cookiejar(cookiejar)
print(cookie_dict)

cookie_jar = requests.utils.cookiejar_from_dict(cookie_dict)
print(cookie_jar)

```
### 解析数据， small_projects
> 正则，xpath
