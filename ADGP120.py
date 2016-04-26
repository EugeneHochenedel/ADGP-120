"""
Eugene Hochenedel
ADGP-120
"""

import sys, pygame, Manhattan, Nodes
pygame.init()




#Pseudocode
'''
	TODO.Add(start)
	while (!TODO.IsEmpty())	// While there are squares to check
	{
		current = TODO.LowestF() // Get the lowest F
		TODO.Remove(current) 
		DONE.Add(current)
		foreach (adjacent square)
		{
			if (square.walkable && !DONE.Contains(square))
			{
				if (!TODO.Contains(square))
				{
					if (square.IsDestination())
					{
						RetracePath();
						return true; // Success
					}
					else
					{
						TODO.Add(square);
					
						square.Parent = current;
						// calcuate G and H
					}
				}
				else
				{
					int costToMoveToSquare = current.G + costToMove;
					if (costToMoveToSquare < square.G)
					{
						square.Parent = current;
						square.G = costToMoveToSquare;
						TODO.Sort();
					}
				}
			}
		}
	}
	return false; // Failure
'''