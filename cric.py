
import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://www.cricbuzz.com').read()
soup = bs.BeautifulSoup(sauce,'lxml')

print(soup.get_text())
