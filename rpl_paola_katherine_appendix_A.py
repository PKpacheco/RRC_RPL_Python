#!/bin/python3

'''
RPL - Python Essentials - DSML
Paola Katherine Cardoso
Python - term 2 - 2023
Appendix A - Winnipeg Transit
RRC
'''

import json
import requests
from datetime import datetime, timedelta


# # #check connectivity
# url_stops = f"https://api.winnipegtransit.com/v3/stops.json?lon={long}&lat={lat}&distance={distance}&api-key={API_KEY}"
# response = requests.get(url_stops)
# print(response)

# API_KEY = "wX6qfnO8Yuxb4jkkJJRP"
# url_test = f"https://api.winnipegtransit.com/v3/stops/10064/schedule?api-key={API_KEY}"
# response = requests.get(url_test)
# if response.status_code == 200:
#     print(response.json())
# else:
#     print("Error from server: " + str(response.content))




class BusWinnipeg():

    def __init__(self):
        self.api_key = "wX6qfnO8Yuxb4jkkJJRP"
        self.url_base = f"https://api.winnipegtransit.com/v3/"
        self.start = self.transform_date_start()
        self.end = self.transform_date_end()
        
    def transform_date_start(self):
        start_no_format = datetime.now()
        start = start_no_format.strftime('%Y-%m-%d{}%H:%M:%S').format("T")
        return start
    
    def transform_date_end(self):
        end_no_format = datetime.now() + timedelta(minutes=5)
        end = end_no_format.strftime('%Y-%m-%d{}%H:%M:%S').format("T")
        return  end

# result:  key    name ( ex: 123  Portage Av) limit 5
    def fetch_stops(self, 
                    long, 
                    lat,
                    distance
                    ):
        api_stop = "stops.json?lon={}&lat={}&distance={}&api-key={}".format(long, lat, distance, self.api_key)
        url_stop = self.url_base+ api_stop
        request_stop = requests.get(url_stop)
        json_stop = json.loads(request_stop.text)
        print (json_stop)

# result:  
    def fetch_schedule(self,
                       bus_stop, 
                       ):
        api_schedule = "stops/{}/schedule?start={}&end={}&api-key={}".format(bus_stop,self.start, self.end, self.api_key)
        url_schedule = self.url_base + api_schedule
        print(url_schedule)
        request_schedule = requests.get(url_schedule)
        import ipdb;ipdb.set_trace()
        # schedule_json = json.loads(request_schedule.text)
        print (request_schedule)


if __name__ == "__main__":

    option_user = int(input("Press 1 for stops available, Press 2 for Schedule  "))
    bw = BusWinnipeg()

    if option_user == 1:
        long = input("Enter the longitude: (example : -97.138)" )
        lat = input("Enter the latitude: ( example(49.895)")
        distance = input("Enter the distance: (example: 100, 200, 250)")
        bw.fetch_stops (long, lat, distance)
    elif option_user == 2:
        bus_stop = input("Enter the  stop number:")
        bw.fetch_schedule(bus_stop)
    else:
        print("Please enter a valid number")


    