"""
Desc:
Python program to check if the integer number is in between a range
"""

# Given range
X = 1000
Y = 7000

def checkRange(num):
   # using comaparision operator
   if X <= num <= Y:
       print('The number {} is in range ({}, {})'.format(num, X, Y))
   else:
      print('The number {} is not in range ({}, {})'.format(num, X, Y))

# Test Input List
testInput = [X-1, X, X+1, Y+1, Y, Y-1]

for eachItem in testInput:
   checkRange(eachItem)