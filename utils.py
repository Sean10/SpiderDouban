import requests
import re
from bs4 import BeautifulSoup
from concurrent import futures
from database import db_open,db_insert
# use Proxy_Pool
def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


def data_out(data):
    fp = open("out.txt","a+")
    fp.write(data)
    fp.close()

def trans2database(title,content):
    connection = db_open()
    db_insert(connection, title,content)

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

def parse_html(req):
    html = BeautifulSoup(req.content, "lxml")
    #print(html.prettify())
    title = html.select("head > title")[0]
    content = html.select("#link-report > div")[0]
    #print(title.text)
    return title.text, content.text
    #print(doc.text)

def get_content(url):
    # workers = 20
    # with futures.ThreadPoolExecutor(workers) as executor:
    #     result = executor.map(get_html, url)
        #print(list(result)[0])
    req = get_html(url)
    title,content = parse_html(req)
    trans2database(title,content)
