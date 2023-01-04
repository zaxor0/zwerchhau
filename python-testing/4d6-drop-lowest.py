import random

rolls = 4
dieSides = 6
totalRolls = 10000

def roller(dice, rolls, dieSides):
  result = 0
  lowest = 18
  position = 0
  rollsmade = []
  for z in range(0,rolls):
    for i in range(0,dice):
      roll = random.randint(1, dieSides)
      if roll < lowest:
        lowest = roll
        lowestPosition = position
      rollsmade.append(roll)
      position += 1
  rollsmade.pop(lowestPosition)
  result = sum(rollsmade)
  return result

def countResults(results, dieSides, totalRolls):
  possibleResults = [ 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 ]
  counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  for i in results:
    for j in possibleResults:
      if i == j:
        counts[j-2] += 1
  for roll in possibleResults:
    percentage = float(100 * (counts[roll - 2] / totalRolls))
    print(roll, "......",round(percentage,3), "%")


results = []
for i in range(totalRolls):
  totalSum = roller(1, rolls, dieSides) 
  results.append(totalSum)

print("rolled 4d6 and dropped the lowest",totalRolls,"times")
countResults(results, dieSides, totalRolls)
