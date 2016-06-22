#This script will contain the code specific to the A* pathing
import math, Nodes

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

class AStarPath(object):
	def __init__(self, Space, Beginning, End, area):
		self.OPENLIST = []
		self.CLOSELIST = []
		self.ROUTE = []
		self._plot = Space
		self._first = Beginning
		self._last = End
		self._current = self._first
		self.xRows = area[0]
		self.yColumns = area [1]
		
		self.Reset()
	
	@property
	def CurrentNode(self):
		return self._current
	
	@CurrentNode.setter
	def CurrentNode(self, value):
		self._current = value
		
	def Reset(self):
		for x in self._plot:
			node = self._plot[x]
			node.parental = None
			node.gValue = 0
			node.fValue = 0
			node.hValue = 0
		
			self.SetAdjacents(node)
			xValues = int(math.fabs(self._last.index[0] - node.index[0]))
			yValues = int(math.fabs(self._last.index[1] - node.index[1]))
			if xValues > yValues:
				node.hValue = 14 * yValues + 10 * (xValues - yValues)
			else:
				node.hValue = 14 * xValues + 10 * (xValues + yValues)
		print("Node H: ", node.hValue)
			
	def Active(self):
	#	self.Reset()
		open = self.OPENLIST
		close = self.CLOSELIST
		start = self._first
		open.append(start)
		print(open)
		
		while open:
			open.sort(key = lambda x : x.fValue)
			CurrentNode = open[0]
			
			open.remove(CurrentNode)
			close.append(CurrentNode)
			i = 0
			for adj in CurrentNode.adjacents:
				if adj.traverse and adj not in close:
					if adj not in open:
						open.append(adj)
						adj.parental = CurrentNode
						adj.gValue = 10 if i < 4 else 14
					else:
						adj.parental = CurrentNode
						adj.gValue = 10 if i < 4 else 14
						movecost = 1.414 + adj.gValue
						if movecost < adj.gValue:
							adj.parental = self._last
							adj.gValue = movecost
					i = i + 1
			if self._last is open:
				self.ROUTE = self.GetRoute(self._last)
				break;
				
	def TestStart(self):
		self.CurrentNode = self._first
		
	def GetRoute(self, node):
		path = self.CLOSELIST
		CurrentNode = node
		while(CurrentNode != self._last):
			path.append(CurrentNode.parental)
			CurrentNode = CurrentNode.parental

			break;
		return path
		
	def SetAdjacents(self, node):
		if node.adjacents:
			node.adjacents = []
		rows = self.xRows
		columns = self.yColumns
		bottom  = node.id + 1
		top = node.id - 1
		right = node.id + rows
		left = node.id - rows
		tRight = right - 1
		bRight = right + 1
		tLeft = left - 1
		bLeft = left + 1
		adjs = [top, bottom, left, right, tLeft, bLeft, tRight, bRight]
		for i in adjs:
			if i in self._plot:
				if self._plot[i].traverse:
					node.adjacents.append(self._plot[i])

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
	Used for Run?
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