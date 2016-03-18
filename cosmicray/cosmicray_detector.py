# To do: make sure the NOR hits take precedence over hits from tube1 
# and tube2 which will occur at the same time.

import Adafruit_BBIO.GPIO as GPIO
import time

GeigerTube1 = "P9_41"
GeigerTube2 = "P9_42"
NOR = "P9_12"

GPIO.setup(GeigerTube1, GPIO.IN)
GPIO.setup(GeigerTube2, GPIO.IN)
GPIO.setup(NOR, GPIO.IN)

Tube1Hits = 0
Tube2Hits = 0
ZenithHits = 0

# Need to have an argument inside the parantheses even if it isnt used
def recordEvent1(pin):
	global Tube1Hits
	print "Recording event on tube 1"
	Tube1Hits += 1

def recordEvent2(pin):
	global Tube2Hits
	print "Recording event on tube 2"
	Tube2Hits += 1

def recordZenithEvent(pin):
	global ZenithHits
	print "Cosmic Ray!"
	ZenithHits += 1

GPIO.add_event_detect(GeigerTube1, GPIO.FALLING, callback=recordEvent1)
GPIO.add_event_detect(GeigerTube2, GPIO.FALLING, callback=recordEvent2)
GPIO.add_event_detect(NOR, GPIO.FALLING, callback=recordZenithEvent)

# Set up the .mat file we're going to write the counts to, by hour,
# for processing and graphing by an accompanying octave script:
todaysFileName = time.strftime("%Y%m%d") + ".mat"
currentHour = time.localtime().tm_hour
today = time.localtime().tm_mday

while True:
	time.sleep(1)
	if time.localtime().tm_mday is not today:
		with open(todaysFileName, 'a') as file:
                        file.write(str(ZenithHits) + '\n')
                        file.close()
                Tube1Hits = 0
                Tube2Hits = 0
                ZenithHits = 0
                currentHour = time.localtime().tm_hour
		today = time.localtime().tm_mday

	if time.localtime().tm_hour is not currentHour:
		with open(todaysFileName, 'a') as file:
			file.write(str(ZenithHits) + '\n')
			file.close()
		Tube1Hits = 0
		Tube2Hits = 0
		ZenithHits = 0
		currentHour = time.localtime().tm_hour
		
