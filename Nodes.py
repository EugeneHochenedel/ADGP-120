import pygame, math
from pygame import *
from math import *

#Color	#(R,G,B)
Red = (255, 0, 0)
Orange = (255, 165, 0)
Yellow = (255, 255, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Indigo = (75, 0, 130)
Teal =(0,128,128)
Violet = (238, 130, 238)
Black = (0, 0, 0)
White = (255, 255, 255)
Grey = (128, 128, 128)
Olive =(128,128,0)

class Node:
	def __init__(self, index):
		
		self.graph = []
		self.id = index
		#self.Nodes = Total[0]
		#self.Near = []
		self.size = 3
		self.top = 0
		self.bottom = None
		self.left = None
		self.right = 0
		self.tLeft = None
		self.bLeft = 0
		self.tRight = 0
		self.bRight = 0
		
	def Graph():
		for i in range(0, self.size*self.size):
			space = Node(i)
			graph.append(space)
			
	def Immediate(self, node):
		for node in self.graph:
		#	i = self
			if (node.id - self.size) < 0:
				node.top = graph[self.id]
				print(self.id)
				return self.top
				
			else:
				node.top = graph[self.id - self.size]
				print(self.id)
				return self.top
			if(node.id + self.size) > self.size*self.size:
				node.bottom = graph[self.id]
				print(self.id)
				return self.bottom
			else:
				node.bottom = graph[self.id + self.size]
				print(self.id)
				return self.bottom
			if (node.id % self.size == 0 or node.id == 0):
				node.left = graph[self.id]
				print(self.id)
				return self.left
			else:
				node.left = graph[self.id - 1]
				print(self.id)
				return self.left
			if (node.id + 1) % self.size == 0:
				node.right = graph[self.id]
				print(self.id)
				return self.right
			else:
				node.right = graph[self.id + 1]
				print(self.id)
				return self.right
			
		
		
	def Diag():
		for i in graph:
			i.tLeft = graph[i.top.left]
			i.bLeft = graph[i.bottom.left]
			i.tRight = graph[i.top.right]
			i.bRight = graph[i.bottom.right]
	
	
	'''def Neighbors(self, node):
		checking = self.Nodes
		top = node.id - 3
		bottom = node.id + 3
		left = node.id - 1
		right = node.id + 1
		tLeft = top - 1
		tRight = top + 1
		bLeft = bottom - 1
		bRight = bottom + 1
		Nay = [top, bottom, left, right, tLeft, bLeft, tRight, bRight]
		for i in Nay:
			if i not in self.Near:
				checking.append(i)
		return checking'''
				
def Main():
	graph = []
	for i in range(0,9):
		n = Node(i)
		graph.append(n)
		
	selected = input("Select a value between 0 and 9: ")
	#if selected in graph:
	#	print(selected.right)
	
	for i in graph:
		if i.id is selected:
			i.Immediate(i.id + 1)
			print(i.Immediate(i.id))
		else:	
			print(i.id)
		
		#print(" ")
		
	#input = raw_input("pause")
	
Main()