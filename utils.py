import requests
import re
from bs4 import BeautifulSoup
# use Proxy_Pool
def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


def data_out(data):
    f = open("data.html","w")
    f.write("\n".join(data))
    f.close()

def spider_url():
    uri = "https://movie.douban.com/people/seanRebn/collect"

def get_html(url):
    retry_count = 5
    proxy = get_proxy()
    while retry_count > 0:
        try:
            req = requests.get(url, proxies={"http": "http://{}".format(proxy)})
            return req
        except Exception:
            retry_count -= 1
    delete_proxy(proxy)
    return None

def get_content(url):
    html = BeautifulSoup(get_html(url).content,"lxml")
    print(type(html))
    doc = html.select("#link-report > div")[0]
    print(doc.text)
