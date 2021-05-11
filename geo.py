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

   


print("[*] Tool - GeoOccupy: A geolocation finder tool via CLI\n" + "[*] Lang&Version - Python3\n" + "[*] Creation Date - May 8 2021 \n" + "[*] Please report any incorrect results at kumaratuljaiswal.in@gmail.com\n")


print("\033[1;33;40m" +20*"*" +3*"/" +20*"*" +3*"/" +20*"*" +3*"/" +20*"*" +"\n" + "\033[0;0m")

import socket
import pygeoip
import argparse
from colorama import Fore, Back, Style
import sys

db1 = pygeoip.GeoIP('GeoIPASNum.dat')
db2 = pygeoip.GeoIP('GeoLiteCity.dat')
def printRecord(ip):
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

        
        print("[**] Country: " +str(country))
        print("[**] City: " +str(city))
        print("[**] Continent: " +str(continentName))
        print("[**] Code: " +str(countrycode))
        print("[**] Postal: " +str(postalcode))  
        print("[**] ASN: " +str(database1))
        print("[**] Zone: " +str(timezone))
        print("[**] Metro: " +str(metrocode))
        print("[**] Latitude: " +str(latitude))
        print("[**] Longitude: " +str(longitude))
        print("[**] DMA: " +str(dma))

    except socket.gaierror:
        pass 


def main():
    parser = argparse.ArgumentParser(description='GeoOccupy is command line argument tool. GeoOccupy means geolocation finder, which is used to find country, city, continent, country code, postal, time-zone via IP or Host. \n', prog='python3 geo2.py -ip=$IP or $HOST -c= -cit= -con= -code=  -postal= -asn= -zone= -metro= -latitude= -longitude= -dma=',  usage='%(prog)s [options]')
    parser.add_argument('-ip', action = 'store', dest='ip', help='IP or Host name that you want to extract info', required=True)
    parser.add_argument('-c', action = 'store', dest='country', help='Find country name')#, required=True)
    parser.add_argument('-cit', action = 'store', dest='city', help='Find city name' )#, required=True)
    parser.add_argument('-con', action = 'store', dest='continent', help='Find continent')#, required=True)
    parser.add_argument('-code', action = 'store', dest='code', help='Find country code')#, required=True)
    parser.add_argument('-postal', action = 'store', dest='postal', help='Find postal code')#, required=True)
    parser.add_argument('-asn', action = 'store', dest='asn', help='Find ASN number')#, required=True)
    parser.add_argument('-zone', action = 'store', dest='zone', help='Find time-zone')#, required=True)
    parser.add_argument('-metro', action = 'store', dest='metro', help='Find metro code')#, required=True)
    parser.add_argument('-latitude', action = 'store', dest='latitude', help='Find latitude')
    parser.add_argument('-longitude', action = 'store', dest='longitude', help='Find longitude')
    parser.add_argument('-dma', action = 'store', dest='dma', help='Find DMA code')
    
    given_args = parser.parse_args()
    
    host1 = given_args.ip
    host2 = given_args.country
    host3 = given_args.city
    host4 = given_args.continent
    host5 = given_args.code
    host6 = given_args.postal
    host7 = given_args.asn
    host8 = given_args.zone
    host9 = given_args.metro
    host10 = given_args.latitude
    host11 = given_args.longitude
    host12 = given_args.dma


    if (host1 == None) or (host2 == None) or (host3 == None) or (host4 == None) or (host5 == None) or (host6 == None) or (host7 == None) or (host8 == None)  or (host9 == None) or (host10 == None) or (host11 == None) or (host12 == None):
        print(parser.usage)
        exit(0)
    else:  
        ip = socket.gethostbyname(host1)    #host2
        #print("[***] ASN: " +str(ip))
        print("[**] The IP that is resolved: " +ip)
        printRecord(str(ip))  



main()

