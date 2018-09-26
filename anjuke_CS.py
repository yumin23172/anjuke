# 安居客二手房
import requests
# from util.time_13bit import time_13bit
import json
import os
import time
import re
from lxml import etree
import execjs

class Anjuke_Cs:
    def __init__(self, cookie):
        self.n = 5
        self.cookie = cookie
        self.ritem = {}

    # def xiaoqu(self, xiaoname):
    #     headers = {
    #         'Cookie': self.cookie,
    #         'Referer': 'http://vip.anjuke.com/house/publish/ershou/?chooseWeb%5B%5D=2',
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    #         'Host': 'vip.anjuke.com'
    #     }
    #     response = requests.get('http://vip.anjuke.com/ajax/community/unity/?type=esf&q={}'.format(xiaoname),
    #                             headers=headers).content.decode()
    #     print(response)
    #     res = json.loads(response)
    #     if res["status"] == "ok":
    #         xq = res["data"]
    #         xq = xq[0]


    def img(self, name, route):
        '''
        https://upd1.ajkimg.com/upload-anjuke
        '''

        headers_1 = {
            'Cookie': self.cookie,
            'Referer': 'http://vip.anjuke.com/house/publish/ershou/?chooseWeb%5B%5D=2',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Host': 'vip.anjuke.com'
        }
        files = {'file': (name, open(route, 'rb'), 'image/jpeg')}
        res = requests.post('https://upd1.ajkimg.com/upload-anjuke', files=files).content.decode()
        print(res)
        j = json.dumps(json.loads(res)["image"])
        # resp = requests.get('https://vip.anjuke.com/ajkbroker/ajax/pic/uploadcallback/', params={"q": res}).content.decode()
        # print(resp)
        return j

    def yuanwangye(self):
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

    def check(self, Price, allArea):
        headers = {
            'cookie': '_ga=GA1.2.1457586794.1534207850; 58tj_uuid=57438cea-0748-4609-b1ae-f7f5c4f5a234; als=0; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1534466717,1535505603; ctid=11; aQQ_brokerguid=37224B3E-0AD2-E82C-F672-1B25EBFA866A; lui=74969145%3A2; __xsptplus8=8.20.1536906031.1536906036.2%232%7Cwww.baidu.com%7C%7C%7C%7C%23%23g1WGNHttTErPLWCaySTJEESAsLBMHcQ1%23; sessid=26E624E9-C65A-E292-BDEA-334D201615D7; anjukereg=sU7URU%2FIc4HVMVKm; aQQ_ajkguid=5B1877E1-A01D-08E8-6B54-BD510EAB519F; lps=http%3A%2F%2Flogin.anjuke.com%2Flogin%2Fverify%3Ftoken%3D11fe5c7db48cc31399baea9224e19820%26source%3D1%7Chttps%3A%2F%2Fvip.anjuke.com%2Flogin; twe=2; ajk_member_id=74969145; ajk_member_name=U15360539999387; ajk_member_key=50305c8ebee0ca96ba15f5effd21c584; ajk_member_time=1569372120; aQQ_ajkauthinfos=v0TaRxPOdtbWNV%2BpcSBRv%2FtsQ1SGR1siOJoRSW3YCDdy4XLyK09C9cdKYDcEzGgM%2FBQTgSsrX5zjySZCRwyvjd1o7w; new_session=1; init_refer=https%253A%252F%252Fvip.anjuke.com%252F; new_uv=20; ajk_broker_id=6544973; ajk_broker_ctid=11; ajk_broker_uid=43831982; aQQ_brokerauthinfos=PNbbfHEwZtKA%2BzAx8i4D8DN1bsDp43%2F3234VIoK9LlrAzt%2B1WLNFI110Qhi0hTgCryi%2BREtXvtmQylGV6abKobRGec05A8QZgbPaTRBg44zrk%2BbiemzrrIlSR%2BgPZqnsYe2Iq43tBg7%2BhLwN2sYIW1VZt%2BN2RkVQ7D8yReoaGCkOGPjJN6HFk55uEcpzIWc',
            'referer': 'https://vip.anjuke.com/house/publish/ershou/?chooseWeb%5B%5D=2',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        response = requests.get(
            'https://vip.anjuke.com/ajax/community/check_price?communityId=100127050&allPrice={}&allArea={}'.format(
                Price, allArea),
            headers=headers).content.decode()
        print(response)
        return response

    def put(self, img):
        headers_1 = {
            'Cookie': self.cookie,
            'Referer': 'http://vip.anjuke.com/house/publish/ershou/?from=manage',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Host': 'vip.anjuke.com'
        }
        roomorder = []
        picture_shineitu = []
        picture_huxingtu = []
        modelorder = []
        all = []
        if type(img) == type(tuple()):
            if len(img) >= 4:
                for i in img:
                    if img.index(i) == 0:
                        s = self.img(i, i)
                        modelorder.append(json.loads(s)['id'])
                        defaultImgID = json.loads(s)['id']
                        picture_huxingtu.append(s)
                        all.append(s)
                    else:
                        s = self.img(i, i)
                        roomorder.append(json.loads(s)['id'])
                        picture_shineitu.append(s)
                        all.append(s)
                x_tuple = self.yuanwangye()
                print(x_tuple)
                data = {
                    "action": "publish",
                    "fixPlanId": "",
                    "broker_id": "5380421",
                    "bianHao": "",
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
                    "params_23": "6",
                    "params_26": "3",
                    "params_25": "1",
                    "params_18": "1",
                    "params_29": "2.5",
                    "jiaGe": "220",
                    "params_28": "66",
                    "title": "摔跤会所哲学摔跤会所",
                    "content_fangyuanxiangqing": "哲学圣地摔跤会所哲学圣地摔跤会所哲学圣地摔跤会所哲学圣地摔跤会所",
                    "content_yezhuxintai": "哲学圣地摔跤会所哲学圣地摔跤会所哲学圣地摔跤会所",
                    "content_xiaoqupeitao": "哲学圣地摔跤会所哲学圣地摔跤会所哲学圣地摔跤会所",
                    "content_fuwujieshao": "哲学圣地摔跤会所哲学圣地摔跤会所哲学圣地摔跤会所哲学圣地摔跤会所哲学圣地摔跤会所哲学圣地摔跤会所哲学圣地摔跤会所哲学圣地摔跤会所哲学圣地摔跤会所",
                    "params_35[]": "2",
                    "params_36[]": "18556287",
                    "defaultImgID": defaultImgID,
                    "modelorder[]": modelorder,
                    "roomorder[]": roomorder,
                    "picture_huxingtu[]": picture_huxingtu,
                    "picture_shineitu[]": picture_shineitu,
                    "file": "",
                    "params_344": "0",
                    x_tuple[0]: x_tuple[1],
                    x_tuple[2]: x_tuple[3]
                }
                print(data)
                print("*" * 80)
                res= requests.post(
                    'http://vip.anjuke.com/house/publish/ershou/?chooseWeb%5B%5D=2',headers=headers_1, data=data).content.decode()
                print(res)
                flag_1 = re.findall("<title>(.*?)</title>", res, re.S)
                if flag_1:
                    if flag_1[0] == "发布成功":
                        self.ritem["release"] = '1'
                        response = requests.get(url="https://vip.anjuke.com/combo/broker/manage/hz/",
                                                headers=headers_1).content.decode()
                        html_1 = etree.HTML(response)
                        shop_url = html_1.xpath("//table[@id='noSpreadHouse']//div/a[1]/@href")[0]
                        self.ritem["url"] = shop_url
                    elif flag_1[0] == "发布失败":
                        self.ritem["release"] = '2'
                        html_2 = etree.HTML(res)
                        error = html_2.xpath("//div[@class='com-result-info']/text()")[1].replace("\n", '').replace(
                            "\t",
                            '').replace(
                            " ", '')
                        if error:
                            self.ritem["error"] = error
                    print(self.ritem)

cookie = "_ga=GA1.2.1457586794.1534207850; 58tj_uuid=57438cea-0748-4609-b1ae-f7f5c4f5a234; als=0; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1534466717,1535505603; ctid=11; aQQ_brokerguid=37224B3E-0AD2-E82C-F672-1B25EBFA866A; lui=74969145%3A2; __xsptplus8=8.20.1536906031.1536906036.2%232%7Cwww.baidu.com%7C%7C%7C%7C%23%23g1WGNHttTErPLWCaySTJEESAsLBMHcQ1%23; sessid=26E624E9-C65A-E292-BDEA-334D201615D7; anjukereg=sU7URU%2FIc4HVMVKm; aQQ_ajkguid=5B1877E1-A01D-08E8-6B54-BD510EAB519F; lps=http%3A%2F%2Flogin.anjuke.com%2Flogin%2Fverify%3Ftoken%3D11fe5c7db48cc31399baea9224e19820%26source%3D1%7Chttps%3A%2F%2Fvip.anjuke.com%2Flogin; twe=2; ajk_member_id=74969145; ajk_member_name=U15360539999387; ajk_member_key=50305c8ebee0ca96ba15f5effd21c584; ajk_member_time=1569372120; aQQ_ajkauthinfos=v0TaRxPOdtbWNV%2BpcSBRv%2FtsQ1SGR1siOJoRSW3YCDdy4XLyK09C9cdKYDcEzGgM%2FBQTgSsrX5zjySZCRwyvjd1o7w; new_session=1; init_refer=https%253A%252F%252Fvip.anjuke.com%252F; new_uv=20; ajk_broker_id=6544973; ajk_broker_ctid=11; ajk_broker_uid=43831982; aQQ_brokerauthinfos=PNbbfHEwZtKA%2BzAx8i4D8DN1bsDp43%2F3234VIoK9LlrAzt%2B1WLNFI110Qhi0hTgCryi%2BREtXvtmQylGV6abKobRGec05A8QZgbPaTRBg44zrk%2BbiemzrrIlSR%2BgPZqnsYe2Iq43tBg7%2BhLwN2sYIW1VZt%2BN2RkVQ7D8yReoaGCkOGPjJN6HFk55uEcpzIWc"

img = ("text.jpg", "text1.jpg", "text2.jpg", "text3.jpg", "text4.jpg")
# s = Anjuke_Cs(cookie).put(img)
# print(s)
# s = Anjuke_Cs(cookie).img(img[0], img[0])
# print(s)
# print(Anjuke_Cs(cookie).yuanwangye())


'''
//script[@id="chooseWebTemp"]

//label[contains(text(),"安居客")]/../label
'''
# Anjuke_Cs(cookie).xiaoqu("东明花苑")
Anjuke_Cs(cookie).put(img)