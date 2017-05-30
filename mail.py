import numpy as np
import itertools as it
from itertools import ifilterfalse
import random

MIN_TRAVEL_TIME = 1
MAX_TRAVEL_TIME = 5
N_LOCATIONS = 5

#List of locations
l = np.arange(N_LOCATIONS)

#List of two location combinations
x = list(it.permutations(l,2))

#List of travel times between two location combinations
travelTimes = np.random.uniform(MIN_TRAVEL_TIME,MAX_TRAVEL_TIME,len(x))

#salesMap Structure:
#(x,y):(a,b)
#x - Orgin location
#y - Destination location
#a - Travel time between x & y
#b - Average travel time
#salesMap = dict(zip(x, zip(travelTimes,zip([0]*len(x))))
salesMap = dict(zip(x, travelTimes))
avgTripTime = dict(zip(x, [0]*len(x)))

#example code
for start, end in salesMap:
  if start == 0:
    print salesMap[(start,end)]
#example code

#Begin Primary Algorithm Loop

#working variables
curLoc = 0
traveled = [0]
remaining = x[:]

#start loop
#prune options that move to current location
for i in range(1,N_LOCATIONS):
  remaining = list(ifilterfalse(lambda x: x[1]==curLoc, remaining))
  #prune to get move Options
  moveOpts = list(ifilterfalse(lambda x: x[0]!=curLoc, remaining))
  #placeholder - Calculate equity value of each option
  #select a move
  move = random.choice(moveOpts)[1]
  #update data based on move
  traveled.append(move)
  remaining = list(ifilterfalse(lambda x: x[0]==curLoc, remaining))
  curLoc = move

print traveled

#update neural network with result

#Populate potential moves from the list of available options, given where we are

#Select a point from the list of available options

#Remove options from the list of available options

#End Primary Algorithm Loop



