"""
Text Adventure Classes
"""

import functions as func
import random as r
import spells as s

# Defining the base Enemy class
# This is also going to be the class bosses inherit from
class Enemy:
    def __init__(self, name, health, mana, strength, defense, species, xp):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.defense = defense
        self.species = species
        self.xp = xp
        self.abilities = []
        self.loot = []

    def attack(self, other):
        damage = self.strength - other.defense
        other.health -= damage
        print(self.name + " attacks the " + other.name + " for " + str(damage) + " damage!")

    def block(self, other):
        defense = self.defense * 1.5
        damage = other.strength - defense
        print(other.name + " attacks the " + self.name + " for " + str(damage) + " damage!")


class Boss(Enemy):
    def __init__(self, name, health, mana, strength, defense, species, xp):
        super().__init__(name, health, mana, strength, defense, species, xp)
        self.abilities = []
        self.loot = []

    def attack(self, other):
        damage = self.strength - other.defense
        other.health -= damage
        print(self.name + " attacks the " + other.name + " for " + str(damage) + " damage!")


# Defining the Player Class
class Player:
    def __init__(self, name, currentHealth, health, currentMana, mana, strength, stamina, intelligence, defense, criticalChance,
                 xpToLevel, currentXP, currentLevel):
        self.name = name
        self.currentHealth = currentHealth
        self.health = health
        self.currentMana = currentMana
        self.mana = mana
        self.strength = strength
        self.stamina = stamina
        self.intelligence = intelligence
        self.defense = defense
        self.criticalChance = criticalChance
        self.xpToLevel = xpToLevel
        self.currentXP = currentXP
        self.currentLevel = currentLevel
        self.abilities = []
        self.inventory = []

    def __str__(self):
        return "\nName: {}\nCurrent Health: {}\nMax Health: {}\nCurrent Mana: {}\nMax Mana: {}\nStrength: " \
               "{}\nStamina: {}\nIntelligence: {}\nDefense: {}\nCrit Chance: {}%\nXP to Level: {}\nXP: {}\nLevel: {}"\
            .format(
                self.name, str(self.currentHealth), str(self.health), str(self.currentMana),
                str(self.mana), str(self.strength), str(self.stamina), str(self.intelligence),
                str(self.defense), str(self.criticalChance), str(self.xpToLevel),
                str(self.currentXP), str(self.currentLevel))

    def attack(self, other):
        isCritical = func.isCriticalStrike(self.criticalChance)
        damage = r.randrange(self.strength - 2, self.strength + 2) - other.defense
        if isCritical:
            damage = damage * 2
            other.health -= damage
            print("\nThe attack is a critical strike!")
            print(self.name + " attacks the " + other.name + " for " + str(damage) + " damage!")
        else:
            other.health -= damage
            print("\n" + self.name + " attacks the " + other.name + " for " + str(damage) + " damage!")

    def cast(self, other, spell):
        abilityList = []
        for ability in s.abilities:
            abilityList.append(ability)
        print(self.name + " casts " + abilityList[spell] + "!")
        isCritical = func.isCriticalStrike(self.criticalChance)
        damage = r.randrange(s.abilityDamage[spell] - 2, s.abilityDamage[spell] + 2) - other.defense
        if isCritical:
            damage = damage * 2
            other.health -= damage
            print("\nThe spell is a critical hit!")
            print("The spell hits for " + str(damage) + " damage!")
        else:
            other.health -= damage
            print("The spell hits for " + str(damage) + " damage!")

    def block(self, other):
        defense = self.defense * 1.5
        damage = other.strength - defense
        print(other.name + " attacks the " + self.name + " for " + str(damage) + " damage!")


# Defining the Item class
class Item:
    def __init__(self, name, strength, stamina, mana, intelligence, health, defense, value):
        self.name = name
        self.strength = strength
        self.stamina = stamina
        self.mana = mana
        self.intelligence = intelligence
        self.health = health
        self.defense = defense
        self.value = value
