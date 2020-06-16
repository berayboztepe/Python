
#it's an example of http reading
#with socket module, we connect to the web server(80 means web server and 'data.pr4e.org' means host that we connect)
#with get, we connect it and get infos about that http data:
"""HTTP/1.1 200 OK
Date: Tue, 16 Jun 2020 10:48:15 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "1d3-54f6609240717"
Accept-Ranges: bytes
Content-Length: 467
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain"""
#encode() means write them as UTF8 format(which is our writing lang, not html format) and send it
#with while loop, we recive(512 byte) datas and prompt them to console. When len(data) comes to 1, it breaks the loop and close the website
#otherwise, it prompts the text file(or whatever, maybe jpg, maybe another thing... etc.) to the console.
#with decode() we decode it and prompt it in a good shape
"""Why should you learn to write programs?

Writing programs (or programming) is a very creative 
and rewarding activity.  You can write programs for 
many reasons, ranging from making your living to solving
a difficult data analysis problem to having fun to helping
someone else solve a problem.  This book assumes that 
everyone needs to know how to program, and that once 
you know how to program you will figure out what you want 
to do with your newfound skills.""" #this is with decode()

#b'HTTP/1.1 200 OK\r\nDate: Tue, 16 Jun 2020 10:57:09 GMT\r\nServer: Apache/2.4.18 (Ubuntu)\r\nLast-Modified: Sat, 13 May 2017 11:22:22 GMT\r\nETag: "1d3-54f6609240717"\r\nAccept-Ranges: bytes\r\nContent-Length: 467\r\nCache-Control: max-age=0, no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nExpires: Wed, 11 Jan 1984 05:00:00 GMT\r\nConnection: close\r\nContent-Type: text/plain\r\n\r\nWhy should you learn to write programs?\n\nWriting programs (or programming) is a very creative \nand rewarding activity.  You can write programs'b' for \nmany reasons, ranging from making your living to solving\na difficult data analysis problem to having fun to helping\nsomeone else solve a problem.  This book assumes that \neveryone needs to know how to program, and that once \nyou know how to program you will figure out what you want \nto do with your newfound skills.  \n'
#this is without decode!
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
