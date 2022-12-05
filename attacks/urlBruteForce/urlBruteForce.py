from threading import Thread
import requests
import time

target_url = "http://127.0.0.1:8000/login"
requests_per_second = 500

def send_request(target_url):
    try:
        requests.get(target_url)
    except Exception as e:
        pass

while True:
    for i in range(requests_per_second):
        t = Thread(target=send_request, args=(target_url,))
        t.start()
        print("sending package....")
    time.sleep(1)
