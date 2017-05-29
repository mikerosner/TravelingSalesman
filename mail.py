import numpy as np
import itertools as it

MIN_TRAVEL_TIME = 1
MAX_TRAVEL_TIME = 5
N_LOCATIONS = 5

#List of locations
l = np.arange(N_LOCATIONS)

#List of two location combinations
x = list(it.combinations(l,2))

#List of travel times between two location combinations
travelTimes = np.random.uniform(MIN_TRAVEL_TIME,MAX_TRAVEL_TIME,x.size)

salesMap = dict(zip(x, travelTimes))

#example code
for start, end in salesMap:
  if start == 0:
    print salesMap[(start,end)]
#example code

#Begin Primary Algorithm Loop

#working variables
startPoint = 0
traveled = 
remaining = x;

#Populate potential moves from the list of available options, given where we are

#Select a point from the list of available options

#Remove options from the list of available options

#End Primary Algorithm Loop



