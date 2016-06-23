"""
Eugene Hochenedel
ADGP-120
"""

import pygame
import AStar
import Nodes
import math
import pygame.locals
import random
from AStar import *
from Nodes import *
from pygame.locals import *
'''
from os import *
from math import *
from random import *
from pygame import *
'''

#Color	#(R,G,B)
Red = (255, 0, 0)
Orange = (255, 165, 0)
Yellow = (255, 255, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Indigo = (75, 0, 130)
Violet = (238, 130, 238)
Black = (0, 0, 0)
White = (255, 255, 255)
Grey = (128, 128, 128)
Teal =(0,128,128)

class Game:
	def __init__(self):
		#os.environ['SDL_VIDEO_CENTERED'] = '1'
		#path = os.path.dirname(os.path.realpath("__file__"))
		pygame.init()
		pygame.font.init()
		
		self.search_space = {}
		self.mouse_listeners = []
		
		#Used to give each cell an independent numeric value
		id = 0
		
		#Determines the number of rows and columns
		self.XROW = 20
		self.YCOL = 50
		#Determines the size of the game window
		self.WIDTH = 30
		self.HEIGHT = 30
		
		for x in range(self.YCOL):
			for y in range(self.XROW):
				
				n = Points(x, y, id)
					
				xWall = True if y % self.XROW == 0 or y % self.XROW == self.XROW - 1 else False
				yWall = True if x % self.YCOL == 0 or x % self.YCOL == self.YCOL - 1 else False
				
				if(xWall or yWall):
					n.traverse = False
					n.Colors
					
				self.mouse_listeners.append(n.onClick)
				
				self.search_space[id] = n
				id+=1
		
		
		#mod = 15
		for i in range(50 * 2):
			rng = random.randint(0,(self.XROW-1) * (self.YCOL-1))
			self.search_space[rng].traverse = False
			self.search_space[rng].Colors
			
			
			
		pad = (5,5)
		screen_width = self.YCOL * (pad[0] + self.WIDTH) + pad[1]
		screen_height = self.XROW * (pad[0] + self.HEIGHT) + pad[1]
		
		
		self.screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
		
		self.font1 = pygame.font.Font(None, 14)
		self.font2 = pygame.font.Font(None, 28)
		
		pygame.display.set_caption("ADGP-120 AStar")
		
		self.Running = True
		self.Paused = False
		self.start = None
		self.init = False
		self.goal = None
		self.defense = None
		self.algo = None
		self.gen = None
		self.delay = 50
		
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill(Black)
		
	#def reset_color(self):
	#	for i in self.search_space:
	#		if self.search_space[i].traverse:
	#			self.search_space[i].Colors
	#		else:
	#			self.search_space[i].Colors
	

	
	def run(self):
		debug = False
		while self.Running:
			events = pygame.event.get()
			for event in events:
				if event.type==VIDEORESIZE:
					self.screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
					pygame.display.flip()
				if event.type == pygame.MOUSEBUTTONDOWN:
					for callback in self.mouse_listeners:
						cb = callback(pygame.mouse.get_pos())
						if cb:
							if cb:
								if event.button == 1:
									if(not self.Paused):
										#self.reset_color()
										init = False
										if self.algo:
											self.algo.Reset()
											self.gen = None
											
										if not cb.marked:
											print("set start")
											self.start = cb
									
								elif event.button == 2 or event.button == 4 or event.button == 5:
									if(not self.Paused):
										self.init = True
										self.defense = cb
										cb.traverse = not cb.traverse
										self.defense.Colors
										
									else:
										self.init = False
										break

								elif event.button == 3:
									if(not self.Paused):
										#self.reset_color()
										
										if self.start is None:
											self.init = False
											break
											
										else:
											self.init = True
											self.goal = cb

											
											self.algo = AStarPath(self.search_space, self.start, self.goal,(self.XROW,self.YCOL))
											self.gen = self.algo.Active()
											
									else:
										if cb is not self.start or cb is not self.goal:
											cb.traverse = not cb.traverse
										
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.Running = False
					if event.key == pygame.K_f:
						self.Paused = not self.Paused
					if event.key == pygame.K_q:
						print (self.delay),
					if event.key == pygame.K_r:
						print (self.delay),
						self.delay += 15
					if event.key == pygame.K_q:
						self.delay -= 15					
					if event.key == pygame.K_d:
						if(not self.Paused):
							debug = not debug
				if event.type == pygame.QUIT:
					self.Running = False
					
					
					
			self.screen.blit(self.background,(0,0))
			
			for i in self.search_space:
				self.search_space[i].drawing(self.background, self.font1, self.init, debug)
				
			
				Nodes = self.search_space[i]
				if Nodes.parental:
					parentmid = (Nodes.parental.square.centerx, Nodes.parental.square.centery)
					selfmid = (Nodes.square.centerx, Nodes.square.centery)
					newrect = Nodes.square.inflate((Nodes.DIMENSIONS/1.25) * -1,(Nodes.DIMENSIONS/1.25) * -1)
					pygame.draw.ellipse(self.screen, (100,25,255), newrect, 1)
					pygame.draw.aaline(self.screen, (Olive), selfmid, parentmid, 5)
					
					#Nodes.parental._color =White
			try:
				self.start._color = Green
				self.goal._color = Grey
				
			except:
				
				bg = pygame.Surface((self.screen.get_size()[0]/3, self.screen.get_size()[1]/3))
				bg.fill(Olive)
				textrect = bg.get_rect()
			
			if(not self.Paused):
				if self.gen:
					try:
						
						self.CurrentNode = self.gen.next()
						adj = self.gen.next()
						adj._color = Yellow
						
						
						if(self.CurrentNode is not self.goal):
							self.CurrentNode._color = Teal
							
					except StopIteration:
						for i in self.algo.ROUTE:
							if i is not self.start:
								i._color = Olive
								
								self.gen = None

						
						
			if(self.Paused is True):
				bg.blit(self.font2.render("PAUSED", True, White), textrect.move(5,10))
				bg.blit(self.font2.render("Press F to unpause", True, White), textrect.move(5, 35))
				bg.blit(self.font2.render("Left click to set the start point", True, White), textrect.move(5,60))
				bg.blit(self.font2.render("Right click to set the end point", True, White), textrect.move(5, 85))
				
				self.screen.blit(bg, (0,0))
			if(debug):
				debugText = self.font2.render("DEBUG", True, Olive)
				self.screen.blit(debugText,(0,0))
				
			pygame.display.flip()
			
		pygame.quit()
		
		
if __name__ == '__main__':
	Game().run()