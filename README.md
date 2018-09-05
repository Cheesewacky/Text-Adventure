# Text Adventure

## A Little Learning Project for Myself

I'm learning how to use github and introducing myself to object oriented programming.

I've split this text adventure up into different modules

Most of the names are self explanatory, but I'll describe them anyway.

```
Classes:
    All the base classes that I use will be in this file
    The Classes are as follows:
        Enemy
        Player
        Item

-Functions:
    Contains other functions that I need outside of the classes
    The Functions are as follows:
        isCriticalStrike - calculates if a hit is a critical strike or not
        moveTile - moves the player around the world
        levelUp - moves the player up a level, increasing the player's stats as well
        showAbilities - lists the player's abilities
        getInput - takes the player's input and splits it up
        turn - defines how the player can interact with everything

-Spells:
    Holds all the spells and information such as damage and mana cost

-World:
    Holds all information on the map and the biome of each tile

-Main:
    Used for testing right now, but will eventually be where the game starts and ends
    Will add in a way for players to save and continue characters

Misc:
    Nothing at the moment. Hopefully I won't use
```

