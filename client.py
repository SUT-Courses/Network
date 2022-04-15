# sajad faghfoor maghrebi
# 97106187

import sys
import time
from socket import AF_INET, socket, SOCK_DGRAM, timeout

from utils.logger import logger, get_timestr_mil_sec, check_command

check_command(num_args=2, correct_command="'python client.py <port>'")    

# server information
host, port = "127.0.0.1", sys.argv[1]

# init server
socket_client = socket(AF_INET, SOCK_DGRAM)
logger(f"Client started on port {port}")

# init timeout
socket_client.settimeout(2)

# [1 .. 10]
for i in range(1,11):
    msg = f"Ping {i} {get_timestr_mil_sec()}"
    
    # simulate some work in the client
    time.sleep(1)  
    
    # send to server
    socket_client.sendto(msg.encode(), (host, int(port)))
    logger(msg=f"Sending from client: {msg}")

    try:
        # received
        data, addr = socket_client.recvfrom(1024)
        logger(msg=f"Received from server: {data.decode()}")
    except timeout:
        # timeout
        logger(msg=f"Request timed out: {i}")

