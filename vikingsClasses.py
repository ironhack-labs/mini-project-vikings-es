import random


# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage


# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has received {damage} points of damage"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health <= 0:
            return f"A {Saxon.__name__} has died in combat"
        else:
            return f"A {Saxon.__name__} has received {damage} points of damage"

# # Davicente
#
# class War():
#     def __init__(self):
#         # your code here
#
#     def addViking(self, viking):
#         # your code here
#
#     def addSaxon(self, saxon):
#         # your code here
#
#     def vikingAttack(self):
#         # your code here
#
#     def saxonAttack(self):
#         # your code here
#
#     def showStatus(self):
#         # your code here
#     pass
#
# class War2:
#
#     def __init__(self):
#         # your code here
#
#     def addViking(self, Viking):
#         # your code here
#
#     def addSaxon(self, Saxon):
#         # your code here
#
#     def vikingAttack(self):
#         # your code here
#
#     def saxonAttack(self):
#         # your code here
#
#     def showStatus(self):
#         # your code here
#
#     pass
