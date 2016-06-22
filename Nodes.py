import pygame, math

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
Teal = (0, 128, 128)

class Points(object):
	def __init__(self, x, y, id):
		self.adjacents = []
		self.parental = None
		self._passable = True
		self._gValue = 0
		self._hValue = 0
		self._fValue = 0
		#Determinse the size of the cells
		self.DIMENSIONS = 40
		#self.width, self.height = self.DIMENSIONS, self.DIMENSIONS
		self.id = id
		self.index = (x, y)
		#Controls the distance between cells and the border
		self.x = (self.DIMENSIONS + 5) * x + 5
		self.y = (self.DIMENSIONS + 5) * y + 5
		#Output only
		#self.position = (self.DIMENSIONS * x, self.DIMENSIONS * y)
		self.screenPosition = (self.x, self.y)
		self.square = pygame.Rect(self.x, self.y, self.DIMENSIONS, self.DIMENSIONS)
		self.placement = pygame.Surface((self.DIMENSIONS, self.DIMENSIONS)) #Only required arguments for pygame.Surface are the sizes.
		self.marked = None
		self._color = Yellow
		
	@property #Turns the traverse() method into a read-only attribute getter of the same name 
	def traverse(self):
		return self._passable
	@traverse.setter #Creates a copy of the traverse property that can be accessed
	def traverse(self, value):
		yellow = (255, 255, 0)
		red = (255, 0, 0)
		self._passable = value
		if self._passable == True:
			self._color = yellow
		else:
			self._color = red
		
	@property
	def checker(self):
		return self.marked
		
	@checker.setter
	def checker(self, value):
		self.marked = value
		teal = (0, 128, 128)
		violet = (238, 130, 238)
		
		if self.marked == True:
			self._color = teal
		elif self.marked == False:
			self._color = None
	
	@property
	def fValue(self):
		return self._fValue
	
	@property
	def hValue(self):
		return self._hValue
		
	@property
	def gValue(self):
		return self._gValue
	
	@fValue.setter
	def fValue(self, value):
		self._fValue = value
	
	@gValue.setter
	def gValue(self, value):
		self._gValue = value
		self._fValue = self._gValue + self._hValue
	
	@hValue.setter
	def hValue(self, value):
		self._hValue = value
		self._fValue = self._gValue + self._hValue
	
	@property
	def Colors(self):
		return self._color
	
	@Colors.setter
	def Colors(self, value):
		yellow = (255, 255, 0)
		red = (255, 0, 0)
		
		if value is red:
			self._color = value
			#self.marked = True
		else:
			self._color = value

		self._color = value
	
	def details(self):
		#print("Position =", self.position)
		ids = " "
		for i in self.adjacents:
			ids += str(i.id) + " " + str(i.index)
		print("Neighbors: ", ids)
		print("Index: ", self.index)

	def drawing(self, screen, font, init = True, text = True):
		self.placement.fill(self._color)
		screen.blit(self.placement, self.screenPosition)
		if self.traverse == True:
		#	self.Colors(Grey)
			textf = font.render("F = " + str(self.fValue), True, (Violet))
			textg = font.render("G = " + str(self.gValue), True, (Violet))
			texth = font.render("H = " + str(self.hValue), True, (Violet))
			textfpos = (self.x + 1, self.y)
			textgpos = (self.x + 1, self.y + self.DIMENSIONS - 20)
			texthpos = (self.x + 1, self.y + self.DIMENSIONS - 10)
			
			if init and text:
				screen.blit(textf, textfpos)
				screen.blit(textg, textgpos)
				screen.blit(texth, texthpos)
	
	
	def onClick(self, position):
		originalColor = self._color
		newColor = self.checker
		x = position[0]
		y = position[1]
		o = None
		if(x > self.square.left and x < self.square.right and y > self.square.top and y < self.square.bottom):
			if(self.checker == False):
				self._color = newColor
			o = self
		return o