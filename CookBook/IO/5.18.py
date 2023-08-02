# 将文件描述符包装成文件对象
import os
import sys
from socket import socket, AF_INET, SOCK_STREAM


# 你有一个对应于操作系统上一个已打开的I/O通道(比如文件、管道、套接字等)的整型文件描述符，你想将它包装成一个更高层的Python文件对象。
fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)
# 变成正确的文件
f = open(fd, 'wt')
f.write('hello world\n')
f.close()


def echo_client(client_sock, addr):
    print('Got connection from', addr)
    # Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                     closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                      closefd=False)
    # 使用文件I/O将线路回显到客户端
    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)

# 上面的例子仅仅是为了演示内置的 open() 函数的一个特性，并且也只适用于基于Unix的系统


# 为stdout创建一个二进制模式文件
bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(b'Hello World\n')
bstdout.flush()


