#get the numbers of given website
#extract the numbers and find the summary
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_676716.json').read()


info1 = json.loads(fhand)

summary, counter = 0, 0

for item in info1['comments']:
    counter += 1
    summary += int(item["count"])

print('Count: ', counter)
print('Sum: ', summary)

