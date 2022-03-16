#!/usr/bin/python

USERNAME = "admin"


from websocket import create_connection
ws = create_connection("ws://web1.utctf.live:8651/internal/ws")

res = ws.recv()
print(res)
ws.send("begin")
ws.send(f"user {USERNAME}")
result =  ws.recv()

breakpoint()
ws.close()

