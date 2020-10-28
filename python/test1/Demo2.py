from urllib.request import urlopen
import requests,re,json,jsonpath
import urllib.request
import random
from selenium import webdriver
from lxml import etree
# 代理服务器
# proxyHost = "http-dyn.abuyun.com"
# proxyPort = "9020"
#
# # 代理隧道验证信息
# proxyUser = "HM83Z2M4A24KXGLD"
# proxyPass = "0A1DBF55E49881D7"
class demo2:
    # def crawlerTest():
    #     url = 'https://www.qimai.cn/rank/marketRank/market/6/category/6/'
    #     driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs')
    #     driver.get(url)
    #     content = driver.page_source
    #     print(content)
    # header = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}
    # request = demo2(url, headers=header)
    # response = urlopen(request)
    # html = response.read()
    # obj = json.loads(html)
    # cityList = jsonpath.jsonpath(obj, '$..rankInfo')
    # print(cityList)

        def crawlerTest2():
            iplist = ['106.75.72.116:10086','106.75.72.118:10086','106.75.72.121:10086','106.75.72.112:10086','106.75.72.113:10086','106.75.72.115:10086','106.75.135.58:10086','106.75.135.59:10086','106.75.135.60:10086','106.75.135.61:10086','120.132.53.195:10086','123.59.41.108:10086','123.59.41.105:10086','180.150.177.144:10086','123.59.81.34:10086','123.59.81.36:10086','106.75.12.18:10086','106.75.35.67:10086','106.75.28.132:10086','106.75.28.188:10086','106.75.60.197:10086','106.75.132.215:10086','106.75.133.244:10086','106.75.136.61:10086','106.75.136.36:10086']
            proxy_support = urllib.request.ProxyHandler({'https': random.choice(iplist)})
            opener = urllib.request.build_opener(proxy_support)
            opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')]
            opener.addheaders = [('Referer', 'https://www.qimai.cn/rank/marketRank/market/6/category/6/date/2020-01-20')]
            urllib.request.install_opener(opener)
            url = 'https://api.qimai.cn/rank/marketRank?analysis=dQ51TyxzAEd9YwBJdSBuCiQXGRNRXlsfXVFCUwFDagVaXSETBgQDBwUID1MAClZ0FVA%3D&market=6&category=6&date=2020-01-20'
            response = urllib.request.urlopen(url)
            html = response.read()
            # 把json格式字符串转换成python对象
            jsonobj = json.loads(html)
            # 从根节点开始
            applist = jsonpath.jsonpath(jsonobj, '$.rankInfo[*]')
            # print(applist)
            # print(type(applist))
            print("应用\t排名\t排名变化\t类别\t昨日下载量\t评分数量\t评分结果\t最后更新\t公司名称\n")
            for appdict in applist:
                print(appdict['appInfo']['appName'], end="\t")
                print(appdict['rankInfo']['ranking'], end="\t")
                print(appdict['rankInfo']['change'], end="\t")
                print(appdict['genre'], end="\t")
                print(appdict['downloadNum'], end="\t")
                print(appdict['appInfo']['app_comment_count'], end="\t")
                print(appdict['appInfo']['app_comment_score'], end="\t")
                print(appdict['releaseTime'], end="\t")
                print(appdict['company']['name'], end="\t")
                print("\n")
                # print(appdict)

if  __name__ == '__main__':
    test1 = demo2
    test1.crawlerTest2()