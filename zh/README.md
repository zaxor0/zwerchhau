# Zwerchhau Combat System

The goal of Zwerchau is to provide a new tactical combat system for old school RPG systems; ideally, it will give fighter types more interesting choices in combat. However, this does add more crunch.

Ideas for a fully fleshed out RPG system are in the ![System Document](https://github.com/zaxor0/zwerchhau/blob/main/system.md).

## Damage, HP, Endurance
Instead of having one pool of hit points that increase with level, this system seeks to separate bodily health from the ability to survive combat.

There are two sets of HP, one set (**flesh**) represents you body and if it reaches 0 you die. The other (**endurance**) represents your constitution and ability to defence yourself in combat; if this reaches 0 you start taking damage to your body.

Damage from a successful attack skews towards endurance, but still may cause bodily damage. This means, a character may die while having positive endurance. 

- **Flesh** - These are the hit points of your physical body, if these are brought to 0 you may die.
  - At first level, this is equivelant to your HP per your rules system.
  - A second level and beyond, it is the maximum HP for your first level + 4. Additional points are rolled into **Endurance**.
  - Recovers per old school rules, 1 per day with overnight rest.
- **Endurance** - these are your hit points that represent you ability to defend yourself in combat.
  - If endurance is 0, you will collapse and be unable to defend yourself. Any future damage is dealt to **flesh**.
  - At first level, this is equal to your constitution
  - At later levels, any additional HP beyond your 1 level max + 4, are added to this number.
  - Recovers fully after a long (1h) rest, if you have less than half of your flesh it recovers only up to 3/4 rounded up.

It may be in the in the interest of high level games to limit additional HP gained with each level.

The outcome is that level 1 characters are less likely to die right away, and therefore can move slightly further into a given dungeon before they need to retreat for the night.

However, given the right circumstance a higher level player may die fairly quickly and would, therefore, still need to maintain caution while adventuring.

### HP Examples
- A level 1 fighter with a 10 constitution and 7 HP (1d8) has a flesh of 7 and a Endurance of 10
- A level 2 fighter with a 10 constitution and 15 HP (2d8) has a flesh of 12 and a endurance of 13
- A level 3 fighter with a 10 constitution and 21 HP (3d8) has a flesh of 12 and a endurance of 19

## Armor and Shields
Zwerchhau implements opposed checks for successful combat attacks, therefore AC is actually damage reduction instead of providing a target number for players "to hit."

#### Armor
Armor only reduces damage to **Flesh**, damage is only reduced between 1 and 3:

|       Armor        | Descend AC | Ascend AC | Damage Reduction |
|--------------------|------------|-----------|------------------|
| Light  (Leather)   |    7       |     12    |       1          |
| Medium (Chainmail) |    5       |     14    |       2          |
| Heavy  (Platemail) |    3       |     16    |       3          |

#### Shields
Shields only reduce damage to **Endurance**
- Reduce damage to endurace by 1 for each opponent
- Provide a +1 to defensive actions

## Initiave and Turn Order
This combat system is better suited to side versus side, than individual combat.

The side that lost gets actions per individual not involved in an opposed check or in defensive fighting.

Those casting spells are considered performing "dodge" with a "disengage" posture unless otherwise declared. 

## Melee Combat Loop

- Declare engagement posture
- Delcare primary opponent in case of more than 1
- Determine Player's Attacking Combat Action
- DM determines NPC's Attacking Combat Action
- Determine the opposed check based on results (dex, str, or both)
- Opposed Roll
  - Ability check roll, winner is **under but highest**
  - If both are under and equal, both deal half damage
  - If both are over / failures, reroll
- Damage Roll - Winner rolls their weapon's damage dice
  - Apply damage bonuses based on Strength
  - Apply damage bonuses based on opposed roll difference (5 or greater)
  - (Optional) Apply damage bonuses based on weapon type & action
  - Determine **Flesh** and **Endurance** split, divide by 2 & favor endurance.
  - Reduce flesh damage based on armor
  - Deal damage to to flesh, check for death
  - Deal damage to endurance, check for exhaustion
- For each opponent, reduce endurance by 1, increasing by 1 for each.
  - 1 for the first opponent, 2 for the second, and so on.
  - A shield negates 1 per opponent, meaning 0 for the first opponent, 1 for the second, and so on.

### Engagement Posture
In the thick of combat, the blows may turn to a grapple. Prior to attack players may choose their default posture, to engage in grapple or to disengage. 

If their default posture is to disengage, they gain a +1 on grappling DEX checks, but do not enter the grapple if they win.

### Multiple Opponents
If you are or could be attacked by more than 1 opponent, you need to delcare which opponent is primary focus. 

Non-primary / additional opponents gain a +1 to their opposed checks, meaning they need to roll under their ability score + 1 for a success.

### Combat Actions
Players decide which type of attack based on the following:

- Attack, add your to hit bonus to your ability, roll under for a success.
  - Thrusts: Piercing actions
  - Slashes / Cuts: Swinging & slicing actions
- Defensive Fighting: Focusing on parries without ripostes, regaining footing when downed.
  - Gain +1 to your roll if you have a shield, meaning roll under your ability score + 1
  - If you are prone due to melee, you gain a + 1 to your opposed check. If you win the opposed check you can stand up.
  - A difference of 5 or greater allows for a **Riposte**, a free follow up attack for half damage. Not applicable while prone due to melee.
- Dodges: evading an attack with quick movement
  - Gain +2 on opposed rolls, meaning roll under your ability score + 2
  - You do not gain the possibility for a riposte
- Grapples: clinging to your opponent to attempt a wrestling maneuvre, with or without your weapon
  - Single-sided grapple attempts take damage on failed opposed checks if the opponent performed a *slash* or *thrust*
  - Throw the opponent to the ground, greatly decreases opponent defenses, ideal action for a swift kill
  - Disarm the opponent, ideal to force an opponent to yield, 1d6 skill check
  - Choke your opponent, attempt to force the opponent to passout; if successful, you are occupied for 3 turns and are unable to defend yourself

#### To Hit Bonus
In descending AC systems, you have a THAC0, to determine your "to hit bonus" simply do 20 - THAC0. The result is your bonus.

Example:
- You are performing a Dexterity opposed check
- You have a dexterity of 15 and a THAC0 of 17
- 20 - 17 = 3, 15 + 3 = 18
- Roll under a 18 for success

Do **NOT** add strength bonuses to this check. Strength bonuses are only for damage.

### Combat Attack Results
The priorty table to determine result check:

|Priority | Opposing Rolls         | Check        |
|---------|------------------------|--------------|
|   1     | Grapple v. Grapple     | Str          |
|   2     | Grapple v. Any         | Dex then Str |
|   3     | Dodge v. Any           | Dex          |
|   4     | Slash v. Any           | Dex or Str   |
|   5     | Thrust v. Thrusts      | Dex          |
|   6     | Defensive v. Defensive | Dex          |
|   7     | Others                 | No Result    | 

### Opposed Checks
Once you've determined which check will occur, whether strength or dex (or both), each side rolls 1d20.

A success is **under but highest**:
- To succeed, roll equal to under your ability score
- To win the check, roll higher than your opponent
- If anyone rolls over their ability score, they fail
- If both sides roll over their ability score no one wins.

The higher value wins the check and deals damage. 

To succeed in a grapple check, you must first win a dex check to wrestle your opponent, and then a strength check to enter the grapple phase. If both sides attempt a grapple, you only need the strength check.

Opponents attacking someone performing "defensive fighting" still roll, but only "hit" on a 6. See below for more detail.

### Damage Dealt and Damage Bonuses
Damage is dealt based on the die roll of the appropriate weapon; however, damage is split between flesh and endurance. Damage to flesh is always dealt first; and therefore may cause a killing blow.

Roll the appropriate die for you given weapon. Add any damage bonuses.

There are two bonuses you add to your damage roll:
- one for strength
- One for opposed roll difference
- Optionally, one for weapon and attack types

#### Strength Bonus
Most OSR rule systems offer melee bonuses for a high Strength, add these to the total damage Roll.

#### Opposed Roll Difference Bonus
Based on the *difference* between the opposed dice rolls, the victor may deal additional damage to their opponent.

Starting at a difference of 5, increase the damage by 1 for a upright opponent or 3 for a down opponent. 

This bonus limited at a difference of 10, +5 to a upright opponent and +7 for a down opponent.

Add this bonus to your damage die roll.

#### Attack Type Bonus (Optional)
These are mentioned previously, but to restate:
- Thrusts
  - Additional damage (+1 Con) for 1h spears
  - Additional damage (+2 Con) for 2h spears
  - Additional damage (+1 HP) for 2h swords
- Slashes
  - Additional damage (+2 Con) for any medium, long, two-handed, or great weapon
  - Additional damage (+1 Con) for blunt great weapons
  - Additional damage (+1 HP) for sharp-edged great weapons

### Defensive Fighting
Defensive Fighting means focusing on parries without ripostes, and attempting to regaining footing when prone from melee.
  - Gain +1 to your roll if you have a shield, meaning roll under your ability score + 1
  - If you are prone due to melee, you gain a + 1 to your opposed check. If you win the opposed check you can stand up.
  - A difference of 5 or greater allows for a **Riposte**, a free follow up attack for half damage. Not applicable while prone due to melee.

### Dodge
On a succesful dodge roll a player suffers no damage from a single attack. 

Dodging provides better defense than defensive fighting, with a +2; however, players do not gain the possibility to make a riposte.

Those performing spellcasting are considering taking a dodge action in case they are attacked. If an opponent attacks them and the lose the opposed check (dex) the spell fails. 

### Grappling and Wrestling
#### One Sided Grapple Attempts
If only one combatant attempts a grapple, there are two checks:

- First dexterity, this represents the lunge or springing action an attacker would make to quickly close distance before a strike is made against them. Also, is represents the opponent swinging their weapon or moving away from the grappler. 
- Upon failure: If the opposing side performed a *thrust* or *slash*, they deal and roll for damage.
- Upon success: A standard opposed strength check to see who dominates.
  - The side that performed grapple gets a +1 on their check, meaning roll under their ability score + 1 for success.

#### Grapple Strength Check
If both sides are performing a grapple, perform an opposed strength check, both sides roll 1d20, with the *under but hightest* being the winner.

The winner performs a wrestling maneuvre:

- **Disarm** the opponent: Attempt to remove the opponent's weapon, this is ideal for forcing a yield
- **Throw** the opponent to the ground: Drastically reduce an opponents defensive capabilities by forcing them into a prone position, this is ideal for a swift kill.
- **Choke** the opponent: Attempt to strangle the opponent, lethal or non lethal. Requires 3 rounds of combat, you are unable to defend yourself during these rounds.

### Riposte
A riposte is follow up to a successful parry that allows for a damage roll halved; with weapon specailization.

### Bonuses to AC
If a player character has a "bonus to AC" such as a halfling bonus +2 versus giants, then instead treat this as a -2 on the opponent's opposed roll.

That means, for this roll, the opponent's ability is considered 2 lower, and they must roll under the new lower number to succeed.

## Ranged Combat
Ranged combat is a simplified process of the melee combat steps, it does not exhaust your CON unless you are forced into melee.

Those with specalization in bows may perform two attacks instead of one, execept in scenario 4 when forced into melee.

There are four ranged combat scenarios:
1. Firing at a suspecting target not in melee
   - Success on 3 to 6
2. Firing into a target in melee
   - Success on 4 to 6
3. Firing at unsuspecting targets not in combat
   - Success on 3 to 6, with special damage bonuses
4. Firing at a target before being forced into melee
   - Bow or crossbow must be drawn or armed already
   - Success on 4 to 6, with special close range damage bonuses
   - No additional ranged attacks

### 1. Standard Ranged Combat
In this scenario you are firing at a target that is aware they are in combat, but they are not currently engaged in melee.

Roll a standrd 1d6 to attack, on a success of 3 to 6, roll for damage using the standard damage chart.

Apply bonuses based on you roll and wether the opponent is upright or downed.

### 2. Firing into Melee
It is not easy to fire on a target that is engaged in melee. Attack rolls suffer a -1 modifier. This means you cannot do better than a 5.

Roll a standard 1d6 with a -1 modifier, on a roll of 4 to 6, 

### 3. Unsuspecting Targets
Bows in small combat are best utilized against unsuspecting targets, therefore the damage possibilities lend themselves toward the attacker.

These bonuses are only gained if the target is *not* currently engaged in combat.

A ranged attacker makes a 1d6 check to hit their target, akin to a stand skill check.  

| Roll | Ranged Damage v. Unaware Targets | 
|------|----------------------------------|
|   1  |  Miss, target is aware of attack |
|   2  |  Miss, target remains unaware    | 
|   3  |  +1 Con Damage                   |
|   4  |  +2 Con Damage                   |
|   5  |  +1 HP, +2 Con Damage            |
|   6  |  +2 HP, +2 Con Damage            |

Only on a roll of 2 does the target remain unaware of combat
- With a long or shortbow, and weapon specialization, you may make 1 additional attack for this scenario (3) unsuspecting targets. 

On any other roll, future attack rolls fall under the other ranged combat scenarios.


### 4. Forced into Melee
When an opponent charges or attacks a player performing ranged combat, that player may make a single ranged attack.

In this scenario, players must already have their bow drawn or a crossbow armed and aiming. 

Immediatly roll a 1d6, with a success on 4 to 6. On a success roll your damage die and 1d4, determine the total damage per the standard damage chart.

Apply additional damage based on the below chart.

| Roll |   Close Ranged Damage   | 
|------|-------------------------|
|   1  |  Miss                   |
|   2  |  Miss                   | 
|   3  |  Miss                   |
|   4  |  +1 Con Damage          |
|   5  |  +1 HP, +1 Con Damage   |
|   6  |  +2 HP, +1 Con Damage   |

- If the opponent is still alive, the player is forced into melee combat with their ranged weapon as an improvised melee weapon that only deals 1d4 damage.
- If the opponent is upright, they peform a 1d6 melee attack roll and deals damage on a success.
- Players may choose to drop their ranged weapon and unsheath a melee weapon at a cost of 2 CON damage during the ensuing melee.

## Combat against Monsters and Beasts
Tactics used against against monsters and beasts are not the same as those used against a humanoid. 

The concept of an opposed check starts to fall apart when your opponent can spew acid from its mouth or swipe at you with its tail. Attacks like tripping, wrestling, and the like may apply to another humanoid, but they make far less sense against beholder or a rhinocerous. 

Therefore, to keep combat simple, when fighting a target that is not your standard humanoid, such as a  werebear, beholder, or a dragon, damage is done directly to HP and we ignore the Con aspect of combat. Essentially, you are trying to stay alive while trying to wound the beast, ideally landing a killing blow; you are not trying to overwhelm it.

### How do I know I am fighting a monster?
The basic rule of thumb is grappling, can you engage in a grappling struggle with a target and not suffer greatly? For example, would you grapple with 800lb 10 foot tall polar bear? Probably not. Would you engage in a grapple with a 7 foot 300 lb Orc? Maybe. 

## Charts

Difference Bonus

| Difference| Upright Opponent   | Downed Opponent   | 
|-----------|--------------------|-------------------|
|      5    |         1          |         2         |  
|      6    |         2          |         3         |
|      7    |         3          |         4         |
|      8    |         4          |         5         |
|      9    |         5          |         6         |
|     10    |         6          |         7         |



Damage Roll Split

| Roll | Flesh Damage | Endurance Damage |
|------|--------------|------------------|
| 1    |       0      |        1         |
| 2    |       1      |        1         |
| 3    |       1      |        2         |
| 4    |       2      |        2         |
| 5    |       2      |        3         |
| 6    |       3      |        3         |
| 7    |       3      |        4         |
| 8    |       4      |        4         |
| 9    |       4      |        5         |
| 10   |       5      |        5         |
| 11   |       5      |        6         |
| 12   |       6      |        6         |
| 13   |       6      |        6         |
| 14   |       6      |        6         |
| 15   |       6      |        6         |
| 16   |       6      |        6         |
| 17   |       6      |        6         |
| 18   |       6      |        6         |
