import classes
import functions as func
import world as w
import spells as s
import time as t

player = classes.Player("Player", 90, 100, 100, 150, 15, 20, 25, 20, .99, 250, 0, 1)
enemy = classes.Enemy("Enemy", 100, 150, 5, 10, "Goblin", 150)
boss = classes.Boss("Boss", 150, 200, 20, 0, "Demon", 250)

currentTile = 21

player.inventory.extend(('gold', 'rusty knife', 'health potion'))
player.abilities.extend((s.abilities[0], s.abilities[1], s.abilities[4]))


#print(player)
#player.currentXP = 324
#func.levelUp(player)
#print(player)

abilityOne = s.abilityDamage[0]
print(abilityOne)
print(abilityOne[0])
print(abilityOne[1])