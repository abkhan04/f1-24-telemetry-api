import socket

udp_ip = '127.0.0.1'
udp_port = 5005

# AF_INET is Internet
# SOCK_DGRAM is UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((udp_ip, udp_port))

while True:
    data, addr = sock.recvfrom(1024) # Buffer size of 1024 bytes
