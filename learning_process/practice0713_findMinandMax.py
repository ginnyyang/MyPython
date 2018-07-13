#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def findMinAndMax(L):
	if len(L)==0:
		return(None,None)
	else:
		min=L[0]
		max=L[0]
		for i in L:
			if i<min:
				min=i
			if i >max:
				max=i
		return(min,max)
		
print(findMinAndMax([]))
print(findMinAndMax([7]))
print(findMinAndMax([7, 1]))
print(findMinAndMax([7, 1, 3, 9, 5]))

	