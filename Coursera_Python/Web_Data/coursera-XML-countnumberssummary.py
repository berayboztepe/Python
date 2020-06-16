#read a webfile, extract the numbers which is in count element in XML code
#find the summary

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#print http://py4e-data.dr-chuck.net/comments_676715.xml
fhand = input('Enter Location: ')
url = urllib.request.urlopen(fhand).read()
summary, counter = 0, 0

comment = ET.fromstring(url)
lst = comment.findall('comments/comment')
for line in lst:
    counter += 1
    summary += int(line.find('count').text)

print("Count: ", counter)
print("Sum: ", summary)