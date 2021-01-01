import socket

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set prot
port = 9999
ip = socket.gethostbyname(socket.gethostname())
# connect
s.connect((ip, port))

# recieve
while True:
    msg = s.recv(1024)
    if msg:
        print("from server: "+msg.decode('utf-8'))
    else:
        print("server close!")
        exit()