#! usr/bin/python

#*******************************************************#
#							#
# Module that reproduces sounds				#
#							#
# Aitor							#
#							#
#*******************************************************#

#Import modules
import pygame
import threading
import time
from random import randint

def reproduceSound(fileName):
	print "Reproducing file: ", fileName
	pygame.mixer.init()
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.load("/home/pi/Projects/Urtxintxa/Audios/"+fileName)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue # Wait until playing is finished
	time.sleep(randint(45,65)*60)
	return
