# 豆瓣影评爬虫

# Tutorial

运行mysql
```
brew services start mysql
mysql -u root -p
source init.sql
```

首先，执行爬虫池
```
cd Proxy_Pool/Run
python3 main.py
```

启动任务队列
```
redis-server
```

获取url放到队列中
```
python3 spider.py
```

开始从任务队列中获取任务执行
```
python3 worker.py
```

# TodoList
* 数据库分表存储
* 爬取全站

# 参考资料
1. [Python BloomFilter](https://axiak.github.io/pybloomfiltermmap/ref.html)
2. [rq](http://python-rq.org/docs/)
3. [lanbing510/DouBanSpider](https://github.com/lanbing510/DouBanSpider)
