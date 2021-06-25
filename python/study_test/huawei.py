import json
import logging
import time
import math
import jsonpath
import pymongo
import requests

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'huawei'
MONGO_COLLECTION_NAME = 'huawei'
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['huawei']
collection = db['huawei']

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s: %(message)s")

# Cookie ='state=4288752; urlBeforeLogin=https%3A%2F%2Fdeveloper.huawei.com%2Fconsumer%2Fcn%2Fconsole%23%2FopenCard%2FThemeService%2F1057; HuaweiID_CAS_ISCASLOGIN=true; CASLOGINSITE=1; LOGINACCSITE=1; X-HD-SESSION=51c045be-f007-04f7-61f7-74b1b68c6c96; authInfo="{\"expiretime\":\"20210616T090008Z\",\"rtCiphertext\":\"Wv8kF4ooSyxOHF13sLEDgXAqEe2/h3Gywihc4AIwAGpRI6q8Cgmmi7KWayJPm2pLIsrEYMtN5bXUJV8DGrEEu8Re/cFZQtxLK2LB6MyFIOuesbeoADhKMvrHR9NZCFcWA8XLTyAtKRIkRZs5zBPxJeJS3wF+waCyueRTFM4HnSn+40pg8GRGdRHwbykZnSXk\",\"createtime\":\"20210616T080008Z\",\"signature\":\"27fb992038b47c36e20cf4f12d26c381276273c368a971d06a36b35d3d70d611\",\"accesstoken\":\"CgB6e3x9S/aklG+dBaxRlVuidLP+tkKU/PhaZJS6kz9upRIaVXpCjanRlAP9B6HgfrrJinX9JRAGr4TuATz+q0r1LRxcWIP5G3xPTiwr1NABSPllOh2C\",\"siteID\":\"1\"}"; csrfToken=B8379046CF84B9C8CDFCC9D4FAA1F150963FECAE5B0309D5C7; x-siteId=1; x-hd-grey=alnc-0; x-teamId=; x-country=CN; x-userType=2; developer_userinfo=%7B%22siteid%22%3A%221%22%2C%22expiretime%22%3A%2220210616T090008Z%22%2C%22csrftoken%22%3A%22B8379046CF84B9C8CDFCC9D4FAA1F150963FECAE5B0309D5C7%22%7D'
Cookie ='HuaweiID_CAS_ISCASLOGIN=true; CASLOGINSITE=1; LOGINACCSITE=1; X-HD-SESSION=4b950343-cbe8-b7c9-ce36-980c436281c6; authInfo="{\"expiretime\":\"20210618T103201Z\",\"rtCiphertext\":\"+oRtemd1QPxuwCNvED1tY/UeUumkuIA29XEGH3GnputaAExHpWzrdjhdfYfCmNBlCUUf3BIg4pn3mgcj2YEUbVjgdgfTKjT/spUlmtUueo5KrPbEhlKCsP2yVkrFQlkgwh8Zw7jEGtfIro4mWSGCkpkO7+ku4jMHDyzF0EmAVwKfv7awD9OycnjFz5q+aasz\",\"createtime\":\"20210618T093201Z\",\"signature\":\"610e264d64a37c0c10d02eb4062d00111d370a2bc4a64354419aaa62e963e5a7\",\"accesstoken\":\"CgB6e3x9X+B5nqI+ohFZxg8MVh1MoL6Gyx1CQ8am0E2eCUJMnVyF0+McdbJ6BvNv27ycPbiBRIQ/FO85xyvTukK8a9f7fIVS0GxInCePaeeLzsDk1o8u\",\"siteID\":\"1\"}"; csrfToken=267EE42D0B695062E88B354E9CCF1E5356830E8818540200D3; x-siteId=1; x-hd-grey=alnc-0; x-teamId=; x-country=CN; x-userType=2; state=5922669; urlBeforeLogin=https%3A%2F%2Fdeveloper.huawei.com%2Fconsumer%2Fcn%2Fconsole%23%2FopenCard%2FThemeService%2F1057; developer_userinfo=%7B%22siteid%22%3A%221%22%2C%22expiretime%22%3A%2220210618T103201Z%22%2C%22csrftoken%22%3A%22267EE42D0B695062E88B354E9CCF1E5356830E8818540200D3%22%7D'
headers_token = {
    "Host": "svc-drcn.developer.huawei.com",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": "https://developer.huawei.com",
    "Connection": "keep-alive",
    "Referer": "https://developer.huawei.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Cookie": Cookie

}

def get_token():
    url = "https://svc-drcn.developer.huawei.com/svc/feedsconnect/contentproviderconn/v1/dlbrowsermgrtoken/query"
    result_token = requests.get(url, headers=headers_token)
    return result_token

headers = {
    "Host": "svc-drcn.developer.huawei.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json;charset=utf-8",
    "browserMgrToken": get_token().text[1:-1],
    "Content-Length": '87',
    "Origin": "https://developer.huawei.com",
    "Connection": "keep-alive",
    "Referer": "https://developer.huawei.com/",
    "Cookie": Cookie

}


timestamp = str(int(time.time() * 1000))+'419762'



def request_server():
    url = 'https://svc-drcn.developer.huawei.com/svc/feedsconnect/contentproviderconn/v1/exportTopN'
    payload = {'requestType':'1','ctype':'news','head':{'seq':timestamp,'remoteAddr':''}}
    return requests.post(url, headers=headers,json=payload)


def queryPublishContent(ctype,startTime,endTime,page,pageSize):
    browserMgrToken = get_token().text[1:-1]
    headers = {
        "Host": "svc-drcn.developer.huawei.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json;charset=utf-8",
        "browserMgrToken": browserMgrToken,
        "Content-Length": '87',
        "Origin": "https://developer.huawei.com",
        "Connection": "keep-alive",
        "Referer": "https://developer.huawei.com/",
        "Cookie": Cookie

    }

    url = 'https://svc-drcn.developer.huawei.com/svc/feedsconnect/contentproviderconn/v1/content/querypublishcontent'
    payload = {"ctype":ctype,"sourceType":"1","status":"P","startTime":startTime,"endTime":endTime,"sourceId":[],"queryKey":"","page":page,"pageSize":pageSize,"head":{"seq":"1623999561464566556","remoteAddr":""}}
    return requests.post(url,headers=headers,json=payload).json()


def parse_detail(content):

    return {

        'docId': content['docId'],

        'hwDocId': content['hwDocId'],

        'title': content['title'],

        'imgUrl': content['imgUrl'],

        'imageUrls': content['imageUrls'],

        'source': content['source'],

        'ctype': content['ctype'],

        'dtype': content['dtype'],

        'updateTime': content['updateTime'],

        'publishTime': content['publishTime'],

        'creatTime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),

        'version': content['version'],

        'canEdit': content['canEdit'],

        'contentSyncStatus': content['contentSyncStatus'],

        'cpMode': content['cpMode'],

        'docStatus': content['docStatus'],

        'statusDetail': content['statusDetail'],

        'hwUrl': content['hwUrl'],

        'contentConsumptionInfo': content['contentConsumptionInfo']
    }

def save_data(data):
    collection.insert_one(data)


def save_data_news(cur_page):
    jsonobj = queryPublishContent("news", "2021-06-16", "2021-06-16", cur_page, 50)
    result = jsonpath.jsonpath(jsonobj, '$.content[*]')
    for content in result:
        data = parse_detail(content)
        save_data(data)

def main():

    jsonobj = queryPublishContent("news", "2021-06-16", "2021-06-16", 1, 50)
    pageSplitInfo = jsonpath.jsonpath(jsonobj, '$.pageSplitInfo')[0]
    total_data = pageSplitInfo['total']
    cur_page = pageSplitInfo['cur']
    page_size = pageSplitInfo['pageSize']
    total_page = math.ceil(total_data / page_size)
    for i in range(cur_page,total_page+1):
        time.sleep(2)
        print(str(total_page)+"\t"+str(i))
        try:
            save_data_news(i)
        except Exception as e:
            print(i)


if __name__ == '__main__':
    print(get_token().text)
    # print(timestamp)
    # res = request_server()
    # print(res.ok)
    # with open("C:/Users/Administrator/Desktop/test.xlsx","wb") as f:
    #     f.write(res.content)

    # print(queryPublishContent("news", "2021-06-16", "2021-06-16", 1, 50))
    # save_data_news(1)
    # time.sleep(10)
    # save_data_news(83)
    # main()