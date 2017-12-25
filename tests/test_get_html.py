# get_html_test.py
#

#from nose2.tools import *
import unittest
import sys
sys.path.append("..")
from utils import get_html,parse_html,data_out
from bs4 import BeautifulSoup
#import utils

class ContentTest(unittest.TestCase):
    def setUp(self):
        self.url = "https://movie.douban.com/review/8894086/"

    def test_get_html(self):
        req = BeautifulSoup(get_html(self.url).content, "lxml")
        #print(req.prettify())
        f = open("ht.html","w")
        f.write(req.prettify())
        f.close()
        #assert None == req, "Assert no html response"

    def test_parse_html(self):
        #assert parse_html(get_html(self.url)) is str,"Succeed get"
        req = get_html(self.url)
        html = parse_html(req)
        data_out(html)
        #print(html)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
    #t = ContentTest()
    #t.test_get_html()
    #t.test_parse_html()
