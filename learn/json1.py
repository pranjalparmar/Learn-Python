import json
import ssl
from urllib import request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1062094.json'
html = request.urlopen(url)
data = html.read()

info = json.loads(data)
sum = 0
a = info.get('comments')

for item in a:
    b = item['count']
    sum+=b
print(sum)