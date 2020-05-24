#ISS Overhead Python v0.1.6

#import RPi.GPIO
import urllib2, json, threading, os, datetime, time
from pygeocoder import Geocoder
#url1 = "http://api.open-notify.org/iss-pass.json?lat={0}&long={0}
url1 = "http://api.open-notify.org/iss-pass.json?lat=36.2645800&lon=-94.4640950&alt=387.08&n=1";
url2 = "https://api.wheretheiss.at/v1/satellites/25544";
url3 = "http://api.open-notify.org/astros.json";


risetime = 0;
time = 0;
duration = 0;
latitude = 0;
longitude = 0;
number = 0;
address = "";
overhead = 0;
altitude = 0;
location  = "";
locationlat = 0;
locationlong = 0;




        
def work():
	global overhead;
	global altitude;
	global latitude;
	global longitude;
	global number;
	global location;
	global time;
	
	
	r1 = urllib2.urlopen(url1);
	r2 = urllib2.urlopen(url2);
	r3 = urllib2.urlopen(url3);
	
	d1 = json.loads(r1.read());
	d2 = json.loads(r2.read());
	d3 = json.loads(r3.read());

	#risetime = d1['response'][0]['risetime'];
        #duration = d1['response'][0]['duration'];
	latitude = d2.get('latitude');
	longitude = d2.get('longitude');
	altitude = d2.get('altitude');
	number = d3.get('number');
	time = datetime.datetime.now().strftime('%m-%d-%y %H:%M:%S');
	#overhead = datetime.datetime.fromtimestamp(risetime).strftime('%m-%d-%y %H:%M:%S');
	#duration = duration/60;
	#location = Geocoder.reverse_geocode(latitude, longitude);
	try:
		location = Geocoder.reverse_geocode(latitude, longitude);
	except:
		pass;
		location = "The Ocean, Probably";
		
	printresults();
	threading.Timer(5, work).start();
	
def printresults():
	os.system('cls');
	print " ";
	print time," ","GMT";
	print " ";
	print "The International Space Station Tracking Information...";
	print "Latitude=",latitude;
	print "Longitude=",longitude;
	print "Altitude=",altitude,"Kilometers";
	print " ";
	print "The ISS is currently over ", location;
	'''print " ";
	print "The ISS will next pass overhead of your current location at";
	print overhead, " ","GMT";
	print "and will be in the sky for ",duration," ","Minutes";
	print " ";'''
	print "There are currently ",number," ","people abord the ISS"; 
work();
	
	
	
	
	
	
	
	
	
	
	
	
