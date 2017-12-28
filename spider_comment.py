import requests
import re
import json
from redis import Redis
from rq import Queue
from bs4 import BeautifulSoup
from pybloomfilter import BloomFilter
from utils import get_html,get_proxy,delete_proxy,get_content
from urllib.parse import urlencode

low = Queue('low',connection=Redis(host='localhost',port=6379))

bloom_f = BloomFilter(capacity=100000, error_rate=0.01)


def spider_movie_comment(movie_id):
    # Get Pages
    url = "https://movie.douban.com/subject/"+movie_id+"/reviews?start="
    head = get_html(url+str(0))
    html = BeautifulSoup(head.content,"lxml")
    temp_html = html.select("#content > h1")
    print(temp_html)
    # f = open("index.html","w")
    # f.write(html.prettify())
    # f.close()

    text = temp_html[0].text
    page = int(re.sub(r"\D*","", text))
    data = []

    for page_num in range(page//20+1):
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
                job = low.enqueue(get_content,review_href)
                print(job.result)
            else:
                pass

if __name__ == '__main__':
    spider_movie_comment('1292213')
