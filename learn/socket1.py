import socket
import urllib.request, urllib.parse, urllib.error

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)) < 1:
        break
    else:
        print(data.decode())
mysock.close()

## Alternate way of only extracting data and not headers

fhandle = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')

count = dict()

for line in fhandle:
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word,0) + 1
print(count)
