import sys, pygame
#pygame.init()

class Points:
	def __init__(self, x, y):
		self.XCoord = x
		self.YCoord = y
		#self.FValue
		#self.GValue
		#self.HValue
		self.Height = 30
		self.Width = 30 #Might only need one of these because squares
		self.Parent = False
		self.Passable = True
		self.Color = (255, 255, 255)

	def drawNode(self, constraint, surface?):
		for i in range(0, constraint, 30):
			if i <= constraint:
				pygame.draw.rect(surface?, self.Color, [0, 0, self.Height, self.Width], 2)
