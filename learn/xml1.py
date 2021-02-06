import urllib.request, urllib.parse, urllib.error
from urllib import request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1062093.xml'
html = request.urlopen(url)
data = html.read()

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
sum = 0

for item in results:
    name = item.find('name').text
    count = item.find('count').text
    sum = sum + int(count)

print(sum)