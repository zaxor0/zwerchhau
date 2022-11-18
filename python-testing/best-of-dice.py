import random

def bestOfRoller(dice):
  results = []
  for z in range(0,999):
    rolls = []
    for i in range(0,dice):
      roll = random.randint(1, 6)
      rolls.append(roll)
  	
    highestVal = 0
    for die in rolls:
      if die > highestVal:
        highestVal = die
      
    results.append(highestVal)
  return results

def countResults(results,name):
  possibleResults = [ 1, 2, 3, 4, 5, 6 ]
  counts = [0, 0, 0, 0, 0, 0]
  for i in results:
    for j in possibleResults: 
      if i == j:
         counts[i-1] += 1
  print(name, counts)

bestOfTwo = bestOfRoller(2) 
countResults(bestOfTwo, "best of two")
bestOfThree = bestOfRoller(3) 
countResults(bestOfThree, "best of three")
