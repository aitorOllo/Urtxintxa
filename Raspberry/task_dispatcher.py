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

SPRINKLER1 = 0x01
SPRINKLER2 = 0x02
LIGHT = 0x03

def sendCommand(device):

	if device == SPRINKLER1:
		print "Send ON command to Arduino"
		time.sleep(10)
		print "Send OFF command to Arduino"
	elif device == SPRINKLER2:
		print "Send ON command to Arduino"
		time.sleep(10)
		print "Send OFF command to Arduino"
	elif device == LIGHT:
		print "Ask Arduino if it is night"
		isNight = False
		if isNight:
			print "Send ON command to Arduino"
		else:
			print "Send OFF command to Arduino"

if __name__ == '__main__':

	#Initialize timers
	timerOwl = threading.Timer(0,0)
	timerSprinkler1 = threading.Timer(0,0)
	timerSprinkler2 = threading.Timer(0,0)
	timerLight = threading.Timer(10*60, sendCommand, [LIGHT])
	#Main infinite loop
	while True:
		if not timerOwl.isAlive():
			print ("Starting sound")
			timerOwl = threading.Timer(3, player.reproduceSound,["owl1.wav"])
			timerOwl.start()
		if not timerSprinkler1.isAlive():
			print ("Starting sprinkler 1")
			timerSprinkler1 = threading.Timer(25, sendCommand, [SPRINKLER1])
			timerSprinkler1.start()
		if not timerSprinkler2.isAlive():
			print ("Starting sprinkler 2")
			timerSprinkler2 = threading.Timer(5, sendCommand, [SPRINKLER2])
			timerSprinkler2.start()
		if not timerLight.isAlive:
			timerLight.start()
