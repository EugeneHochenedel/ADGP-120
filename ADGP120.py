"""
Eugene Hochenedel
ADGP-120
"""

import pygame
import AStar
import Nodes
import math
import os
import pygame.locals
import random
from AStar import *
from Nodes import *
from pygame import mixer
from pygame.locals import *
'''
from os import *
from math import *
from random import *
from pygame import *
'''

#Color	#(R,G,B)
Lime =(0,255,0)
Cyan =(0,255,255)
Magenta =(255,0,255)
Silver =(192,192,192)
Maroon =(128,0,0)
Olive =(128,128,0)
Teal =(0,128,128)
Navy =(0,0,128)
Sky = (128, 128, 255)
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

class Game:
	def __init__(self):
		os.environ['SDL_VIDEO_CENTERED'] = '1'
		path = os.path.dirname(os.path.realpath("__file__"))
		pygame.init()
		pygame.font.init()
		pygame.mixer.pre_init(44100, -16, 1, 512)
		pygame.mixer.init()
		
		self.search_space = {}
		self.mouse_listeners = []
		
		id = 0
		self.ROWS = 20
		self.COLS = 50
		self.WIDTH = 30
		self.HEIGHT = 30
		
		for x in range(self.COLS):
			for y in range(self.ROWS):
				
				n = Points(x, y, id)
				
				if(x >= 5 and x <= 6 and y >= 5 and y <= 8):
					n._passable = False
					
				TopWall = True if y % self.ROWS == 0 else False
				BottomWall = True if y % self.ROWS == self.ROWS - 1 else False
				LeftWall = True if x % self.COLS == 0 else False
				RightWall = True if x % self.COLS == self.COLS - 1 else False
				
				if(TopWall or BottomWall or LeftWall or RightWall):
					n._passable = False
					
				self.mouse_listeners.append(n.onClick)
				
				self.search_space[id] = n
				id+=1
		
		
		mod = 15
		for i in range(50 + 50 + 50):
			rng = random.randint(0,(self.ROWS-1) * (self.COLS-1))
			self.search_space[rng]._passable = False
			
			
			
		pad = (5,5)
		screen_width = self.COLS * (pad[0] + self.WIDTH) + pad[1]
		screen_height = self.ROWS * (pad[0] + self.HEIGHT) + pad[1]
		
		
		self.screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
		
		self.font1 = pygame.font.Font(None, 14)
		self.font2 = pygame.font.Font(None, 28)
		
		pygame.display.set_caption("ADGP-120 AStar")
		
		self.Running = True
		self.Paused = False
		self.start = None
		self.init = False
		self.goal = None
		self.algo = None
		self.gen = None
		self.delay = 50
		
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill(Black)
		
	def reset_color(self):
		for i in self.search_space:
			if self.search_space[i]._passable:
				self.search_space[i].color = White
			else:
				self.search_space[i].color = Red
	

	
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
									self.reset_color()
									init = False
									if self.algo:
										self.algo.Reset()
										self.gen = None
									if not cb.marked:
										print("set start")
										cb.details()
										self.start = cb
									

								elif event.button == 3:
									if(not self.Paused):
										self.reset_color()
										print("left click")
										if self.start is None:
											print("Must set start")
											self.init = False
											break
										else:
											self.init = True
											self.goal = cb
											self.goal.details()
											
											self.algo = AStarPath(self.search_space, self.start, self.goal,(self.ROWS,self.COLS))
											
											self.gen = self.algo.Active()
											
									else:
										if cb is not self.start or cb is not self.goal:
											cb.traverse = not cb.traverse
										
										
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.Running = False
					if event.key == pygame.K_f:
						self.Paused = not self.Paused
						if self.Paused:
							pygame.mixer.pause()
						if not self.Paused:
							pygame.mixer.unpause()
					if event.key == pygame.K_q:
						print (self.delay),
					if event.key == pygame.K_r:
						print (self.delay),
						self.delay += 15
					if event.key == pygame.K_q:
						self.delay -= 15					
					if event.key == pygame.K_d:
						debug = not debug
				if event.type == pygame.QUIT:
					self.Running = False
					
					
					
			self.screen.blit(self.background,(0,0))
			
			for i in self.search_space:
				self.search_space[i].drawing(self.background, self.font1, self.init, debug)
				
			for i in self.search_space:
				pointers = self.search_space[i]
				if pointers.parental:
					parentmid = (node.parent.rect.centerx, node.parent.rect.centery)
					selfmid = (node.rect.centerx, node.rect.centery)
					newrect = node.rect.inflate((node.width/1.25) * -1,(node.height/1.25) * -1)
					pygame.draw.ellipse(self.screen, (100,25,255), newrect, 1)
					pygame.draw.aaline(self.screen, (100,25,255), selfmid, parentmid, 5)
			try:
				self.start._color = Green
				self.goal.color = Grey
			except:
				
				bg = pygame.Surface((self.screen.get_size()[0]/3, self.screen.get_size()[1]/3))
				bg.fill(Indigo)
				textrect = bg.get_rect()
			
			if(not self.Paused):
				if self.gen == pointers:
					try:
						
						self.current = self.gen.next()
						adj = self.gen.next()
						adj.color = Violet
						
						pygame.time.wait(self.delay)
						
						if(self.current is not self.start):
							self.current._color = Navy
							
					except StopIteration:
						for i in self.algo.Route:
							if i is not self.start:
								i._color = Orange
						
						print("finished")
						
						self.gen = None
						
			else:
				bg.blit(self.font2.render("PAUSED", True, White), textrect.move(5,10))
				bg.blit(self.font2.render("Press F to unpause", True, White), textrect.move(5, 35))
				bg.blit(self.font2.render("Left click to add new blockers", True, White), textrect.move(5,60))
				bg.blit(self.font2.render("Right click to set starting position!", True, White), textrect.move(5, 85))
				bg.blit(self.font2.render("Try to block off the bad guy!", True, White), textrect.move(5, 110))
				self.screen.blit(bg, (0,0))
			if(debug):
				debugText = self.font2.render("DEBUG", True, Lime)
				self.screen.blit(debugText,(0,0))
				
			pygame.display.flip()
			
		pygame.quit()
		
		
if __name__ == '__main__':
	Game().run()