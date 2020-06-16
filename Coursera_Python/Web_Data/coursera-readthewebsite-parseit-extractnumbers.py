#read the html code of a website and find the numbers in it
#then find the summary

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl, re
#print http://py4e-data.dr-chuck.net/comments_676713.html

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
summary = 0

tags = soup('span')
for tag in tags:
    #both codes are correct
    #tag1 = tag.decode().split('>')[1].split('<')[0]
    tag1 = re.findall('[0-9]+', tag.decode())
    summary += int(tag1[0])
    #summary += int(tag1)

print(summary)
