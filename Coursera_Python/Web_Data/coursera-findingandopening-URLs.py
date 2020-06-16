#enter given url, and find positionth URL
#go to that URL and find again positionth URL
#do that count times
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


count = int(input("Enter Count:"))
position = int(input("Enter Position:"))

l = []
for i in range(count+1):
    if i == 0:
        url = input('Enter - ')
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        print(url)

    else:
        print(l[position-1])
        url = l[position-1]
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
    l = []
    tags = soup('a')
    for tag in tags:
        a = tag.get('href', None)
        l.append(a)


