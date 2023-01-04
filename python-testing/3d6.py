import random

rolls = 3
dieSides = 6
totalRolls = 10000

def roller(dice, rolls, dieSides):
  result = 0
  for z in range(0,rolls):
    rollsmade = []
    for i in range(0,dice):
      roll = random.randint(1, dieSides)
      rollsmade.append(roll)
    for die in rollsmade:
      result += die
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

print("rolled 3d6",totalRolls,"times")
countResults(results, dieSides, totalRolls)
