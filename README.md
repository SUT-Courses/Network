 python3 server.py 5550

[2022-04-14 19:37:00.213] Server started on port 5550

[2022-04-14 19:37:13.183] Received from client: Ping 1 2022-04-14 19:37:11.180

[2022-04-14 19:37:13.183] Sending to client: PING 1 2022-04-14 19:37:11.180

[2022-04-14 19:37:15.185] Received from client: Ping 2 2022-04-14 19:37:13.183

[2022-04-14 19:37:15.185] Sending to client: PING 2 2022-04-14 19:37:13.183

[2022-04-14 19:37:17.188] Received from client: Ping 3 2022-04-14 19:37:15.185

[2022-04-14 19:37:21.192] Received from client: Ping 4 2022-04-14 19:37:19.190

[2022-04-14 19:37:25.195] Received from client: Ping 5 2022-04-14 19:37:23.193

[2022-04-14 19:37:29.200] Received from client: Ping 6 2022-04-14 19:37:27.197

[2022-04-14 19:37:29.200] Sending to client: PING 6 2022-04-14 19:37:27.197

[2022-04-14 19:37:31.202] Received from client: Ping 7 2022-04-14 19:37:29.200

[2022-04-14 19:37:31.202] Sending to client: PING 7 2022-04-14 19:37:29.200

[2022-04-14 19:37:33.205] Received from client: Ping 8 2022-04-14 19:37:31.202

[2022-04-14 19:37:37.209] Received from client: Ping 9 2022-04-14 19:37:35.207

[2022-04-14 19:37:37.209] Sending to client: PING 9 2022-04-14 19:37:35.207

[2022-04-14 19:37:39.212] Received from client: Ping 10 2022-04-14 19:37:37.209

 python3 client.py 5550

[2022-04-14 19:37:11.180] Client started on port 5550

[2022-04-14 19:37:13.183] Sending from client: Ping 1 2022-04-14 19:37:11.180

[2022-04-14 19:37:13.183] Received from server: PING 1 2022-04-14 19:37:11.180

[2022-04-14 19:37:15.185] Sending from client: Ping 2 2022-04-14 19:37:13.183

[2022-04-14 19:37:15.185] Received from server: PING 2 2022-04-14 19:37:13.183

[2022-04-14 19:37:17.188] Sending from client: Ping 3 2022-04-14 19:37:15.185

[2022-04-14 19:37:19.190] Request timed out: 3

[2022-04-14 19:37:21.192] Sending from client: Ping 4 2022-04-14 19:37:19.190

[2022-04-14 19:37:23.193] Request timed out: 4

[2022-04-14 19:37:25.195] Sending from client: Ping 5 2022-04-14 19:37:23.193

[2022-04-14 19:37:27.197] Request timed out: 5

[2022-04-14 19:37:29.200] Sending from client: Ping 6 2022-04-14 19:37:27.197

[2022-04-14 19:37:29.200] Received from server: PING 6 2022-04-14 19:37:27.197

[2022-04-14 19:37:31.202] Sending from client: Ping 7 2022-04-14 19:37:29.200

[2022-04-14 19:37:31.202] Received from server: PING 7 2022-04-14 19:37:29.200

[2022-04-14 19:37:33.205] Sending from client: Ping 8 2022-04-14 19:37:31.202

[2022-04-14 19:37:35.207] Request timed out: 8

[2022-04-14 19:37:37.209] Sending from client: Ping 9 2022-04-14 19:37:35.207

[2022-04-14 19:37:37.209] Received from server: PING 9 2022-04-14 19:37:35.207

[2022-04-14 19:37:39.212] Sending from client: Ping 10 2022-04-14 19:37:37.209

[2022-04-14 19:37:41.214] Request timed out: 10
