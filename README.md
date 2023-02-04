# Zwerchhau Combat System
![Zwerchhau](https://github.com/zaxor0/zwerchhau/blob/main/zwerchhau.png)

Combat in Zwerhhau is meant to be swift, deadly, and decisive. 

It is a ritual well practiced by adventurers.

The goal is this system is to change combat in old school RPG systems; ideally, it will provide a means for more tactical combat with more interesting choices for fighter types.

Idea for a fully fleshed out RPG system are in the ![System](https://github.com/zaxor0/zwerchhau/blob/main/system.md)
## Initiave and Turn Order
1. Players delcare actions and intentions.
2. DM decribes NPC actions and intentions, where necessary.
3. Each side rolls 1d6, highest goes first, roll again in a tie.
4. Resolve actions for the winning side.
5. The losing side gets actions per individual not involved in an opposed check or in defensive fighting.

Those casting spells are considered performing "dodge" with a "disengage" posture unless otherwise declared. 

## Melee Combat Loop
Melee combat is exhausting, each round requires that the sides engaged lose 2 Constitution.

- Declare engagement posture
- Determine Player's Attacking Combat Action
- DM Rolls for NPC's action
- Determine the opposed check based on results (dex, str, or both)
- Opposed Roll - Add the relevant ability (dex, str)
  - Highest wins, note winner's value, reroll on equal values. 
- Damage Roll - Winner rolls their weapon's damage dice
  - Reduce HP damage based on armor
  - Check for death
  - Apply damage bonuses
- Reduce Constituion Points, 2 per round of combat
  - If player is wearing heavy armor and unskilled, reduce CON by 1 further. 

### Engagement Posture
In the thick of combat, the blows may turn to a grapple. Prior to attack players may choose their default posture, to engage in grapple or to disengage. 

If their default posture is to disengage, they gain a +1 on grappling DEX checks, but do not enter the grapple if they win.

### Combat Actions
Players decide which type of attack based on the following:

- Thrusts: Piercing actions
  - Additional damage (+1 Con) for 1h spears
  - Additional damage (+2 Con) for 2h spears
  - Additional damage (+1 HP) for 2h swords
- Slashes / Cuts: Swinging & slicing actions
  - Additional damage (+2 Con) for any medium, long, two-handed, or great weapon
  - Additional damage (+1 Con) for blunt great weapons
  - Additional damage (+1 HP) for sharp-edged great weapons
- Parries: blocking the blow of a weapon with your weapon
  - An opposed roll of natural 6 allows for a riposte
  - Gain +1 to your roll if you have a shield
- Ripostes: a free follow up attack after a parry opposed roll of 6, half damage
  - With weapon specialization, does normal damage
- Dodges: evading an attack with quick movement
  - Allow for bonus to escape
- Grapples: clinging to your opponent to attempt a wrestling maneuvre, with or without your weapon
  - Single-sided grapple attempts take half damage on failed DEX checks
  - Throw the opponent to the ground, greatly decreases opponent defenses, ideal action for a swift kill
  - Disarm the opponent, ideal to force an opponent to yield, 1d6 skill check
  - Sleeperhold, attempt to force the opponent to passout; if successful, you are occupied for 3 turns and are unable to defend yourself
- Defensive Fighting: Focusing on parries without ripostes, regaining footing when downed. See the below section.

### NPC Combat Attack Roll
One d6 die roll representing the following actions

| Roll | Slashing | Thrusting or Slashing |  Thrusting   |
|------|----------|-----------------------|--------------|
|   1  |  DM Pick |       DM Pick         |  DM Pick     |  
|   2  |  Parry   |       Parry           |  Parry       |
|   3  |  Slash   |       Thrust          |  Thrust      |
|   4  |  Slash   |       Slash           |  Thrust      |
|   5  |  Dodge   |       Dodge           |  Dodge       |
|   6  |  Grapple |       Grapple         |  Grapple     |

### Combat Attack Results
The priorty table to determine result check:

|Priority | Opposing Rolls      | Check        |
|---------|---------------------|--------------|
|   1     | Grapple v. Grapple  | Str          |
|   2     | Grapple v. Any      | Dex then Str |
|   3     | Dodge v. Any        | Dex          |
|   4     | Slash v. Any        | Dex or Str   |
|   5     | Thrust v. Thrusts   | Dex          |
|   6     | Parry v. Thrusts    | Str          |
|   7     | Others              | No Result    | 

A table view of the same information:

|       |Cut  |Thrust|Parry|Dodge|Grapple|
|-------|-----|------|-----|-----|-------|
|Slash  | DvS | DvS  | DvS | Dex | D&S   |
|Thrust | DvS | Dex  | Str | Dex | D&S   |
|Parry  | DvS | Str  | nil | nil | D&S   |
|Dodge  | Dex | Dex  | nil | nil | D&S   |
|Grapple| D&S | D&S  | D&S | D&S | Str   |

### Opposed Checks
Once you've determined which check will occur, whether strength or dex (or none at all), each side rolls 1d6 + their attribute.

The higher value wins the check and deals damage. 

To succeed in a grapple check, you must first win a dex check to wrestle your opponent, and then a strength check to enter the grapple phase. If both sides attempt a grapple, you only need the strength check.

Opponents attacking someone performing "defensive fighting" still roll, but only "hit" on a 6. See below for more detail.

### Damage Dealt
Damage is dealth based on the die roll of the appropriate weapon; however, damage is split between flesh / HP and Constitution.

| Roll | HP Damage | CON Damage |
|------|-----------|------------|
| 1    |     0     |     1      |
| 2    |     1     |     1      |
| 3    |     1     |     2      |
| 4    |     2     |     2      |
| 5    |     2     |     3      |
| 6    |     3     |     3      |
| 7    |     3     |     4      |
| 8    |     4     |     4      |
| 9    |     4     |     5      |
| 10   |     5     |     5      |
| 11   |     5     |     6      |
| 12   |     6     |     6      |

- Damage to HP (flesh and blood) is always dealt first.
- If HP damage brings the player character **below 0 hit points**, they are dead.
- If a player character takes damage that brings them to **exactly zero hit points**:
  - Perform the *Will to Live* roll to see if they survive.
  - Do not process any additional damage
- If a player is **above zero hit points**, add damage bonuses.
- If after damage bonuses the player is **at or below zero HP**, they are dead.

### The Will to Live

1. Make a 1d12 *Will to Live* roll. If the player rolls equal to or under thier Will ability score, they are not dead.
2. Next, they must roll on the *Scars, Broken Bones, and Mortal Wounds* table below.
3. The must roll a 1d6, add the result to their maximum HP. 
4. The player character is still at 0 HP but are unconscious.
5. Ignore any damage bonuses, they are out of the fight.
6. Without medical aid soon, they will die.

#### Scars, Broken Bones, and Mortal Wounds

Roll 1d6 
- On a 1-2 you gain a scar
- On a 3-5 you have a broken bone
- On a 6 you have a mortal wound, you will die unless untreated. 

Roll 1d4, see where you have been wounded.

|1d4| Scars (1,2) | Broken Bones (3,4,5) |  Mortal Wounds (6) |
|---|-------------|----------------------|--------------------|
| 1 |   Facial    |     Skull            |    Lose an Eye     |
| 2 |   Chest     |     Ribs             |    Punctured Organ |
| 3 |   Arm       |     Arm              |    Lose an arm     |
| 4 |   Leg       |     Leg              |    Lose a leg      |

### Damage Bonuses
Based on the opposed die roll, the victor may deal additional damage to their opponent, to either their HP (flesh and blood) or to their CON (thier overall endurance)

| Roll | Upright Opponent   | Downed Opponent   | 
|------|--------------------|-------------------|
|   1  |  nil               | nil               | 
|   2  |  nil               | +1 Con damage     | 
|   3  |  nil               | +1 Con Damage     | 
|   4  |  +1 Con Damage     | +2 Con Damage     | 
|   5  |  +2 Con Damage     | +1 HP, +1 Con Dmg | 
|   6  |  +1 HP, +1 Con Dmg | +2 HP, +2 Con Dmg | 

#### Attack type bonuses
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
Defensive Fighting occurs in place of an opposed roll. Opponents land hits only on 6s and additional opponents gain bonuses to hit. Players should consider this choice when they need to perform the following:

- Keep enemies at bay
- Parry incoming attacks
- Avoid being encircled
- Regain footing after being knock down, lose 1 CON

#### Actions for opponents
- Hit the defensive fighter only on a 6
- Do not gain damage bonuses if alone
- For each additional opponent attacking, each attacker gains a +1 to their roll with a maximum of +3. 
- If there are 3 or more opponents attacking the defensive fighter, they deal +1 CON damage each.

### Dodge
On a succesful dodge roll a player suffers no damage from a single attack. Ideally used in 1 on 1 scenarios, otherwise defensive fighting is recommended.

- If there is more than 1 opponent, a player must declare who they are dodging, if there is more than 1 opponent. 
- If they succeed on a 5 or 6, they may attempt to escape if there is a viable route to retreat. 
- On a success and for each additional opponent, they must expend 1 CON to continue dodging with a maximum of 3 CON.
- If there are multiple opponents, and the player cannot expend Constitution, opponents land hits on 5s and 6s.

Those performing spellcasting are considering taking a dodge action in case they are attacked. If an opponent attacks them and the lose the opposed check (dex) the spell fails. 

### Grappling and Wrestling
#### One Sided Grapple Attempts
If only one combatant attempts a grapple, there are two checks:

- First dexterity, this represents the lunge or springing action an attacker would make to quickly close distance before a strike is made against them. Also, is represents the opponent swinging their weapon or moving away from the grappler. 
- Upon failure: If the opposing side performed a *thrust* or *slash*, take damage.
- Upon success: A standard opposed strength check to see who dominates.

#### Grapple Strength Check
If both sides are performing a grapple, each side rolls 1d6 & add their strength, winner performs a wrestling maneuvre.

- Disarm the opponent: Attempt to remove the opponent's weapon, this is ideal for forcing a yield, requires a 1d6 skill check 
- Throw the opponent to the ground: Drastically reduce an opponents defensive capabilities by forcing them into a prone position, this is ideal for a swift kill.
- Sleeperhold: Attempt to force the opponent to passout; if successful, you are occupied for 3 turns and are unable to defend yourself, requires a 1d6 skill check.

These maneurves are the sort of thing a warrior would want to have "skills" in, giving them an "advantage roll."

#### Relevanti Grappling Skills
- Grappling: +1 to engagement on grappling STR checks 
- Wrestling throws: +2 CON damage (instead of none)
- Disarming: Advantage on disarm checks

### Riposte
If a player rolled a parry versus a slash or thrust, and they win the opposed check with a natural roll of 6, may riposte.

A riposte is follow up to a successful parry that allows for a damage roll halved; with weapon specailization, normal damage is dealt.

A parry roll of 5 with a +1 for a shield does not allow for a riposte, the roll must be a natural 6.

### Small Sized Combatants
This mainly applies to half sized humanoids (halflings, gnomes, kobolds, etc.) fighting medium sized humanoids (humans, dwarves, elves, etc). 

If you are of this "small" size fighting a medium sized opponent:

- Any constitution damage you deal is halved. This *does not* apply to flesh damage to HP. 
- You receive advantage during grappling if your posture is to disengage.

For example, a halfling equipped with a two-handed long sword should be able to land a lethal blow on a human; however, due to their relative strength, they are unlikely to "wear down" the physical endurance of someone twice their size. Additionally, being small often tends to increase nimbleness and agility, therefore the "small" sized combatant is better suited to escape a grapple.

These advantages do not scale beyond small versus medium opponents.

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

# Saving Throws and Ability Checks
- Saves are rolled as a 1d6 and determined to be a success based on the standard 1d6 skill check. 
- Those with a stat of 6 in a given ability score gain a +1 bonus to the save
- Those with who, at the time of the roll, have a 15 or higher Constitution gain +1 to the save.
- Some racial abilities give a +1 bonus, these do not stack. You only ever get +1.

## Saves and Checks Table
These are example to help categorize saves that need to be made during gameplay.

| Strength                    | Dexterity     | Will   | Constitution         | 
|-----------------------------|---------------|--------|----------------------|
| Catch falling person        | Breath Weapon | Spells | Poison               |
| Knock charging monster      | Dodge         | Wands  | Paralysis            |
| Stand ground against charge | Avoid falling | Sleep  | Toxic Substances     |
|                             |               | Charm  | Extreme cold or heat | 
