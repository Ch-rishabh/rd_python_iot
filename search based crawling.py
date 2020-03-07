import urllib.request as req
import bs4 #BeautifulSoup

search = input("Search product : ")
url = f"https://www.flipkart.com/search?q={search}"

res = req.urlopen(url)

html = bs4.BeautifulSoup(res, 'lxml')

a_tag_list = html.find_all('a', '_2mylT6')

for a_tag in a_tag_list:
    print(a_tag.text)
