"""
 _____   _______   __     ______      __    __   
/__  /  / ____/ | / /    /_  __/___ _/ /_  / /__ 
  / /  / __/ /  |/ /      / / / __ `/ __ \/ / _ \
 / /__/ /___/ /|  /      / / / /_/ / /_/ / /  __/
/____/_____/_/ |_/      /_/  \__,_/_.___/_/\___/ 
                                                 

FILE:     ZenGraphics.py
CHANGED:  26.03.2020

Fachhochschule Südwestfalen
Mechatronik/Mikrocomputer
Prof. Dr.-Ing. Tobias Ellermeyer

"""
# Dies ist hoffentlich nur im Testing-Branch zu sehen ...

import pygame	# for graphics, see pygame.org
import numpy as np
from time import sleep

class ZenTable:
	def __init__(self):
		self.pos_x = 0
		self.pos_y = 0

		self.size_x = 800
		self.size_y = 800	
		self.scaling = 10	# Scaling x/y to screen scaling=20 -> x=200 -> screen 10
		self.offset_x = 10
		self.offset_y = 10	
		self.delay = 0.005	# Delay per movement
		pygame.init()		# init graphics
		pygame.display.set_caption("Zen Table Simulator")	# Set window title
		self.screen = pygame.display.set_mode((self.size_x,self.size_y))		# generate screen in window

		self.DesertSand = pygame.Color(237,201,175)
		self.PenColor = pygame.Color(255,255,0)
		self.BallColor = pygame.Color(200,200,200)
		self.WallColor = pygame.Color(200,200,0)
    
	def clear(self):
		self.screen.fill(self.DesertSand)	# clear screen
		self.pos_x = 0
		self.pos_y = 0

		# Draw Ball
		pygame.draw.circle(self.screen,self.BallColor,[self.pos_x+self.offset_x,self.size_y-(self.pos_y+self.offset_y)],8)

		pygame.display.update()

	# Bresenham Line Algorhytmus
	def moveto(self,x,y):
		x = x // self.scaling
		y = y // self.scaling
		
		
		dx = abs(x-self.pos_x)
		dy = abs(y-self.pos_y)
		# Vorzeichen berechnen
		sx = np.sign(x-self.pos_x)
		sy = np.sign(y-self.pos_y)

		#print("   --> MoveTo x=",x," y=",y," / dx= ",dx," dy=",dy," sx=",sx," sy=",sy)

		runloop = True

		# Fehlerterm (Bresenham)

		if (dx > dy):
			df = dx//2
		else:
			df = dy//2 

		# Distanz/Anzahl Schritte
		if (dx>dy):
			dist = dx
		else:
			dist = dy

		cnt = 0
		

		while runloop:
			# Remove Ball
			pygame.draw.circle(self.screen,self.PenColor,[self.pos_x+self.offset_x,self.size_y-(self.pos_y+self.offset_y)],8)

			cnt=cnt+1

			ssx = 0
			ssy = 0
			df2 = df
			if (df2 >-dx):
				df = df - dy
				self.pos_x = self.pos_x + sx
				ssx = sx
			else:
				ssx = 0
			if (df2 < dy):
				df = df + dx
				self.pos_y = self.pos_y + sy
				ssy = sy
			else:
				ssy=0

#			print("x=",pos_x," y=",pos_y)
			pygame.draw.circle(self.screen,self.BallColor,[self.pos_x+self.offset_x,self.size_y-(self.pos_y+self.offset_y)],8)
			pygame.display.update()
			sleep(self.delay)
			if  ( (self.pos_x>=x) & (self.pos_y>=y) ): 
				runloop = False 
