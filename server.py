import socket
from threading import Thread
import os
import keyboard

###################################################################
global client, addr
c = []
def exit():
    '''
    exit
    :return: None
    '''
    print("Bye\n")
    os._exit(1)


def moreFunc(**kwargs):
    '''
    run more functions
    :param kwargs:
    :return:
    '''
    threads = []
    for func, args in kwargs.items():
        threads.append(Thread(target=globals()[func],args=args))
    for t in threads:
        t.start()

def initconnect(port=9999):
    # listen
    ip = socket.gethostbyname(socket.gethostname())
    print(ip)
    s.bind((ip, port))
    # largest connection
    # now will wait for connection
    s.listen(5)
    return None


def send(msg):
    client.send(msg.encode('utf-8'))  # send bytes
####################################################################

# socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# if press esc, exit.
keyboard.add_hotkey('esc',exit)

initconnect()

client, addr = s.accept()  # start connection

while True:
    try:
        msg = input("send: ")
        send(msg)  # send bytes
    except:
        print("no connect!")
        client, addr = s.accept()  # start connection


