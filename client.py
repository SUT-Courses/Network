import sys
from socket import AF_INET, socket, SOCK_DGRAM, timeout

from utils.logger import logger, get_timestr_mil_sec

if len(sys.argv) != 3:
    logger(msg="🔥Not acceptable🔥 use 'python client.py <host> <port>")
    sys.exit(1)    

_, host, port = sys.argv


socket_client = socket(AF_INET, SOCK_DGRAM)
socket_client.settimeout(2)

for i in range(1,11):
    msg = f"Ping {i} {get_timestr_mil_sec()}"
    socket_client.sendto(msg.encode(), (host, int(port)))
    print(msg.encode())
    logger(msg=f"Sending from client: {msg}")
    try:
        data, addr = socket_client.recvfrom(1024)
        logger(msg=f"Received from server: {data.decode()}")
    except timeout:
        logger(msg=f"Request timed out: {i}")

