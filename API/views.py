from django.shortcuts import render, redirect
from pwn import *
from django.contrib import  messages
import requests

def createMath(requset):
    if requset.method == "GET":
        try:
            req = remote('112.137.129.129', 27001)
            PKT_HELLO = p32(0) + p32(8) + b"19020235"
            req.send(PKT_HELLO)
            while True:
                result = req.recv(2000)
                if int.from_bytes(result[0:4], "little") == 0:
                    result = result[8:]
                while int.from_bytes(result[0:4], "little") == 1:
                    a = int.from_bytes(result[8:12], "little")
                    b = int.from_bytes(result[12:16], "little")
                    PKT_RESULT = p32(2) + p32(4) + p32(a + b)
                    req.send(PKT_RESULT)
                    result = req.recv(2000)
                if int.from_bytes(result[0:4], "little") == 3:
                    break
                if int.from_bytes(result[0:4], "little") == 4:
                    messages.info(requset,result[8:len(result) - 1].decode())
                    break
            req.close()
        except:
            pass
    return redirect("ctf:home")
    # return render(requests, 'html/home.html')