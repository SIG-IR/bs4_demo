from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('https://www.reddit.com/').read()
soup = BeautifulSoup(r, "html.parser")
#print type(soup)
#print soup
#print soup.prettify()
#print soup.text



#content = soup.find_all("div", class="content")
#print content