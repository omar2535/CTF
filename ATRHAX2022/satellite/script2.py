import socket
import sys
import os
import struct
from ctypes import *
import threading
import select
import time

''''Procotol Services'''
bus_service = b'\x01'
payload_service = b'\x02'
telemetry_service = b'\x03'
control_service = b'\x04'
disconnect_service = b'\x05'

'''Protocol fields'''
length = b'\x12'
fragment_id = b'\x00'
data = b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaac'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(sock):
    #server_address = ("0.cloud.chals.io", 34357)
    server_address = ("0.cloud.chals.io", 34357)
    sock.connect(server_address)

def transceive_packet(sock, service, length, fragment_id, data):
    count = 0
    if service==telemetry_service:
        while count < 11:
            fragment_id = struct.pack('>B',count)
            packet = service + length + fragment_id + data
            sock.send(packet)
            count = count+1
            time.sleep(0.2)#must keep this delay between packets for tranmission sync with satellite
                      
        packet = service + length + fragment_id + b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacaaa\x01'
        sock.send(packet)
        time.sleep(0.2)
        
        packet = service + length + fragment_id + b'\x01aaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacaaa\x01'
        sock.send(packet)
        time.sleep(0.2)
            
        packet = control_service + length + b'\x00' + data
        sock.send(packet)
        count = 0
        while count <=3:
            data = sock.recv(74)
            print(data)
            count = count+1
            time.sleep(0.2)#must keep this delay between packets for tranmission sync with
    else:
        packet = service + length + fragment_id + data
        sock.send(packet)
        while count <=3:
            data = sock.recv(74)
            print(data)
            count = count+1
            time.sleep(0.2)#must keep this delay between packets for tranmission sync with satellite

connect(sock)
transceive_packet(sock, telemetry_service, length, fragment_id, data)