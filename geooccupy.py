#!/usr/bin/python
header= """
  ______                        ______                                                    
 /      \                      /      \                                (@hackingtruthin)                                               
/$$$$$$  |  ______    ______  /$$$$$$  |  _______   _______  __    __   ______   __    __ 
$$ | _$$/  /      \  /      \ $$ |  $$ | /       | /       |/  |  /  | /      \ /  |  /  |
$$ |/    |/$$$$$$  |/$$$$$$  |$$ |  $$ |/$$$$$$$/ /$$$$$$$/ $$ |  $$ |/$$$$$$  |$$ |  $$ |
$$ |$$$$ |$$    $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |
$$ \__$$ |$$$$$$$$/ $$ \__$$ |$$ \__$$ |$$ \_____ $$ \_____ $$ \__$$ |$$ |__$$ |$$ \__$$ |
$$    $$/ $$       |$$    $$/ $$    $$/ $$       |$$       |$$    $$/ $$    $$/ $$    $$ |
 $$$$$$/   $$$$$$$/  $$$$$$/   $$$$$$/   $$$$$$$/  $$$$$$$/  $$$$$$/  $$$$$$$/   $$$$$$$ |
                                                                      $$ |      /  \__$$ |
                                                                      $$ |      $$    $$/ 
                                by KumarAtulJaiswal (@whoiskumaratul) $$/        $$$$$$/  
"""
# try:
#     print(header + "                   by KumarAtulJaiswal (@whoiskumaratul)\n")
# except:
#     print(header + "                           by @hackingtruthin\n")    

try:
    print(header)
except:
    print(header) 
    

print("\033[1;33;40m" +20*"*" +3*"/" +20*"*" +3*"/" +20*"*" +3*"/" +20*"*" +"\n" + "\033[0;0m")

   


print("[*] Tool - GeoOccupy: A geolocation finder tool via CLI\n" + "[*] Lang&Version - Python3\n" + "[*] Creation Date - May 8 2021 \n" + "[*] Please report any incorrect results at kumaratuljaiswal222@gmail.com\n")


print("\033[1;33;40m" +20*"*" +3*"/" +20*"*" +3*"/" +20*"*" +3*"/" +20*"*" +"\n" + "\033[0;0m")

import socket
import pygeoip
import argparse
from colorama import Fore, Back, Style
import sys

db1 = pygeoip.GeoIP('GeoIPASNum.dat')
db2 = pygeoip.GeoIP('GeoLiteCity.dat')

def printRecord(ip, given_args):
    try:
        database1 = db1.org_by_name(ip)
        database2 = db2.record_by_name(ip)
    except:
        print("[**] Sorry, I can't locate that in my database")    

    try:
        country = database2['country_name']
        city = database2['city']
        continentName = database2['continent']
        countrycode = database2['country_code']
        postalcode = database2['postal_code']
        timezone = database2['time_zone']
        metrocode= database2['metro_code']
        latitude = database2['latitude']
        longitude = database2['longitude']
        dma = database2['dma_code'] 

        if given_args.country:
            print("[**] Country: " +str(country))

        if given_args.city:
            print("[**] City: " +str(city))

        if given_args.continent:
            print("[**] Continent: " +str(continentName))

        if given_args.code:
            print("[**] Code: " +str(countrycode))

        if given_args.postal:
            print("[**] Postal: " +str(postalcode))

        if given_args.asn:
            print("[**] ASN: " +str(database1))

        if given_args.zone:
            print("[**] Zone: " +str(timezone))

        if given_args.metro:
            print("[**] Metro: " +str(metrocode))

        if given_args.latitude:
            print("[**] Latitude: " +str(latitude))

        if given_args.longitude:
            print("[**] Longitude: " +str(longitude))

        if given_args.dma:
            print("[**] DMA: " +str(dma))

    except socket.gaierror:
        pass 


def main():
    parser = argparse.ArgumentParser(description='GeoOccupy is command line argument tool. GeoOccupy means geolocation finder, which is used to find country, city, continent, country code, postal, time-zone via IP or Host. \n', prog='python3 geooccupy.py',  usage='%(prog)s [options]')
    parser.add_argument('-ip', action = 'store', dest='ip', help='IP or Host name that you want to extract info', required=True)
    parser.add_argument('-c', action = 'store_true', dest='country', help='Find country name')#, required=True)
    parser.add_argument('-cit', action = 'store_true', dest='city', help='Find city name' )#, required=True)
    parser.add_argument('-con', action = 'store_true', dest='continent', help='Find continent')#, required=True)
    parser.add_argument('-code', action = 'store_true', dest='code', help='Find country code')#, required=True)
    parser.add_argument('-postal', action = 'store_true', dest='postal', help='Find postal code')#, required=True)
    parser.add_argument('-asn', action = 'store_true', dest='asn', help='Find ASN number (Autonomous System Number)')#, required=True)
    parser.add_argument('-zone', action = 'store_true', dest='zone', help='Find time-zone')#, required=True)
    parser.add_argument('-metro', action = 'store_true', dest='metro', help='Find metro code')#, required=True)
    parser.add_argument('-lat', action = 'store_true', dest='latitude', help='Find latitude')
    parser.add_argument('-long', action = 'store_true', dest='longitude', help='Find longitude')
    parser.add_argument('-dma', action = 'store_true', dest='dma', help='Find DMA code (Designated Market Area)')
    
    given_args = parser.parse_args()
    
 
    ip = socket.gethostbyname(given_args.ip)   
    print("[**] The IP that is resolved: " +ip)
    printRecord(str(ip), given_args)  



main()

