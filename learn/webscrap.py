import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#
# # Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

for tag in range(count):
    link = tags[position].get('href', None)
    name = tags[position].contents[0]
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

print(name)
        # Look at the parts of a tag
        # html = urllib.request.urlopen(tags[2], context=ctx).read()
        # soup = BeautifulSoup(html, 'html.parser')
        # print(tag.contents[0])



# soup = BeautifulSoup(html,"html.parser")
# href = soup('a')
#print href

# for i in range(count):
#     link = href[position].get('href',None)
#     print(href[position].contents[0])
#     soup = BeautifulSoup(html, 'html.parser')
#     html = urllib.request.urlopen(link, context=ctx).read()
#     href = soup('a')