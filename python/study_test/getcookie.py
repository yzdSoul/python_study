from urllib.parse import urljoin
from selenium import webdriver
import requests
import time

from selenium.webdriver.remote.webelement import WebElement

BASE_URL = 'https://developer.huawei.com/consumer/cn/console'
# BASE_URL = 'https://id1.cloud.huawei.com/'
LOGIN_URL = urljoin(BASE_URL, '/CAS/portal/loginAuth.html')
INDEX_URL = urljoin(BASE_URL, '/AMW/portal/userCenter/index.html')
USERNAME = '18601017142 '
PASSWORD = 'wuli2020'

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(options=options)
# browser = webdriver.Firefox()
browser.get(BASE_URL)
time.sleep(3)

# get cookies from selenium
browser.delete_all_cookies()
cookies = browser.get_cookies()
print('Cookies', cookies)
Cookies =  [
    {'name': 'CAS_THEME_NAME', 'value': 'red', 'domain': '.id1.cloud.huawei.com', 'path': '/'},
    {'name': 'cookieBannerOnOff', 'value': 'false', 'domain': 'id1.cloud.huawei.com', 'path': '/'},
    {'name': 'cversion', 'value': '40200', 'domain': 'id1.cloud.huawei.com', 'path': '/DimensionalCode/'},
    {'name': 'expiredTime', 'value': '1624601698139', 'domain': 'id1.cloud.huawei.com', 'path': '/DimensionalCode/'},
    {'name': 'HW_id_id1_cloud_huawei_com_id1_cloud_huawei_com', 'value': 'aeeac28d75c94a418e77c7f9e3aaa438', 'domain': 'id1.cloud.huawei.com', 'path': '/'},
    {'name': 'HW_idn_id1_cloud_huawei_com_id1_cloud_huawei_com', 'value': '7536467afb1e4658b1da80ea465c6af9', 'domain': 'id1.cloud.huawei.com', 'path': '/'},
    {'name': 'HW_idts_id1_cloud_huawei_com_id1_cloud_huawei_com', 'value': '1622080780181', 'domain': 'id1.cloud.huawei.com', 'path': '/'},
    {'name': 'HW_idvc_id1_cloud_huawei_com_id1_cloud_huawei_com', 'value': '40', 'domain': 'id1.cloud.huawei.com', 'path': '/'},
    {'name': 'HW_refts_id1_cloud_huawei_com_id1_cloud_huawei_com', 'value': '1622080780179', 'domain': 'id1.cloud.huawei.com', 'path': '/'},
    {'name': 'HW_viewts_id1_cloud_huawei_com_id1_cloud_huawei_com', 'value': '1624597917234', 'domain': 'id1.cloud.huawei.com', 'path': '/'},
    {'name': 'hwid_cas_sid', 'value': '204937da38a7b586a92475b788beef4d9f0c9edeed7dc7400469639fabe9659dbb1b0f1a3fa0370d3786', 'domain': '.id1.cloud.huawei.com', 'path': '/'},
    {'name': 'JSESSIONID', 'value': 'DF8E9ACE5BEF4A97519EF5F59D24281D4A0E0AC104F8DCF4', 'domain': 'id1.cloud.huawei.com', 'path': '/AMW'},
    {'name': 'JSESSIONID', 'value': '0EC50C51EC4A3C794AD0B0A3912A8918B4F2053FA0C66634', 'domain': 'id1.cloud.huawei.com', 'path': '/CAS'},
    {'name': 'JSESSIONID', 'value': '16F26121E70B554EBCFC743210E5829F', 'domain': 'id1.cloud.huawei.com', 'path': '/DimensionalCode'},
    {'name': 'notify_fill_age_ED32A6C5F56047752B293FB2128A3CA835F2B11BEC33AACB0FD7A0BB470FE323', 'value': 'true', 'domain': '.id1.cloud.huawei.com', 'path': '/'},
    {'name': 'qrCodeCreateTime', 'value': '1624601517139', 'domain': 'id1.cloud.huawei.com', 'path': '/DimensionalCode/'},
    {'name': 'qRCode', 'value': 'QrCode_wECxibUrq3sywtsaXXlFqdshC6mdVOQq', 'domain': 'id1.cloud.huawei.com', 'path': '/DimensionalCode/'},
    {'name': 'sid', 'value': '204937da38a7b586a92475b788beef4d9f0c9edeed7dc7400469639fabe9659dbb1b0f1a3fa0370d3786', 'domain': '.id1.cloud.huawei.com', 'path': '/'},
    {'name': 'VERSION_NO', 'value': 'UP_CAS_5.3.0.100.SP1', 'domain': '.id1.cloud.huawei.com', 'path': '/'}
]
for cookie in Cookies:
    # print(cookie)
    browser.add_cookie(cookie)

cookies = browser.get_cookies()
print(print('Cookies', cookies))
time.sleep(3)
browser.maximize_window()
# browser.find_element_by_css_selector('input[class="hwid-input userAccount"]').click()
# result = browser.find_elements_by_xpath('//input[@type="text"]')
# result[1].click()
# print(text)
browser.find_elements_by_xpath('//input[@type="text"]')[1].send_keys(USERNAME)
browser.find_element_by_xpath('//input[@type="password"]').send_keys(PASSWORD)
browser.find_element_by_xpath('//div[@class="button-base-box"]').click()

data_indexurl = 'https://developer.huawei.com/consumer/cn/console#/openCard/ThemeService/1057'
time.sleep(10)
browser.get(data_indexurl)
time.sleep(5)
browser.find_element_by_xpath('//span[@class="icon icon-close appPromotion-icon"]').click()
browser.switch_to.frame("service_cards_iframe")
time.sleep(5)
browser.find_element_by_xpath('//*[contains(text()[1],"内容详情数据")]').click()
#
# time.sleep(3)
#
# logined_cookies = browser.get_cookies()
# print(logined_cookies)
#
# Cookie = ""
# for c in logined_cookies:
#     if c['name'] == 'authInfo':
#         Cookie = c['value']
#
# print(Cookie)
# time.sleep(10)
#
# # get cookies from selenium
# cookies = browser.get_cookies()
# print('Cookies', cookies)
# browser.close()
#
# # set cookies to requests
# session = requests.Session()
# for cookie in cookies:
#    session.cookies.set(cookie['name'], cookie['value'])
#
# response_index = session.get(INDEX_URL)
# print('Response Status', response_index.status_code)
# print('Response URL', response_index.url)