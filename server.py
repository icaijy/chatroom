import socket

from threading import Thread
def moreFunc(**kwargs):
    threads = []
    for func, args in kwargs.items():
        threads.append(Thread(target=globals()[func],args=args))
    for t in threads:
        t.start()

'''
AF_INET: IPv4
AF_INET6: IPv6
SOCK_STREAM: TCP 
'''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def waitconnect():
    # listen
    ip = socket.gethostbyname(socket.gethostname())
    port = 9999

    print(ip)
    s.bind((ip, port))


    # largest connection
    # now will wait for connection
    s.listen(5)
    return None


while True:
    waitconnect()
    client,addr = s.accept()     # start connection
    while True:
        msg = input("send: ")
        client.send(msg.encode('utf-8')) # send bytes
    #client.close() # close connection
