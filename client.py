import socket
from threading import Thread
import os

def exit():
    '''
    exit
    :return: None
    '''
    os._exit(1)

def moreFunc(**kwargs):
    threads = []
    for func, args in kwargs.items():
        threads.append(Thread(target=globals()[func],args=args))
    for t in threads:
        t.start()


# socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set port
def connect(ip=socket.gethostbyname(socket.gethostname()),port=9999):
    # connect
    s.connect((ip, port))
    return None


# recieve

def receive():
    while True:
        try:
            msg = s.recv(1024)
            if msg:
                print("from server: "+msg.decode('utf-8'))
        except ConnectionResetError:
            print('server close')
            os._exit(1)


connect(ip=input("server's ip:"))
#keyboard.add_hotkey('ctrl+q',exit)
moreFunc(receive=())
