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

print(header)

print("\033[1;33;40m" +20*"*" +3*"/" +20*"*" +3*"/" +20*"*" +3*"/" +20*"*" +"\n" + "\033[0;0m")

print("[*] Tool - GeoOccupy: A geolocation finder tool via CLI\n" +
    "[*] Lang&Version - Python3\n" + "[*] Creation Date - May 8 2021 \n" +
    "[*] Please report any incorrect results at kumaratuljaiswal222@gmail.com\n")

print("\033[1;33;40m" +20*"*" +3*"/" +20*"*" +3*"/" +20*"*" +3*"/" +20*"*" +"\n" + "\033[0;0m")

import socket
import pygeoip
import argparse

db1 = pygeoip.GeoIP('GeoIPASNum.dat')
db2 = pygeoip.GeoIP('GeoLiteCity.dat')

def printRecord(ip, given_args):

    data = db2.record_by_name(ip) 

    if data != None:
        country = data['country_name']
        city = data['city']
        continentName = data['continent']
        countrycode = data['country_code']
        postalcode = data['postal_code']
        timezone = data['time_zone']
        metrocode= data['metro_code']
        latitude = data['latitude']
        longitude = data['longitude']
        dma = data['dma_code'] 

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
            print("[**] ASN: " +str(db1.org_by_name(ip)))

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

    else:
        print("[**] Sorry, I can't locate that in my database")


def main():
    parser = argparse.ArgumentParser(description='GeoOccupy is command line argument tool. GeoOccupy means geolocation finder, '+ 
        'which is used to find country, city, continent, country code, postal, time-zone via IP or Host. '+ 
        '\n', prog='python3 geooccupy.py',  usage='%(prog)s [options]')

    parser.add_argument('-ip', action = 'store', dest='ip', help='IP or Host name that you want to extract info', required=True)
    parser.add_argument('-c', action = 'store_true', dest='country', help='Find country name')
    parser.add_argument('-cit', action = 'store_true', dest='city', help='Find city name' )
    parser.add_argument('-con', action = 'store_true', dest='continent', help='Find continent')
    parser.add_argument('-code', action = 'store_true', dest='code', help='Find country code')
    parser.add_argument('-postal', action = 'store_true', dest='postal', help='Find postal code')
    parser.add_argument('-asn', action = 'store_true', dest='asn', help='Find ASN number (Autonomous System Number)')
    parser.add_argument('-zone', action = 'store_true', dest='zone', help='Find time-zone')
    parser.add_argument('-metro', action = 'store_true', dest='metro', help='Find metro code')
    parser.add_argument('-lat', action = 'store_true', dest='latitude', help='Find latitude')
    parser.add_argument('-long', action = 'store_true', dest='longitude', help='Find longitude')
    parser.add_argument('-dma', action = 'store_true', dest='dma', help='Find DMA code (Designated Market Area)')
    
    given_args = parser.parse_args()

    try:
        ip = socket.gethostbyname(given_args.ip)
    except socket.gaierror:
        print('Invalid IP or Host')
        exit(0)

    print("[**] The IP that is resolved: " +ip)
    printRecord(str(ip), given_args)  



main()