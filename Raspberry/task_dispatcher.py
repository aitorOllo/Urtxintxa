#! /usr/bin/python

#*******************************************************#
#							#
# Urtxintxa project					#
#							#
# Task dispatcher for Urtxintxa project:		#
# Executes different actions each random time		#
#							#
# Aitor							#
#							#
#*******************************************************#

# Import modules
import soundPlayer as player
import threading
import time
import serial
from random import randint

SPRINKLER1 = 0x01
SPRINKLER2 = 0x02
LIGHT = 0x03

isNight = False

def sendCommand(arduino,device):

	if device == SPRINKLER1:
		print "Send ON command to Arduino"
		arduino.write('a')
		time.sleep(10)
		print "Send OFF command to Arduino"
		arduino.write('b')
	elif device == SPRINKLER2:
		print "Send ON command to Arduino"
		arduino.write('c')
		time.sleep(10)
		print "Send OFF command to Arduino"
		arduino.write('d')
	elif device == LIGHT:
		print "Ask Arduino if it is night"
		arduino.write('e')
		time.sleep(0.1)
		global isNight
		readValue = ''
		while arduino.inWaiting() > 0:
			readValue = arduino.read(1)
			print ("Read from arduino: {0}".format(readValue))
		if readValue =='z':
			isNight = True
			print "Send ON command to Arduino"
			arduino.write('f')
		elif readValue  == 'y':
			isNight = False
			print "Send OFF command to Arduino"
			arduino.write('g')

if __name__ == '__main__':
	#Open serial connection
	arduino = serial.Serial('/dev/ttyACM0', 9600)
	#Initialize timers
	timerOwl = threading.Timer(0,0)
	timerSprinkler1 = threading.Timer(0,0)
	timerSprinkler2 = threading.Timer(0,0)
	timerLight = threading.Timer(0,0)
	#Main infinite loop
	while True:
		if (not timerOwl.isAlive()) and (isNight):
			print ("Starting sound")
			timerOwl = threading.Timer(0, player.reproduceSound,["owl1.wav"])
			timerOwl.start()
		if not timerSprinkler1.isAlive():
			print ("Starting sprinkler 1")
			if isNight:
				timerSprinkler1 = threading.Timer(randint(15,20)*60, sendCommand, [arduino, SPRINKLER1])
			else:
				timerSprinkler1 = threading.Timer(randint(55,65)*60, sendCommand, [arduino, SPRINKLER1])
			timerSprinkler1.start()
		if not timerSprinkler2.isAlive():
			print ("Starting sprinkler 2")
			if isNight:
				timerSprinkler2 = threading.Timer(randint(15,20)*60, sendCommand, [arduino, SPRINKLER2])
			else:
				timerSprinkler2 = threading.Timer(randint(55,65)*60, sendCommand, [arduino, SPRINKLER2])
			timerSprinkler2.start()
		if not timerLight.isAlive():
			print ("Starting Light")
			timerLight = threading.Timer(10, sendCommand, [arduino, LIGHT])
			timerLight.start()
	arduino.close();
