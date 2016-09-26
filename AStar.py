import math, Nodes
from math import *
from Nodes import *

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
Olive =(128,128,0)

class Algorithm(object):
	def __init__(self, Looking, Beg, Fin, area):
		self._searchArea = Looking
		self._initalPoint = Beg
		self._finalPoint = Fin
		self._currentPoint = None
		self._Values = None
		self.XROWS = area[0]
		self.YCOLUMNS = area[1]
		self.OPEN = []
		self.CLOSE = []
		self.ROUTE = []
		
		self.screenPosition = (self.x, self.y)
		
		self.square = pygame.Rect(self.x, self.y, self.DIMENSIONS, self.DIMENSIONS)
		self.placement = pygame.Surface((self.DIMENSIONS, self.DIMENSIONS))
		
		self.adjacents = []
	
	def CurrentCell(self, value):
		self._currentPoint = value
		return self._currentPoint
		
	def movementCost(self):
		return self._gValue
	
	def getRoutes(self, node):
		path = []
		CurrentCell = node
		if(self._finalPoint == node):
			return path[self._finalPoint]
		if CurrentCell is not self._initalPoint:
			return None
		while CurrentCell is not self._initalPoint:
			path.append(CurrentCell.parental)
			CurrentCell = path[0]
			
		
	def Active(self):
		self.OPEN.append(start)
		
		while self.OPEN[0] is not self._finalPoint:
			self.OPEN.sort(keys = lambda x : x.fValue)
			CurrentCell = self.OPEN[0]

#Pseudocode
'''
	TODO.Add(start)
	while(!TODO.IsEmpty()) //While there are squares to check
	{
		current = TODO.LowestF() //Get the lowest F value
		TODO.Remove(current)
		DONE.Add(current)
		foreach(adjacent square)
		{
			if(square.walkable && !DONE.Contains(square))
			{
				if(!TODO.Contains(square))
				{
					if(square.IsDestination())
					{
						RetracePath();
						return true; //Success
					}
					else
					{
						TODO.Add(square);
						square.Parent = current; //calculate G and H
					}
				}
				else
				{
					int costToMoveToSquare = current.G + costToMove;
					if(costToMoveToSquare < square.G)
					{
						square.Parent = current;
						square.G = costToMoveToSquare;
						TODO.Sort();
					}
				}
			}
		}
	}
	return false; //Failure
'''
#Pseudocode Mr. Matt posted
'''
	List Astar(S, D, Space):
		Add S to OL //Open List
		Set C to LowestF in OL //C is current node
		foreach adjacent in C.adjacents //Check all nodes adjacent to C
			if D is in OL or OL is Empty //Stop if the destination is in the Open List or if the list is empty
				break;
			if adj is not in OL and is not in CL and is walkable //CL is closed list. Checks If the adjacent node isn't in the OL or CL and is walkable
				Add adj to OL //Adds the unlisted node to the OL
				set adj.parent to C //Changes the parent of the adjacent node to current
				set adj.g to (C.g + cost to move from C to adj) //Calculates G of the adjacent node by adding the movement cost for that node to the G of the current node
				set adj.h to Heuristic(adj, D) //Calculates the H value of the adjacent node by taking it's position and that of the destination
				set adj.f to g+h //Calculates the F value of the adjacent node
			else if adj is in OL //someone already added //Checks if the adjacent node is in the Open List
				if C.g < adj.g //Checks if the G value of the current node is less than that of the adjacent node. Calculations should be done already
					set adj.parent to C //Makes the adjacent parent the Current node
					set adj.g to C.g + cost to move from C to adj //Calculates G of the adjacent node by adding the movement cost for that node to the G of the current node
		Retrace the path from D
'''