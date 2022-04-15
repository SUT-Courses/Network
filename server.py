# sajad faghfoor maghrebi
# 97106187

import random
import sys
import time

from socket import AF_INET, socket, SOCK_DGRAM
from utils.logger import logger, get_timestr_mil_sec, check_command

check_command(num_args=2, correct_command="'python server.py <port>'")
port = int(sys.argv[1])

# init server
socket_server = socket(AF_INET, SOCK_DGRAM)
socket_server.bind(('', port))

logger(f"Server started on port {port}")

while True:
    # msg received from client
    msg, addr = socket_server.recvfrom(1024)
    logger(f"Received from client: {msg.decode()}")
    
    # perform actions on msg
    modified_msg = msg.decode().upper()
    time.sleep(1)

    # simulate packet loss
    if random.random() < 0.7:
        socket_server.sendto(modified_msg.encode(), addr)
        logger(f"Sending to client: {modified_msg}")