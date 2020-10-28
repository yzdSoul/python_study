import asyncio
from pyppeteer import launch

def Proxies():
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"
    # 代理隧道验证信息
    proxyServer = "http://" + proxyHost + ":" + proxyPort
    return proxyServer
def Authens():
    proxyUser = "HM83Z2M4A24KXGLD"
    proxyPass = "0A1DBF55E49881D7"
    authen = {"username": proxyUser, "password": proxyPass}
    return authen
async def main():
    # headless参数设为False，则变成有头模式
    browser = await launch(headless=True, args=['--disable-infobars',"--proxy-server=" + Proxies()])  # headless=True 启动了无头模式，--proxy-server 启动了代理
    page = await browser.newPage()
    await page.authenticate(Authens())  # 输入代理账号密码
    await page.setExtraHTTPHeaders(Proxies())              # 在pyppeteer中和puppeteer是一样的，都不能把隧道加在args里，只能加在headers里
    # 设置页面视图大小
    await page.setViewport(viewport={'width': 1280, 'height': 800})

    url = 'https://www.qimai.cn/rank/marketRank/market/6/category/6/date/2020-01-20'
    # 是否启用JS，enabled设为False，则无渲染效果
    await page.setJavaScriptEnabled(enabled=True)
    await page.goto(url)
    # 打印页面cookies
    # print(await page.cookies())
    # 打印页面文本
    print(await page.content())
    # 打印当前页标题
    print(await page.title())
    # 抓取新闻标题
    title_elements = await page.xpath('//div[@class="app-info"]/a')
    for item in title_elements:
        # 获取文本
        title_str = await (await item.getProperty('textContent')).jsonValue()
        print(await item.getProperty('textContent'))
        # 获取链接
        title_link = await (await item.getProperty('href')).jsonValue()
        print(title_str)
        print(title_link)

    # 关闭浏览器
    await browser.close()




asyncio.get_event_loop().run_until_complete(main())