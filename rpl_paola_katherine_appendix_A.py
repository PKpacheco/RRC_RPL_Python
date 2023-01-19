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
        end_no_format = datetime.now() + timedelta(minutes=30)
        end = end_no_format.strftime('%Y-%m-%d{}%H:%M:%S').format("T")
        return  end

    def fetch_stops(self, 
                    long, 
                    lat,
                    distance
                    ):
        api_stop = "stops.json?lon={}&lat={}&distance={}&api-key={}".format(long, lat, distance, self.api_key)
        url_stop = self.url_base+ api_stop
        request_stop = requests.get(url_stop)
        json_stop = json.loads(request_stop.text)

        print("Stops available", distance,"from the coodinates (",lat, long,"):" )
        for i in json_stop['stops']:
            print(i['key'], '  ', i['name'])

# result: scheduled and estimated   
    def fetch_schedule(self,
                       bus_stop, 
                       ):
        api_schedule = "stops/{}/schedule.json?start={}&end={}&api-key={}".format(bus_stop,self.start, self.end, self.api_key)
        url_schedule = self.url_base + api_schedule
        request_schedule = requests.get(url_schedule)
        schedule_json = json.loads(request_schedule.text)
        item_list = ['scheduled', 'estimated'] 
        import ipdb;ipdb.set_trace()
        for i in schedule_json['stop-schedule']:
            print(i['scheduled'], '  ', i['estimated'])


if __name__ == "__main__":

    option_user = int(input("Press 1 for stops available, Press 2 for Schedule  "))
    
    bw = BusWinnipeg()

    if option_user == 1:
        lat_long_input = int(input("Press 1 for random coordinates, Press 2 for input the coordinates "))
        if lat_long_input == 1:
            long = 49.895
            lat = -97.138
            distance = 200

        elif lat_long_input == 2:
            long = input("Enter the longitude: (example : -97.138)" )
            lat = input("Enter the latitude: ( example(49.895)")
            distance = input("Enter the distance: (example: 100, 200, 250)")

        else:
            print('Please enter a valid number')
        bw.fetch_stops (long, lat, distance)

    elif option_user == 2:
        bus_stop = input("Enter the  stop number:")
        bw.fetch_schedule(bus_stop)

    else:
        print("Please enter a valid number")
