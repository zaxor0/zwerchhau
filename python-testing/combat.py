import random

def statGenerator():
  results = []
  # generate str dex will int (this is the assumed order)
  for die in range(0,4):
    rolls = []
    for i in range(0,2):
      roll = random.randint(1, 6)
      rolls.append(roll)
    highestVal = 0
    for die in rolls:
      if die > highestVal:
        highestVal = die
    results.append(highestVal)
  # assuming level 1, endurance = str + dex + will + 1
  endurance = 1
  for stat in range(0,3):
     endurance += results[stat]
  results.append(endurance)
  results.append(6)
  return results

def combatAction(weapon):
  if weapon == "sword":
    ones = "cut"
  if weapon == "spear":
    ones = "thrust"
  roll = random.randint(1, 6)
  actions = [ones, "cut", "thrust", "parry", "dodge", "grapple"]
  return actions[roll-1]

def combatCheckResult(attack1, attack2):
  check = "nil"
  while check == "nil":
    if attack1 == "grapple" or attack2 == "grapple":
      check = "dex then str"
      if attack1 == "grapple" and attack2 == "grapple":
        check = "str"
      break
    if attack1 == "dodge" or attack2 == "dodge":
      check = "dex"
      if attack1 == "dodge" and attack2 == "dodge":
        check = "nil"
      if attack1 == "parry" or attack2 == "parry":
        check = "nil"
      break
    if attack1 == "cut" or attack2 == "cut":
      check = "dex or str"
      break
    if attack1 == "thrust" and attack2 == "thrust":
      check = "dex"
      break
    if (attack1 == "parry" and attack2 == "thrust") or (attack1 == "thrust" and attack2 == "parry"):
      check = "dex"
      break
    else:
      break
  print("...", attack1, "v.", attack2, " > ", check)
  return check

def combatRoll(player, enemy, combatCheck):
  stats = []
  if combatCheck == "str":
    stats.append(0)
  if combatCheck == "dex":
    stats.append(1)
  if combatCheck == "dex then str":
    stats.append(1) 
    stats.append(0) 
  if combatCheck == "dex or str":
    if player[0] > player[1]:
      stats.append(0)
    if player[1] > player[0]:
      stats.append(1)
  for stat in stats:
    playerRoll = random.randint(1, 6)
    playerTotal = playerRoll + player[stat]
   #print("player rolls a", playerRoll, "with a +", player[stat])
    enemyRoll = random.randint(1, 6)
    enemyTotal = enemyRoll + enemy[stat]
  # print("enemy rolls a", enemyRoll, "with a +", enemy[stat])
    if enemyTotal > playerTotal:
      winner = "enemy"
      cRoll = enemyRoll
    else:
      winner = "player"
      cRoll = playerRoll
    print(winner, "wins!")
  return winner, cRoll

def damageRoll(victim, cRoll, damageDie):
  damage = random.randint(1, damageDie)
  if cRoll < 5:
     print("endurance damage", damage)
     victim[4] -= damage
  if cRoll == 5:
     print("-1 to flesh and endurance damage", damage -1)
     victim[4] -= (damage - 1)
     victim[5] -= 1
  if cRoll == 6:
     print("-2 to flesh and endurance damage", damage -2)
     victim[4] -= (damage - 2)
     victim[5] -= 2
  return victim
  
# main
player = statGenerator()
enemy = statGenerator()
print("(STR, DEX, WILL, INT, Endurance, HP)")
print(player, "wielding a sword")
print("...versus...")
print(enemy,"wielding a spear")
combatRound = 0
while player[4] > 0 and player[5] > 0 and enemy[4] > 0 and enemy[5] > 0:
  print("new round")
  combatRound += 1
  playerAttack = combatAction("sword")
  enemyAttack = combatAction("spear")
  combatCheck = combatCheckResult(playerAttack, enemyAttack)
  if combatCheck != "nil":
    winner, cRoll = combatRoll(player, enemy, combatCheck)
    if winner == "player":
      enemy = damageRoll(enemy, cRoll, 6)
    else:
      player = damageRoll(player, cRoll, 6)
  print("player HP",player[5],"En",player[4],"  |  ","enemy HP",enemy[5],"En",enemy[4])
  print("...end combat round", combatRound)
