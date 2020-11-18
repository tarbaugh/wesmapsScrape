from bs4 import BeautifulSoup
import urllib.request
import time
import os

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

while True:
    page = urllib.request.urlopen('https://owaprod-pub.wesleyan.edu/reg/!wesmaps_page.html?stuid=&facid=NONE&crse=016045&term=1211')
    soup = BeautifulSoup(page, 'html.parser')
    info = soup.find(id='print_sect_info')
    table = info.find('table')
    trs = table.find_all('tr')
    td = trs[3].find('td')
    if td.string == 'Seats Available: 0':
        print('Unavailable')
    else:
        notify("WesMaps", "Check Software Engineering")
    time.sleep(60)
