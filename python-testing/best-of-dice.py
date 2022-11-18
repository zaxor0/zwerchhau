import random

totalRolls = 10000
dieSides = 6

def bestOfRoller(dice, totalRolls, dieSides):
  results = []
  for z in range(1,totalRolls):
    rolls = []
    for i in range(0,dice):
      roll = random.randint(1, dieSides)
      rolls.append(roll)
    highestVal = 0
    for die in rolls:
      if die > highestVal:
        highestVal = die
      
    results.append(highestVal)
  return results

def countResults(results,name, totalRolls, dieSides):
  possibleResults = [ 1, 2, 3, 4, 5, 6 ]
  counts = [0, 0, 0, 0, 0, 0]
  for i in results:
    for j in range(1,dieSides + 1): 
      if i == j:
         counts[i-1] += 1
  print(name, counts)
  print("SIDE ... PERCENT")
  for side in range(1, dieSides + 1):
    percentage = int(float(100 * (counts[side - 1] / totalRolls)))
    print(side, "......", percentage, "%")


bestOfOne = bestOfRoller(1, totalRolls, dieSides) 
countResults(bestOfOne, "best of one", totalRolls, dieSides)
bestOfTwo = bestOfRoller(2, totalRolls, dieSides) 
countResults(bestOfTwo, "best of two", totalRolls, dieSides)
bestOfThree = bestOfRoller(3, totalRolls, dieSides) 
countResults(bestOfThree, "best of three",totalRolls, dieSides)
