import base64

import requests
# from util.time_13bit import time_13bit
import json
import os
import time
import re
from lxml import etree
import execjs


class Anjuke_Cs:
    def __init__(self):
        self.n = 5
    def img(self, name, route):
        files = {'file': (name, open(route, 'rb'), 'image/jpeg')}
        res = requests.post('https://upd1.ajkimg.com/upload-anjuke', files=files).content.decode()
        print(res)
        j = json.dumps(json.loads(res)["image"])
        return j
    def yuanwangye(self):
        cookie = "_ga=GA1.2.1457586794.1534207850; 58tj_uuid=57438cea-0748-4609-b1ae-f7f5c4f5a234; als=0; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1534466717,1535505603; ctid=11; aQQ_brokerguid=37224B3E-0AD2-E82C-F672-1B25EBFA866A; lui=74969145%3A2; sessid=2D6F808B-ACFB-495B-829F-EF4302C60189; twe=2; ajk_broker_id=6544973; ajk_broker_ctid=11; ajk_broker_uid=43831982; ajk_member_captcha=c3fa7084f3795b8a3bccab6cdef1b857; _gid=GA1.2.813644008.1536827688; lps=http%3A%2F%2Fshanghai.anjuke.com%2Fcaptcha%7Chttps%3A%2F%2Fshanghai.anjuke.com%2Fprop%2Fview%2FA1411842807; aQQ_ajkguid=5B1877E1-A01D-08E8-6B54-BD510EAB519F; ajk_member_id=74969145; ajk_member_name=U15360539999387; ajk_member_key=a25ba3fc614ae0f1dc969cd0813aad1d; ajk_member_time=1568421780; propertys=jwr48v-pf0w1w_; aQQ_ajkauthinfos=sB6LRUHPd4XWNV%2BpcSBRv%2FtsQ1SGR1siOJoRSW3YCDdy4XLyK09C9cdKYDcEzGgM%2FBQTgSorVZrjwiBCRwyvjd1o7w; __xsptplus8=8.18.1536890181.1536890181.1%232%7Cwww.baidu.com%7C%7C%7C%7C%23%23VvgPlA7CjvN6hvpVZuTdtZOaRo9reFYx%23; new_session=1; init_refer=https%253A%252F%252Fvip.anjuke.com%252Fcombo%252Fbroker%252Fmanage%252Fhz%252F; new_uv=17; aQQ_brokerauthinfos=Pd3bcHEwbNSA%2BzAx8i4D8DN1bsDp43%2F3234VIoK9Ll3wy9ixW7JDIV1xRRq3hGoElHnvF0UJ64qWnAeU4aHOordLfJBqA8FN1dWcRXsI44yB%2BdzhKSDulrA1ROozZZfXZNGKrbzrfAmXgMVTg%2F4KWWQI299xEhAC4zAzSrwaJhczFvvPYKWUxcpsFsN9G2axuLBUeo6PrlMM%2FFOdPUMewwvMNA"
        headers = {
            'Cookie': cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        response = requests.get("http://vip.anjuke.com/house/publish/ershou/?from=manage",
                                headers=headers).content.decode('utf-8', 'ignore').replace(u'\xa9', u'')
        # with open("s_0.html", "w") as f:
        #     f.write(response)
        res = etree.HTML(response)
        x_0 = res.xpath('//script[contains(text(),"拦截CSRF<XSRF>（Cross-site request forgery）跨站请求伪造")]/text()')[0]
        x_1 = res.xpath('//script[contains(text(),"houseNumberValue")]/text()')[0]
        x_0_name_value = re.findall(r"\"value\":\"(.*?)\"", x_0)
        x_0_name = x_0_name_value[0]
        x_0_value = x_0_name_value[1]
        x_1_name = re.findall(r"input\.name = \'(.*?)\'", x_1)[0]
        x_1_function = \
            re.findall("input\.name = [\s\S]*?input.value = \(function (\(\) \{[\s\S]*return [\s\S]*\})\)\(\)", x_1)[0]
        a = execjs.compile('function add' + x_1_function)
        x_1_value = a.call('add')
        return x_0_name, x_0_value, x_1_name, x_1_value
    def put(self, img):
        cookie = "_ga=GA1.2.1457586794.1534207850; 58tj_uuid=57438cea-0748-4609-b1ae-f7f5c4f5a234; als=0; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1534466717,1535505603; ctid=11; aQQ_brokerguid=37224B3E-0AD2-E82C-F672-1B25EBFA866A; lui=74969145%3A2; sessid=2D6F808B-ACFB-495B-829F-EF4302C60189; twe=2; ajk_broker_id=6544973; ajk_broker_ctid=11; ajk_broker_uid=43831982; ajk_member_captcha=c3fa7084f3795b8a3bccab6cdef1b857; _gid=GA1.2.813644008.1536827688; lps=http%3A%2F%2Fshanghai.anjuke.com%2Fcaptcha%7Chttps%3A%2F%2Fshanghai.anjuke.com%2Fprop%2Fview%2FA1411842807; aQQ_ajkguid=5B1877E1-A01D-08E8-6B54-BD510EAB519F; ajk_member_id=74969145; ajk_member_name=U15360539999387; ajk_member_key=a25ba3fc614ae0f1dc969cd0813aad1d; ajk_member_time=1568421780; propertys=jwr48v-pf0w1w_; aQQ_ajkauthinfos=sB6LRUHPd4XWNV%2BpcSBRv%2FtsQ1SGR1siOJoRSW3YCDdy4XLyK09C9cdKYDcEzGgM%2FBQTgSorVZrjwiBCRwyvjd1o7w; __xsptplus8=8.18.1536890181.1536890181.1%232%7Cwww.baidu.com%7C%7C%7C%7C%23%23VvgPlA7CjvN6hvpVZuTdtZOaRo9reFYx%23; new_session=1; init_refer=https%253A%252F%252Fvip.anjuke.com%252Fcombo%252Fbroker%252Fmanage%252Fhz%252F; new_uv=17; aQQ_brokerauthinfos=Pd3bcHEwbNSA%2BzAx8i4D8DN1bsDp43%2F3234VIoK9Ll3wy9ixW7JDIV1xRRq3hGoElHnvF0UJ64qWnAeU4aHOordLfJBqA8FN1dWcRXsI44yB%2BdzhKSDulrA1ROozZZfXZNGKrbzrfAmXgMVTg%2F4KWWQI299xEhAC4zAzSrwaJhczFvvPYKWUxcpsFsN9G2axuLBUeo6PrlMM%2FFOdPUMewwvMNA"

        headers_1 = {
            'Cookie': cookie,
            'Referer': 'http://vip.anjuke.com/house/publish/ershou/?from=manage',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Host': 'vip.anjuke.com'
        }
        roomorder = []
        picture_shineitu = []
        picture_huxingtu = []
        all = []
        if type(img) == type(tuple()):
            if len(img) >= 4:
                for i in img:
                    if img.index(i) == 0:
                        s = self.img(i, i)
                        print(s)
                        picture_huxingtu.append(s)
                        all.append(s)
                    else:
                        s = self.img(i, i)
                        print(s)
                        roomorder.append(json.loads(s)['id'])
                        picture_shineitu.append(s)
                        all.append(s)
                x_tuple = self.yuanwangye()
                print(x_tuple)
                data = {
                    "action": "publish",
                    "broker_id": "5380421",
                    "community_unite": "东方名嘉(东区)",
                    "xiaoquId": "100529733",
                    "shi": "9",
                    "ting": "8",
                    "wei": "7",
                    "params_16": "1",
                    "zhuangXiuQingKuang": "1",
                    "chaoXiang": "1",
                    "params_17": "1",
                    "suoZaiLouCeng": "5",
                    "zongLouCeng": "6",
                    "params_19": "4",
                    "params_82": "1",
                    "params_20": "3",
                    "params_83": "1",
                    "params_21": "2",
                    "mianJi": "110",
                    "params_12": "22",
                    "params_24": "2",
                    "params_81": "1",
                    "params_14": "1901",
                    "params_22": "1",
                    "params_26": "3",
                    "params_25": "1",
                    "params_18": "1",
                    "params_29": "2.5",
                    "jiaGe": "220",
                    "title": "来发布房源了如伽阿尔撒旦法",
                    "content_fangyuanxiangqing": "额我飞机飞啊阿飘上来看到飞过绝望【批发给寄物品而根据物品如果将",
                    "content_yezhuxintai": "额我飞机飞啊阿飘上来看到飞过绝望【批发给寄物品而根据物品如果将",
                    "content_xiaoqupeitao": "额我飞机飞啊阿飘上来看到飞过绝望【批发给寄物品而根据物品如果将",
                    "content_fuwujieshao": "额我飞机飞啊阿飘上来看到飞过绝望【批发给寄物品而根据物品如果将",
                    "params_35[]": "2",
                    "params_36[]": "18556287",
                    # "defaultImgID": defaultImgID,
                    # "modelorder[]": modelorder,
                    "roomorder[]": roomorder,
                    "picture_huxingtu[]": picture_huxingtu,
                    "picture_shineitu[]": picture_shineitu,
                    "file": "",
                    "params_344": "0",
                    # '65870d054d62cc41d2792588c48aa42e': '3213e8bb5084456351485fa1c422398d',#在?chooseWeb%5B%5D=2的value中
                    # 's516d7a02': '18316a378027f5d667b9aacf7ed56b5c|OokbIQ2trMdKSlRox00ksQ==ae==',#js生成
                    x_tuple[0]: x_tuple[1],
                    x_tuple[2]: x_tuple[3]
                }
                print(data)
                print("*" * 80)
                response = requests.post(
                    'http://vip.anjuke.com/house/publish/ershou/',
                    headers=headers_1, data=data)
                return response.content.decode()



img = ("text.jpg", "text1.jpg", "text2.jpg", "text3.jpg", "text4.jpg")
if __name__ == '__main__':
    anjuke = Anjuke_Cs()
    anjuke.img(img[0], img[0])
    anjuke.put(img)
