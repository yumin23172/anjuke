#  58写字楼出租
import requests
import json
import re
from lxml import etree
import execjs

class S58_Cz:
    def __init__(self):
        self.n = 5
        self.ritem = {}
        self.headers = {
            'Cookie': '''_ga=GA1.2.1457586794.1534207850; 58tj_uuid=57438cea-0748-4609-b1ae-f7f5c4f5a234; als=0; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1534466717,1535505603; aQQ_brokerguid=37224B3E-0AD2-E82C-F672-1B25EBFA866A; ctid=58; propertys=jobdke-pflv8u_; __xsptplus8=8.25.1537867277.1537868912.3%232%7Cwww.baidu.com%7C%7C%7C%7C%23%236ZNrYc6OTo0le-wIAspGX6Ltqn3ofpx_%23; lps=http%3A%2F%2Flogin.anjuke.com%2Flogin%2Fverify%3Ftoken%3Ddcc85fad46cd0ad8032b8c5ab34e5065%26source%3D1%7Chttps%3A%2F%2Fvip.anjuke.com%2Flogin; sessid=295BD9FF-1D71-A492-BECF-5C4EA8A94C3A; twe=2; init_refer=https%253A%252F%252Fvip.anjuke.com%252Flogin%252F; new_uv=26; anjukereg=sUnZRESZd9%2FZM1Cr; aQQ_ajkguid=5B1877E1-A01D-08E8-6B54-BD510EAB519F; ajk_member_id=51425556; ajk_member_name=1502326082845; ajk_member_key=bd5baad9785eece128a016a4f6f2ba82; ajk_member_time=1569467580; aQQ_ajkauthinfos=vEzVQBPEJNXUMFKtfSRQvPtsQ1SGR1siI5oBD23IHDly337zKXFO8MRhOjkEzGgM%2FBQTgSsqX5vkyCVCRwyvjd1o7w; lui=51425556%3A2; new_session=0; ajk_broker_id=4338661; ajk_broker_ctid=58; ajk_broker_uid=41537906; aQQ_brokerauthinfos=P4SPd3tiaIWC%2FTc9%2FS8B8DJwbcfl6nr723wTLIuyLl3%2BzdOyXbtDKV1zQx27i2sGlCu5EBEIuNydmAHA6fPI%2FbEeecdoVZZM1dmUSi5R5oXb%2BdzhKTiqw%2B9iRukxYJPWYNGOpLzrBWi6gINhksJ0AVQz5eJzFSoD7zs6e4IfGi0NGKrPYqDPrqZVQcIlSWO1uOJUfojdqAML%2BAWcb0ESzA3wN4tDidRR7MaGtg'''
        }
        self.image = []
        self.code = {}
#小区id
    def xiaoqu(self):
        headers = self.headers
        try:
            response = requests.get(
                'http://vip.anjuke.com/ajax/community/unity/?type=esf&q={}'.format(item["xiaoquname"]),
                headers=headers).content.decode()
            res = json.loads(response)
        except Exception:
            return "cookie已过期"
        if res["status"] == "ok":
            xqa = res["data"][0]
            self.xq =xqa['wb_id']
            self.r=xqa['r']
            self.m=xqa['m']
            self.address=xqa['address']
            return self.xq
#图片
    def img(self):
        url = 'https://upd1.ajkimg.com/upload-anjuke'
        files_name = [r'C:\Users\Admin\Pictures\Saved Pictures\text1.jpg',
                      r'C:\Users\Admin\Pictures\Saved Pictures\text.jpg']
        for file in files_name:
            files = {'file': ('timg.jpg', open(file, 'rb'), 'image/jpeg')}
            res = requests.post(url=url, headers=self.headers, files=files).content.decode()
            data = json.dumps(json.loads(res)["image"])
            self.image.append(data)
#跨站请求伪造
    def get_kuazhan(self):
        response = requests.get("https://vip.anjuke.com/house/publish/rent/?from=manage",
                                headers=self.headers).content.decode('utf-8', 'ignore').replace(u'\xa9', u'')
        res = etree.HTML(response)
        code_str0 = res.xpath('//script[contains(text(),"跨站请求伪造")]/text()')[0]
        code_str1 = res.xpath('//script[contains(text(),"input.value = (function ()")]/text()')[0]
        code_list0 = re.findall(r"\"value\":\"(.*?)\"", code_str0)
        code_0_key = code_list0[0]
        code_0_value = code_list0[1]
        code_1_key = re.findall(r"input\.name = \'(.*?)\'", code_str1)[0]
        code_1_function = re.findall(r"input\.value = \(function(.*?return.*?})", code_str1, re.S)[0]
        sum = execjs.compile('function add' + code_1_function)
        code_1_value = sum.call('add')
        self.code['key_0'] = code_0_key
        self.code['key_1'] = code_1_key
        self.code['value_0'] = code_0_value
        self.code['value_1'] = code_1_value

    def put(self):
        headers_1 = self.headers
        data = {
            "sites": item["sites"],                                                    #安居客(1)58(2）赶集（3）三网合一（1，2，3）
                    "type": "1",                                                       #1出租2出售
                    'officeType': '1',                                                 #写字楼类型（）
                    'officeLevel': '1',                                                #写字楼等级
                    'officeProperty': '2',                                             #58写字楼性质
                    "office58": item["xiaoquname"],                                    #写字楼名（xiezilouname）
                    'zone58': self.r,
                    'biz58': self.m,
                    'address58': self.address,
                    'dizhi':item["xiaoquname"],
                    'floorType': '1',                                                    #1单层2独栋
                    'floor': item["louceng"],                                            #楼层（floor）
                    'allFloor': item["zonglouceng"],                                     #总楼层（allFloor）
                    'roomarea': item["mianji"],                                          #面积（roomarea）
                    'rentPrice': item["price"],                                          #价格（rentprice）
                    'areapercent': '98',                                                 #得房率
                    'partition': '1',                                                    #可分割
                    'decoration': item["zhuangxiu"],                                     #装修情况
                    'rentUnit': '1',                                                     #租金单位元/月
                    'rentTime': '3',                                                     #起租期
                    'rentTimeUnit': '1',                                                 #单位元/月
                    'rentFreeMonths': '1',                                               #免租期
                    'monthsOfPay': item["fu"],                                           #付
                    'monthsOfDeposit': item["ya"],                                       #压
                    "title": item["title"],                                              #标题（title）
                    "describe": item["miaoshu"],                                         #描述（describe）
                    "newupdroom[]": self.image,
                    self.code['key_0']: self.code['value_0'],
                    self.code['key_1']: self.code['value_1'],
        }
        print(data)
        print("*" * 80)
        res = requests.post(
            'https://vip.anjuke.com/house/publish/office/?jpChooseType=1&chooseWeb%5B%5D=2', headers=headers_1,
            data=data).content.decode()
        # print(res)
        flag_1 = re.findall("<title>(.*?)</title>", res, re.S)
        if flag_1:
            if flag_1[0] == "发布成功":
                self.ritem["release"] = '1'
                response = requests.get(url="https://vip.anjuke.com/jp58/kcfyxz58",
                                        headers=self.headers).content.decode()
                html_1 = etree.HTML(response)
                shop_url = html_1.xpath("//div[@class='ui-boxer-content']//div/a[3]/@href")[0]
                self.ritem["url"] = shop_url
            elif flag_1[0] == "发布失败":
                self.ritem["release"] = '2'
                html_2 = etree.HTML(res)
                error = html_2.xpath("//div[@class='com-result-info']/text()")[1].replace("\n", '').replace("\t",
                                                                                                            '').replace(
                    " ", '')
                if error:
                    self.ritem["error"] = error
            print(self.ritem)

    def run(self):
        if self.xiaoqu() == "cookie已过期":
            self.ritem["release"] = 2
            self.ritem["error"] = 'cookie已过期'
            print(self.ritem)
            return self.ritem
        self.img()
        self.get_kuazhan()
        self.put()
item={
'sites': '2',                          #安居客(1)58(2）赶集（3）三网合一（1，2，3）
'xiaoquname': '汇佳大厦',
"louceng":'5',"zonglouceng":'55',
"mianji":"123", "price":"4200",
'decoration': '3',
"fu":"3","ya":"1",
"title":"好不好你据格斤复怀旧格方法给寒计较斤斤计较斤斤计较斤斤计较",
"miaoshu":"水水水水水水水时间还哈工水哦数控刀具水水法的实施",
}


if __name__ == '__main__':
    s58 = S58_Cz()
    s58.run()