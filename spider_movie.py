import requests
import re
import json
from redis import Redis
from rq import Queue
from bs4 import BeautifulSoup
from pybloomfilter import BloomFilter
from utils import get_html,get_proxy,delete_proxy,get_content
from urllib.parse import urlencode
from spider_comment import spider_movie_comment

high =Queue('high',connection=Redis(host='localhost',port=6379))

bloom_movie = BloomFilter(capacity=100000,error_rate=0.01)

def spider_movie(tag,pages):
    # https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E5%89%A7%E6%83%85&start=10
    for page_num in range(pages):
        url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags="+tag+"&start="+str(10*page_num)

        req = get_html(url)
        js_data = json.loads(req.text)
        for key in js_data["data"]:
            #print(key["id"])
            if str.encode(key["id"]) not in bloom_movie:
                bloom_movie.add(str.encode(key["id"]))
                job = high.enqueue(spider_movie_comment,key["id"])
                print(job)
        with open("data.json","a") as fp:
            json.dump(js_data,fp,indent=4)

        #print(js_data)


def init():
    list = ["剧情","爱情","喜剧","科幻","动作", "悬疑", "犯罪", "恐怖", "青春", "励志", "战争","文艺", "黑色幽默","传记","情色","暴力", "音乐","家庭"]
    return list


if __name__ == "__main__":
    tag_list = init()
    for tag in tag_list:
        spider_movie(tag,1)
    #spider_url()
    #spider_movie_comment()
