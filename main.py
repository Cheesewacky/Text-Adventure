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
player.abilities.extend((s.abilities['Fireball'], s.abilities['Life Siphon'], s.abilities['Ice Bolt']))


print(player.abilities)
func.showAbilities(player)

print("\n")
player.cast(enemy, player.abilities[0])