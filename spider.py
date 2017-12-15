import requests
import re
from redis import Redis
from rq import Queue
from bs4 import BeautifulSoup
from pybloomfilter import BloomFilter
from utils import get_html,get_proxy,delete_proxy,get_content

q = Queue(connection=Redis(host='localhost',port=6379))

bloom_f = BloomFilter(capacity=100000, error_rate=0.01)

def spider():
    # Get Pages
    url = "https://movie.douban.com/subject/1441053/reviews?start="
    head = get_html(url+str(0))
    temp_html = BeautifulSoup(head.content,"lxml").select("#content > h1")
    print(temp_html)

    text = temp_html[0].text
    page = int(re.sub(r"\D*","", text))
    data = []

    for page_num in range(page//20+1):
        proxy = get_proxy()
        req = get_html(str.encode(url+str(page_num*20)))
        #bloom_f.add(url+str(page_num*20))
        #data.append(req)
        #For solving Chinese Code problem
        html = str(req.content,"utf-8")
        soup = BeautifulSoup(html,"lxml")

        div = soup.find("div",{'class':'review-list'})
        #print(div.prettify())
        #data.append(div.text)
        for review in div.select("div > h2 > a"):
            review_href = review['href']
            if str.encode(review_href) not in bloom_f:
                bloom_f.add(str.encode(review_href))
                job = q.enqueue(get_content,review_href)
                print(job.result)
            else:
                pass

            #print(review_href)

        #print(soup.prettify())
        #for review_info in div.find_all("")
        #for review in soup.find_all("")
    #data_out(data)


def init():
    pass


if __name__ == "__main__":
    init()
    #spider_url()
    spider()
