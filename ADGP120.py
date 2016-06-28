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

				if(x % self.YCOL == 0 or x % self.YCOL == self.YCOL - 1):
					yWall = True
				else:
					yWall = False
				
				if(xWall or yWall):
					n.traverse = False
					n.colors
				
				
				self.selection.append(n.onClick)
				
				self.search_space[id] = n
				id+=1
		
		for i in range(50 * 2):
			rng = random.randint(0,(self.XROW-1) * (self.YCOL-1))
			self.search_space[rng].traverse = False
			self.search_space[rng].colors
			
		pygame.init()
			
		pad = (5,5)
		screen_width = self.YCOL * (pad[0] + self.WIDTH) + pad[1]
		screen_height = self.XROW * (pad[0] + self.HEIGHT) + pad[1]
		
		self.font1 = pygame.font.Font(None, 14)
		
		self.screen = pygame.display.set_mode((screen_width, screen_height))
		
		pygame.display.set_caption("ADGP-120 AStar")
		
		self.Running = True
		self.start = Points(x, y, id)
		self.init = False
		self.goal = Points(x, y, id)
		self.defense = None
		self.runner = None
		self.general = None
	
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill(Black)
	
	def run(self):
		debug = False
		while self.Running:
			events = pygame.event.get()
			for event in events:
				if event.type == pygame.MOUSEBUTTONDOWN:
					for checking in self.selection:
						review = checking(pygame.mouse.get_pos())
						if review:
							
							if event.button == 1:
								init = False
								if self.runner:
									self.runner.Values()
									self.general = None
										
								if not self.init:
									self.start = review
								#	review.details()
									review.traverse = True
							
							if event.button == 2:
								self.init = True
								self.defense = review
								review.traverse = not review.traverse
								self.defense.colors
							
							if event.button == 3:
								if self.start is None:
									self.init = False

								else:
									self.init = True
									self.goal = review
									review.traverse = True
											
									self.runner = AStarPath(self.search_space, self.start, self.goal,(self.XROW,self.YCOL))
									self.general = self.runner.Active()
										
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.Running = False
					if event.key == pygame.K_d:
						debug = not debug
				if event.type == pygame.QUIT:
					self.Running = False
					
			self.screen.blit(self.background,(0,0))
			
			for i in self.search_space:
				self.search_space[i].drawing(self.background, self.font1, self.init, debug)
			
			for i in self.search_space:
				self.start.colors = Green
				self.goal.colors = Grey
			
				Nodes = self.search_space[i]
				if Nodes.parental:
					parentmid = (Nodes.parental.square.centerx, Nodes.parental.square.centery)
					selfmid = (Nodes.square.centerx, Nodes.square.centery)
					newrect = Nodes.square.inflate((Nodes.DIMENSIONS/1.25) * -1,(Nodes.DIMENSIONS/1.25) * -1)
					pygame.draw.ellipse(self.screen, (Blue), newrect, 1)
					pygame.draw.aaline(self.screen, (Olive), selfmid, parentmid, 5)
					
			if(debug):
				debugText = self.font1.render("DEBUG", True, Olive)
				self.screen.blit(debugText,(0,0))
			
			pygame.display.flip()
			
		pygame.quit()

Game().run()