from fastapi import FastAPI
from MyRedis import create_redis
from datetime import datetime
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello friends, how you do'in? ;)"}
    
# ex ip: 39.110.142.79
@app.get("/{ip}")
async def get_country_by_ip(ip:str):
    myRedis = create_redis()
    # myRedis.flush_redis()

    # check if ip already in data
    if myRedis.is_ipv4_exists(ip):
        print('###### record already exists ####')
        return {"country_name": myRedis.get_ip_record(ip)['country_name']}

    # find the ip data
    res = requests.get(f"https://geolocation-db.com/json/67273a00-5c4b-11ed-9204-d161c2da74ce/{ip}&position=true")

    if res.status_code != 200:
        return {'error': 'request failed ... please try again'}

    res = res.json()
    if res["country_name"] == None:
        return {'error': 'ip does not exist....'}

    myRedis.add_record(res)
    myRedis.get_all_data() #!!!!!!!!!
    return {"country_name": res['country_name']}

@app.get("/countries/top-5")
async def get_top_5_countries():
    myRedis = create_redis()
    top_5_countries = myRedis.get_5_top_countries()
    myRedis.get_all_data() #!!!!!!!!!
    return {"top 5 countries": top_5_countries}

@app.get("/countries/{country_name}")
async def get_ips_by_country(country_name: str, start_time: datetime = None , end_time: datetime = None):
    myRedis = create_redis()

    if not myRedis.is_country_exists(country_name):
        return {'error': f'no data were found for country {country_name}'}

    ips = myRedis.get_ips_by_country(country_name, start_time, end_time)
    return {'country_name':country_name, 'country_ips': ips}
