import Adafruit_BBIO.GPIO as GPIO
import time

GeigerTube1 = "P9_41"
GeigerTube2 = "P9_42"
NAND = "P9_43"

GPIO.setup(GeigerTube1, GPIO.IN)
GPIO.setup(GeigerTube2, GPIO.IN)
GPIO.setup(NAND, GPIO.IN)

Tube1Hits = 0
Tube2Hits = 0
ZenithHits = 0

def recordEvent(tube):
	global Tube1Hits, Tube2Hits
	print "Recording event on " + tube + "\n"
	if tube == 1:
		Tube1Hits += 1
	elif tube == 2:
		Tube2Hits += 1
	else:
		ZenithHits += 1

GPIO.add_event_detect(GeigerTube1, GPIO.FALLING, callback=recordEvent)
GPIO.add_event_detect(GeigerTube2, GPIO.FALLING, callback=recordEvent)
GPIO.add_event_detect(NAND, GPIO.FALLING, callback=recordEvent)
print "Program finished.\n"
