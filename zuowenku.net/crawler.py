import bs4
import urllib2
import sys
page_url = 'http://www.zuowenku.net/1000160.shtml'
def crawler_page(page_url):
    html = urllib2.urlopen(page_url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    file_handler = open(soup.title.string + '.txt','w')
    file_handler.write(soup.findAll('div', id='zwdetail')[0].findAll('h1')[0].string.encode('utf8'))
    file_handler.write('\n')
    for i in soup.findAll('div', style='clear:both')[0].findAll('p'):
        file_handler.write(i.string.encode('utf8'))
        file_handler.write('\n')
    file_handler.close()
def crawler_page_list(page_url):
    html = urllib2.urlopen(page_url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for entry in soup.findAll('td', class_='s_l')[0].findAll('ol')[0].findAll('li'):
        crawler_page(entry.find('h3').find('a')['href'])
if __name__ == "__main__":
    # pass the url of the zuowen page list as a parameter
    print sys.argv[1]
    crawler_page_list(sys.argv[1])
#    for i in range(0, 100):
#        crawler_page_list('http://www.zuowenku.net/wunianji-' + str(i) + '.shtml')
