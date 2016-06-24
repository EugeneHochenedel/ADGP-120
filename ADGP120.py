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

class Game:
	def __init__(self):
		pygame.init()
		pygame.font.init()
		
		self.search_space = {}
		self.selection = []
		
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
				
				if(y % self.XROW == 0 or y % self.XROW == self.XROW - 1):
					xWall = True
				else:
					xWall = False


				yWall = True if x % self.YCOL == 0 or x % self.YCOL == self.YCOL - 1 else False
				
				if(xWall or yWall):
					n.traverse = False
					n.Colors
					
				self.selection.append(n.onClick)
				
				self.search_space[id] = n
				id+=1
		
		for i in range(50 * 2):
			rng = random.randint(0,(self.XROW-1) * (self.YCOL-1))
			self.search_space[rng].traverse = False
			self.search_space[rng].Colors
			
			
			
		pad = (5,5)
		screen_width = self.YCOL * (pad[0] + self.WIDTH) + pad[1]
		screen_height = self.XROW * (pad[0] + self.HEIGHT) + pad[1]
		
		
		self.screen = pygame.display.set_mode((screen_width, screen_height))
		
		pygame.display.set_caption("ADGP-120 AStar")
		
		self.Running = True
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
	

	
	def run(self):
		while self.Running:
			events = pygame.event.get()
			for event in events:
				if event.type==VIDEORESIZE:
					self.screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
					
				if event.type == pygame.MOUSEBUTTONDOWN:
					for callback in self.selection:
						cb = callback(pygame.mouse.get_pos())
						if cb:
							if cb:
								if event.button == 1:
									init = False
									if self.algo:
										self.algo.Reset()
										self.gen = None
											
									if not cb.marked:
										self.start = cb
									
								elif event.button == 2:
									self.init = True
									self.defense = cb
									cb.traverse = not cb.traverse
									self.defense.Colors
										
								elif event.button == 3:
									if self.start is None:
										self.init = False
										break
											
									else:
										self.init = True
										self.goal = cb
											
										self.algo = AStarPath(self.search_space, self.start, self.goal,(self.XROW,self.YCOL))
										self.gen = self.algo.Active()
											
										
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.Running = False
				if event.type == pygame.QUIT:
					self.Running = False
					
			self.screen.blit(self.background,(0,0))
			
			for i in self.search_space:
				self.search_space[i].drawing(self.background)
				
			
				Nodes = self.search_space[i]
				if Nodes.parental:
					parentmid = (Nodes.parental.square.centerx, Nodes.parental.square.centery)
					selfmid = (Nodes.square.centerx, Nodes.square.centery)
					newrect = Nodes.square.inflate((Nodes.DIMENSIONS/1.25) * -1,(Nodes.DIMENSIONS/1.25) * -1)
					pygame.draw.ellipse(self.screen, (100,25,255), newrect, 1)
					pygame.draw.aaline(self.screen, (Olive), selfmid, parentmid, 5)
					
			try:
				self.start._color = Green
				self.goal._color = Grey
			except:
				
				bg = pygame.Surface((self.screen.get_size()[0]/3, self.screen.get_size()[1]/3))
				bg.fill(Olive)
				textrect = bg.get_rect()
			pygame.display.flip()
			
		pygame.quit()
		
		
if __name__ == '__main__':
	Game().run()