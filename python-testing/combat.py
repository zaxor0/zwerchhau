import random

def statGenerator():
  stats = [ "STR", "DEX", "WILL", "INT"]
  results = {}
  # generate str dex will int (this is the assumed order)
  for stat in stats:
    rolls = []
    for i in range(0,2):
      roll = random.randint(1, 6)
      rolls.append(roll)
    highestVal = 0
    for die in rolls:
      if die > highestVal:
        highestVal = die
    results[stat]= highestVal
  # assuming level 1, endurance = str + dex + will + 1
  constitution = results["STR"] + results["DEX"] + results["WILL"]
  results["CON"] = constitution
  results["HP"] = 6
  results["Thrown"] = False
  return results

def combatAction(weapon):
  if weapon == "sword":
    ones = "slash"
  if weapon == "spear":
    ones = "thrust"
  roll = random.randint(1, 6)
  #print("ones are",ones,"rolled", roll)
  actions = [ones, "parry", "thrust", "slash", "dodge", "grapple"]
  return actions[roll-1]

def combatCheckResult(attack1, attack2):
  check = { "player" : "nil", "enemy" : "nil", "player2" : "nil", "enemy2" : "nil"}
  while True:
    # if at least 1 grapple
    if attack1 == "grapple" or attack2 == "grapple":
      # if both grapple, then STR
      if attack1 == "grapple" and attack2 == "grapple":
        check["player"] = "STR"
        check["enemy"] = "STR"
      # if only 1 grapple, then DEX and STR
      else:
        check["player"] = "DEX"
        check["enemy"] = "DEX"
        check["player2"] = "STR"
        check["enemy2"] = "STR"
      break
    # if at least 1 dodge
    if attack1 == "dodge" or attack2 == "dodge":
      # if both dodge, nothing
      if attack1 == "dodge" and attack2 == "dodge":
        None
      # if both parry, nothing
      if attack1 == "parry" or attack2 == "parry":
        None
      # if only 1 dodge, then DEX
      else:
        check["player"] = "DEX"
        check["enemy"] = "DEX"
      break
    # if at least one slashing
    if attack1 == "slash" or attack2 == "slash":
      # better of DEX or STR for both
      if player["STR"] > player["DEX"]:
        check["player"] = "STR"
      else:
        check["player"] = "DEX"
      if enemy["STR"] > enemy["DEX"]:
        check["enemy"] = "STR"
      else:
        check["enemy"] = "DEX"
      break
    # if both thrusting
    if attack1 == "thrust" and attack2 == "thrust":
      check["player"] = "DEX"
      check["enemy"] = "DEX"
      break
    # if a combination of thrusting and parrying, then DEX
    if (attack1 == "parry" and attack2 == "thrust") or (attack1 == "thrust" and attack2 == "parry"):
      check["player"] = "DEX"
      check["enemy"] = "DEX"
      break
    else:
      None
      break
  print("  PLAYER",attack1,"| ENEMY",attack2, " > ", check, "check!")
  return check

def combatRoll(player, enemy, playerAttack, enemyAttack, statRolls):
  # single grapple check
  if playerAttack == "grapple" and enemyAttack != "grapple":
    grappler = "player"
  elif playerAttack != "grapple" and enemyAttack == "grapple":
    grappler = "enemy"
  else:
    grappler = "none"
  # perform rolls
  reroll = True
  while reroll == True:
    playerRoll = random.randint(1, 6)
    playerStat = player[statRolls["player"]]
    playerTotal = playerRoll + playerStat
    enemyRoll = random.randint(1, 6)
    enemyStat = enemy[statRolls["enemy"]]
    enemyTotal = enemyRoll + enemyStat
    #print("  player: rolls a", playerRoll, "+", playerStat,statRolls["player"],"=",playerTotal)
    #print("  enemy:  rolls a", enemyRoll, "+", enemyStat,statRolls["enemy"],"=",enemyTotal)
    if enemyTotal > playerTotal:
      winner = "enemy"
      cRoll = enemyRoll
      reroll = False
    elif playerTotal > enemyTotal:
      winner = "player"
      cRoll = playerRoll
      reroll = False
    else:
      reroll = True
  # grappling!
  thrown = "none"
  if grappler != "none":
    if grappler != winner:
      if enemyAttack == "slash" or enemyAttack == "thrust":
        winner = "ememy"
        cRoll = enemyRoll
      elif playerAttack == "slash" or playerAttack == "thrust":
        winner = "player"
        cRoll = playerRoll
      else:
        winner = "none"
    #print("  GRAPPLED! Enter Strength Check!")
    if grappler == winner:
      # do a str check
      reroll = True
      while reroll == True:
        playerRoll = random.randint(1, 6)
        playerStat = player[statRolls["player2"]]
        playerTotal = playerRoll + playerStat
        enemyRoll = random.randint(1, 6)
        enemyStat = enemy[statRolls["enemy2"]]
        enemyTotal = enemyRoll + enemyStat
        #print("    player: rolls a", playerRoll, "+", playerStat,statRolls["player2"],"=",playerTotal)
        #print("    enemy:  rolls a", enemyRoll, "+", enemyStat,statRolls["enemy2"],"=",enemyTotal)
        if enemyTotal > playerTotal:
          winner = "enemy"
          thrown = "player"
          cRoll = enemyRoll
          reroll = False
        elif playerTotal > enemyTotal:
          winner = "player"
          thrown = "enemy"
          cRoll = playerRoll
          reroll = False
        else:
          print("  ...REROLLING")
          reroll = True
      print("  !!",thrown,"HAS BEEN THROWN!")
  print(" ",winner,"wins!")
  return winner, cRoll, thrown


def damageRoll(victim, cRoll, damageDie):
  damage = random.randint(1, damageDie)
  if victim["Thrown"] == False:
    if cRoll < 5:
       victim["CON"] -= damage
    if cRoll == 5:
       victim["CON"] -= (damage - 1)
       victim["HP"] -= 1
    if cRoll == 6:
       victim["CON"] -= (damage - 2)
       victim["HP"] -= 2
  if victim["Thrown"] == True:
    if cRoll == 1:
       victim["CON"] -= damage
    if cRoll == 2:
       victim["CON"] -= (damage - 1)
       victim["HP"] -= 1
    if cRoll == 3:
       victim["CON"] -= (damage - 1)
       victim["HP"] -= 1
    if cRoll == 4:
       victim["CON"] -= (damage - 2)
       victim["HP"] -= 2
    if cRoll == 5:
       victim["CON"] -= (damage - 3)
       victim["HP"] -= 3
    if cRoll == 6:
       victim["CON"] -= (damage - 4)
       victim["HP"] -= 4
  return victim
  
# main
player = statGenerator()
enemy = statGenerator()
print("PLAYER",player)
print("ENEMY ",enemy,"\n")
playerWins = 0
enemyWins = 0
noWins = 0
combatRound = 0
#for i in range(0,100):
while player["CON"] > 0 and player["HP"] > 0 and enemy["CON"] > 0 and enemy["HP"] > 0:
  combatRound += 1
  #print("COMBAT ROUND",str(combatRound),"  |  PLAYER:",player["HP"],"HP /",player["CON"],"CON |  ENEMY:",enemy["HP"],"HP /",enemy["CON"],"CON")
  playerAttack = combatAction("sword")
  enemyAttack = combatAction("spear")
  statRolls = combatCheckResult(playerAttack, enemyAttack)
  if statRolls["player"] != "nil":
    winner, cRoll, thrown = combatRoll(player, enemy, playerAttack, enemyAttack, statRolls)
    if thrown == "none":
      if winner == "player":
        enemy = damageRoll(enemy, cRoll, 8)
      else:
        player = damageRoll(player, cRoll, 8)
    elif thrown == "player":
      player["Thrown"] = True
    elif thrown == "enemy":
      enemy["Thrown"] = True
  else:
    print("  nils")
  print("  player HP",player["HP"],"CON",player["CON"],"  |  ","enemy HP",enemy["HP"],"CON",enemy["CON"])

