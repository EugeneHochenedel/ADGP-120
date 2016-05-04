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

class Points(object):
	def __init__(self, x, y, id):
		self.adjacents = []
		self.parental = None
		self._passable = True
		self._gValue = 0
		self._hValue = 0
		self._fValue = 0
		Dimensions = 40
		self.width, self.height = [Dimensions, Dimensions]
		self._id = id
		self.index = (x, y)
		self.x = (self.width + 5) * x + 5
		self.y = (self.height + 5) * y + 5
		self.position = (self.width * x, self.height * y)
		self.screenPosition = (self.x, self.y)
		self.square = pygame.Rect(self.x, self.y, self.width, self.height)
		self.placement = pygame.Surface((self.width, size.height)) #Only required arguments for pygame.Surface are the sizes.
		self.marked = False
		self._color = White
		
	@property #Turns the traverse() method into a read-only attribute getter of the same name 
	def traverse(self):
		return self._passable
	@traverse.setter #Creates a copy of the traverse property that can be accessed
	def traverse(self, value):
		#white = (255, 255, 255)
		#red = (255, 0, 0)
		#if value:
		#	self.color = (255, 255, 255)
		#else:
		#	self.color = (255, 0, 0)
		self._passable = value
		
	@property
	def fValue(self):
		return self._fValue
	
	@fValue.setter
	def fValue(self, value):
		self._fValue = value
		
	@property
	def gValue(self):
		return self._gValue
	
	@gValue.setter
	def gValue(self, value):
		self._gValue = value
	
	@property
	def hValue(self):
		return self._hValue
	
	@hValue.setter
	def hValue(self, value):
		self._hValue = value * 10
	
	@property
	def Colors(self):
		return self._color
	
	@Colors.setter
	def Colors(self, value):
	#	white = (255, 255, 255)
	#	red = (255, 0, 0)
		
	#	if value is red:
	#		self.Color = value
	#		self.marked = True
	#	else:
	#		self.Color = value
		self._color = value
	
	def details(self):
		print("Position =", self.position)
		ids = " "
		for i in self.adjacents:
			ids += " " + str(i._id)
		print("Neighbors: ", ids)
		print("Index: ", self.index)

	def drawing(self, screen, font, init = True, text = True):
		self.placement.fill(self._color)
		screen.blit(self.placement, self.screenPosition)
		if self.traverse == True:
		#	self.Colors(Grey)
			textf = font.render("F = " + str(self.f), True, (1, 1, 1))
			textgh = font.render("G = " + str(self.g) + "H = " + str(self.h), True, (1, 1, 1))
			textfpos =  (self.x, self.y)
			textghpos = (self.x, self.y + self.height - 10)
			
			if init and text:
				screen.blit(textf, textfpos)
				screen.blit(textgh, textghpos)
				'''	#if self.traverse == False:
	
	def onClick(self, position):
		originalColor = self.colors
		newColor = Grey
		x = position[0]
		y = position[1]
		o = None
		if(x > self.square.left and x < self.square.right and y > self.square.top and y < self.square.bottom):
			if(self.marked == False):
				self._color = newColor
			o = self
		return o'''