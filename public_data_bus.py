# from https://www.youtube.com/watch?v=RrPZza_vZ3w
# CTA unofficial API

import urllib
from xml.etree.ElementTree import parse
from geopy.distance import great_circle # pip install --user geopy # in terminal
import time

def monitor():
    dave_lat = 41.880262 # lat > 41.xx is northbound, was 41.980262 originally
    dave_long = -87.668452
    
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    
    data = u.read()
    
    f = open('rt22.xml','wb')
    f.write(data)
    f.close()

    doc = parse('rt22.xml')
    
    office_loc = (dave_lat,dave_long)
    
    for bus in doc.findall('bus'):
        dn = bus.findtext('dn')
        lat = float(bus.findtext('lat'))
        lon = float(bus.findtext('lon'))
        bus_id = int(bus.findtext('id'))
        if lat > dave_lat:
            if dn.startswith('N'):
                bus_loc = (lat,lon)
                dist = great_circle(office_loc,bus_loc).miles
                print bus_id, dist

while True:
    monitor()
    time.sleep(5)



''' 
tasks
1)
 parse downloaded data for vehicles traveling north of Dave's office
 Dave's office: lat 41.980262 , long -87.668452
2)
 periodically monitor identified buses and report distance from office
 when bus gets within .5 miles, issue alert by popping up web page with bus location on map
'''

''' 
# parsing document into tree

from xml.etree.ElementTree import parse
doc = parse('rt22.xml')

# iterate over specific element type

for bus in doc.findall('bus'):
    ...

# extracting data elem.findtext()

for bus in doc.findall('bus'):
    d = bus.findtext('d')
    lat = float(bus.findtext('lat'))
    
    
display map: 
Google Static Maps

import webbrowser
 webbrowser.open ('http://...')   

'''