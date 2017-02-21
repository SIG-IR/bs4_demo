from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

import urllib
import requests
import IPython

r = requests.get("http://www.cnn.com/2017/02/21/politics/donald-trump-republican-support/index.html")
soup = BeautifulSoup(r.text, "html.parser")


print "CNN Article:"

print "Title:"
article_title = soup.find("h1", {"class": "pg-headline"})
print article_title.text

print "Update Time:"
article_time = soup.find("p", {"class": "update-time"})
print article_time.text

print "Content:"
article_content = soup.find("section", {"class": "zn-body-text"})
print article_content.text