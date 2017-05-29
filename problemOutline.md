Context:
* n Locations are spread throughout a region. 
* The travel time between any two locations is randomly selected from a uniform distribution between 1 and 5 units
* Starting at Location l1, a Traveling salesman must visit each of the n locations in the last amount of time and then back to his original location

**Objective Function:** Minimize total travel time

**Variable definition:**

**l** - Location
  [1, 2, 3, 4, 5, ..., n]
  
**travelTime** - Array((n * (n-1))
  [
    [((1,2), 1)],
    [((1,3), 1)],
    [((1,4), 1)],
    ...
    [((10,7), 1)],
    [((10,8), 1)],
    [((10,9), 1)]
  ]
  
**move** - Move from one location to another
  (lx, ln)
  
**Trip**
  [lx, ln, lp, ...]
  

    


