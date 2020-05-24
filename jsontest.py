from pygeocoder import Geocoder
import urllib2, json, threading, os, datetime, time
url = "http://api.open-notify.org/astros.json";

location = ""
currentlocation = ""
astros = 0

def work():
    global astros
    global currentlocation
    global location

    r1 = urllib2.urlopen(url);
    d1 = json.loads(r1.read());

    astros = d1.get('number');

    location = raw_input('What is your current location? (City,ST) ')

    currentlocation = Geocoder.geocode(location)
    printresults();
def printresults():
    os.system('cls');
    print currentlocation[0].coordinates;
    print 'There are currently ',astros, 'people in space';
    time.sleep(5);
work();
