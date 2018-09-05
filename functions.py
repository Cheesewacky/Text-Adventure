"""
Functions for the Text Adventure
"""
import random as r
import world as w


# Setting up some basic functions for the game
def isCriticalStrike(chance):
    """
    :param chance:
    :return isCritical:

    Takes in the Parameter 'chance' and returns the boolean isCritical
    Compares 'chance' to a random float between 0 and 1 to determine isCritical
    """
    # The check variable is a random number between 0 and 1
    # 'check' will be compared to the critical strike variable 'chance'
    # If 'check' is less than or equal to 'chance' the hit is a critical
    check = r.random()
    if check <= chance:
        isCritical = True
        return isCritical
    else:
        isCritical = False
        return isCritical


def moveTile(currentTile, direction):
    """
    :param currentTile:
    :param direction:

    Takes the tile the player is currently at and moves the player
    based on the direction they choose.
    """
    if direction == 'west':
        if w.world[currentTile - 1] == 1:
            print("A wall blocks your path. You can't go that way.")
            return currentTile
        else:
            currentTile -= 1
            biome = w.world[currentTile]
            print("You move to the west.")
            print("You are in the " + str(w.biomes[biome]))
            return currentTile

    elif direction == 'east':
        if w.world[currentTile + 1] == 1:
            print("A wall blocks your path. You can't go that way.")
            return currentTile
        else:
            currentTile += 1
            biome = w.world[currentTile]
            print("You move to the east.")
            print("You are in the " + str(w.biomes[biome]))
            return currentTile

    elif direction == 'north':
        if w.world[currentTile - 20] == 1:
            print("A wall blocks your path. You can't go that way.")
            return currentTile
        else:
            currentTile -= 20
            biome = w.world[currentTile]
            print("You move to the north.")
            print("You are in the " + str(w.biomes[biome]))
            return currentTile

    elif direction == 'south':
        if w.world[currentTile + 20] == 1:
            print("A wall blocks your path. You can't go that way.")
            return currentTile
        else:
            currentTile += 20
            biome = w.world[currentTile]
            print("You move to the south.")
            print("You are in the " + str(w.biomes[biome]))
            return currentTile


def levelUp(self):
    """
    Causes the player to go up in level, keeping any xp over the limit
    This will also increase the player's stats by a small amount
    """
    self.currentLevel += 1
    self.currentXP = self.currentXP - self.xpToLevel
    self.xpToLevel = 250 * self.currentLevel
    self.stamina += 2
    self.defense += 1
    self.strength += 1
    self.intelligence += 1


def showAbilities(self):
    """
    Prints the players abilities
    """
    abilityList = []
    for ability in self.abilities:
        abilityList.append(ability)
    print(abilityList)


def getInput():
    print("\nWhat do you want to do?")
    try:
        answer = str(input(">").lower())
    except TypeError:
        print("Invalid Input.")
    answer = answer.split()
    return answer


def turn(self, other):
    inputOne, inputTwo = getInput()
    if inputOne == 'move':
        pass