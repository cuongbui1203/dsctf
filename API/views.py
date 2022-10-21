from django.shortcuts import render, redirect
from pwn import *
from django.contrib import messages
import requests
from CTF.forms import *


class Match():
    gameIP= ''
    gameID = ''
    uID1 = ''
    uID2 = ''
    keymath = ''
    status = ('chưa bắt đầu', 'đang diễn ra', 'kết thúc')

    def change_value(self):
        self.gameID += 1

    def __init__(self,ip, gameID, uid1, uid2, keymath):
        self.gameIP = ip
        self.gameID = gameID
        self.uID1 = uid1
        self.uID2 = uid2
        self.keymath = keymath

MATCH = []
def updateMatch():
    host = '127.0.0.1'
    port = 8888
    server_socket = socket.socket()
    server_socket.bind((host, port))
    print("start server:")
    server_socket.listen(40)
    while True:
        try:
            conn, address = server_socket.accept()
            print("Connection from: " + str(address))
            while True:
                try:
                    data = conn.recv(1024)
                    if data is not None:
                        data = struct.unpack('iii',data)
                        matchID = data[0]
                        winer = data[1]
                        status = data[2]
                        for match in MATCH:
                            if status==1 and  matchID == match.gameID and address==match.gameIP:
                                user = User.objects.filter(id=winer).first()
                                user.userScore+=1
                                user.save()
                                conn.send(b'ok')
                                conn.close()
                        conn.send(b'no')
                except:
                    pass
            conn.close()
        except:
            pass

def createMatch(request):
    if request.method == "POST":
        error_messages = {
            "ip_valid": (f'The game IP address "%s" is not valid'),
            "connect_server": (f'Can\'t connect to "%s"'),
        }
        form = MatchForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get('id')
            ip = form.cleaned_data.get('ip')
            port = form.cleaned_data.get('port')
            uid1 = form.cleaned_data.get('uid1')
            uid2 = form.cleaned_data.get('uid2')
            keymath = form.cleaned_data.get('keymath')
            try:
                if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
                    messages.error(request, error_messages['ip_valid'])
                else:
                    try:
                        req = remote(ip, port)
                        CREATE_MATCH = p32(int(id))+p32(int(uid1))+p32(int(uid2))+p32(len(keymath))
                        print(CREATE_MATCH)
                        req.send(CREATE_MATCH)
                        result = req.recv(1024).decode()
                        if result == 'ok':
                            MATCH.append(Match(ip,id, uid1, uid2, keymath))
                        req.close()
                        messages.info(request, "tao van dau thanh cong")
                        print(5)
                    except Exception as e:
                        messages.error(request, error_messages['connect_server'] % ip)
                        print(e)
            except:
                messages.error(request, 'none')
        return redirect("ctf:home")
    return redirect("ctf:home")
    # return render(requests, 'html/home.html')
