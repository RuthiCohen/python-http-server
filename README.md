## Python HTTP server project

### This project consists of 3 different parts:

1. **First part:**
    In this part I've built a small http web server that supports 3 methods:
    a. get a country by given an ip.
    b. get all ips data by given a country.
    c. get the top 5 countries by the max number of ips associated to them.
    
    In order to run the server open the terminal & type:

    `cd httpServer`

    `uvicorn main:app --reload`

    open a new terminal & type:

    `redis-server`
2. **Second part:**
    In this part you can see 3 different attacks: http response splitting, syn flooding, url brute force.
    In order to run the attack:

    `cd attacks/<your-specific-attack-folder>`

    and then run:

    `sudo python3 <the-python-attack-file>`

    In order to see the packages that comes to the server open a new terminal & type:
    `sudo tcpdump -nn -i any  port 8000`
3. **Third part:**
    In this part I've added a Nginx proxy to the server as a reversed proxy.
    open a terminal & type:

    `cd proxy`

    `sudo python3 nginx.py`

## Technologies:
    Python3
    Redis DB