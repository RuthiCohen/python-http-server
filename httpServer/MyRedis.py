from datetime import datetime
from ast import literal_eval
from redisUtils import lower_word, str_2_date, date_2_str
import redis
import json

class MyRedis():
    def __init__(self, host, port):
        self.myRedis = redis.Redis(host=host, port=port)

    def flush_redis(self):
        self.myRedis.flushdb()
        self.myRedis.set('all_countries', json.dumps({}))

    def is_ipv4_exists(self, ipv4):
        if not self.myRedis.exists(ipv4):
            return False
        return True

    def is_country_exists(self, country):
        country = lower_word(country)
        countries_dict = json.loads(self.myRedis.get('all_countries'))

        if country not in countries_dict:
            return False
        return True

    def add_record(self, record):
        ipv4 = record['IPv4']
        ipv4_country = lower_word(record['country_name'])
        current_time = date_2_str(datetime.now())

        self.myRedis.set(ipv4, json.dumps({"country_name": ipv4_country, "time": current_time}))
        self.add_country(ipv4_country)

    def add_country(self, country):
        countries_dict = json.loads(self.myRedis.get('all_countries'))
        if country not in countries_dict:
            countries_dict[country] = 1
        else:
            countries_dict[country] += 1
        self.myRedis.set('all_countries', json.dumps(countries_dict))

    def get_ip_record(self, ip):
        decoded_ip_data = literal_eval(self.myRedis.get(ip).decode('utf-8'))
        return decoded_ip_data

    def get_all_data(self):
        for key in self.myRedis.scan_iter():
            print(key, self.myRedis.get(key))

    def get_ips_by_country(self, country, start, end):
        country_ips = []
        for ip in self.myRedis.scan_iter():

            if ip == b'all_countries':
                continue

            ip_country = self.get_ip_record(ip)['country_name']
            ip_time = str_2_date(self.get_ip_record(ip)['time'])

            if ip_country == country:
                if start == None and end == None:
                    country_ips.append(ip)
                elif start == None and end != None:
                    if ip_time <= end:
                        country_ips.append(ip)
                elif start != None and end == None:
                    if ip_time >= start:
                        country_ips.append(ip)
                else:
                    if ip_time >= start and ip_time <= end:
                        country_ips.append(ip)

        return country_ips

    def get_5_top_countries(self):
        index = 0
        countries_dict = json.loads(self.myRedis.get('all_countries'))
        top_countries = []

        while index < 5 and countries_dict != {}:
            # the country whose value is the largest
            max_country = max(countries_dict, key=lambda k: countries_dict[k])
            top_countries.append(max_country)
            del countries_dict[max_country]
            index += 1

        return top_countries

def create_redis():
    return MyRedis(host = "localhost", port = 6379)