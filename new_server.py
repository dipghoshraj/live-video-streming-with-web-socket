import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import zlib

HOST='127.0.0.1'
PORT=8485
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')
s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')
conn,addr=s.accept()
print("accepted")


