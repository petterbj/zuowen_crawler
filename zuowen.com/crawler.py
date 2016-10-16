import bs4
import urllib2
import sys
# page_url = 'http://k.zuowen.com/list/xx/a9b11/'
def crawler_page(page_url):
    html = urllib2.urlopen(page_url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    file_handler = open(soup.title.string + '.txt','w')
    print soup.title.string.encode('utf8')
    file_handler.write(soup.findAll('h1')[0].string.encode('utf8'))
    file_handler.write('\n')
    for i in soup.findAll('div', class_='con_content')[0].findAll('p')[:-1]:
        if not i.string == None:
            file_handler.write(i.string.encode('utf8'))
            file_handler.write('\n')
    file_handler.close()
def crawler_page_list(page_url):
    html = urllib2.urlopen(page_url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for entry in soup.findAll('div', class_='zw_item')[0].findAll('dl'):
        crawler_page(entry.find('dt').find('h3').find('a')['href'])
if __name__ == "__main__":
    print sys.argv[1]
    crawler_page_list(sys.argv[1])
# #    for i in range(0, 100):
# #        crawler_page_list('http://www.zuowenku.net/wunianji-' + str(i) + '.shtml')
