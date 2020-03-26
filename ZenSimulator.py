"""
 _____   _______   __     ______      __    __   
/__  /  / ____/ | / /    /_  __/___ _/ /_  / /__ 
  / /  / __/ /  |/ /      / / / __ `/ __ \/ / _ \
 / /__/ /___/ /|  /      / / / /_/ / /_/ / /  __/
/____/_____/_/ |_/      /_/  \__,_/_.___/_/\___/ 
                                                 

FILE:     ZenSimulator.py
CHANGED:  26.03.2020

Fachhochschule Südwestfalen
Mechatronik/Mikrocomputer
Prof. Dr.-Ing. Tobias Ellermeyer

"""

#import serial   # for serial/bluetooth communication

import pygame	# for graphics, see pygame.org
import ZenGraphics

from time import sleep

SerialPort = "COM8"		


running = True
cnt = 0


# New Zen Graphics Object
zg = ZenGraphics.ZenTable()
zg.clear()


while running:
	# event handling, gets all event from the event queue
	for event in pygame.event.get():
		# only do something if the event is of type QUIT
		if event.type == pygame.QUIT:
			# change the value to False, to exit the main loop
			running = False

	# test drawings
	if (cnt==0):
		zg.moveto(1000,1400)
		cnt = 1
	if (cnt==1):
		zg.moveto(4000,700)
		cnt = 2
	if (cnt==2):
		zg.moveto(5000,3000)
		cnt = 3