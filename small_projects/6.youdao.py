import requests
import time, json, random, hashlib


class Youdao(object):
    def __init__(self, word):
        # http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Referer': 'http://fanyi.youdao.com/',
            'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=43028193.30088438; _ga=GA1.2.734522324.1532445198; OUTFOX_SEARCH_USER_ID=-1930169975@10.168.8.76; JSESSIONID=aaaJWk5RawzKMf276UEtw; ___rl__test__cookies=1532779599343'
        }
        self.word = word

        self.post_data = None

    def generate_post_data(self):
        """注意找到js正确的下面内容，与response对应提交表单一致
            i: n,
            from: _,
            to: C,
            smartresult: "dict",
            client: S,
            salt: r,
            sign: o,
            doctype: "json",
            version: "2.1",
            keyfrom: "fanyi.web",
            action: e || "FY_BY_DEFAULT",
            typoResult: !1
        r = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
        o = u.md5(S + n + r + D)
        """
        S = 'fanyideskweb'
        n = self.word
        now = int(time.time() * 1000)
        r = str(now + random.randint(0,9))
        D = 'ebSeFb%=XZ%T[KZ)c(sy!'
        temp_str = S + n + r + D
        md5 = hashlib.md5()
        md5.update(temp_str.encode())
        o = md5.hexdigest()

        self.post_data = {
            'i': self.word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': "dict",
            'client': 'fanyideskweb',
            'salt': r,
            'sign': o,
            'doctype': "json",
            'version': "2.1",
            'keyfrom': "fanyi.web",
            'action': "FY_BY_DEFAULT",
            'typoResult': False
        }




    def get_data(self):
        resp = requests.post(self.url, headers=self.headers, data=self.post_data)
        # print(resp.content)
        return resp.content.decode()

    def parse_data(self, data):
        dict_data = json.loads(data)
        print(dict_data)
        result = dict_data["translateResult"][0][0]['tgt']
        print(result)


    def run(self):

        self.generate_post_data()
        data = self.get_data()
        self.parse_data(data)


if __name__ == '__main__':
    import sys
    word = sys.argv[1]
    youdao = Youdao(word)
    youdao.run()




