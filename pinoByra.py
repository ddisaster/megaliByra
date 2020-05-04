#!/usr/bin/env python3
import socket

print("Let's start")

yolo = "A" * (2048))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.178.10", 7042))
s.send(yolo)

s.close()

print("Finished")
