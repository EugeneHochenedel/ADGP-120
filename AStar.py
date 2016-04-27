#This script will contain the code specific to the A* Algorithm


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
			if(square.walhable && !DONE.Contains(square))
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
