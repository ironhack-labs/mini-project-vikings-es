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


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        active_viking = random.choice(self.vikingArmy)
        active_saxon = random.choice(self.saxonArmy)
        result = active_saxon.receiveDamage(active_viking.strength)

        # removes it from the army if it dies.
        if active_saxon.health <= 0:
            self.saxonArmy.remove(active_saxon)

        return result

    def saxonAttack(self):
        active_viking = random.choice(self.vikingArmy)
        active_saxon = random.choice(self.saxonArmy)
        result = active_viking.receiveDamage(active_saxon.strength)
        if active_viking.health <= 0:
            self.vikingArmy.remove(active_viking)
        return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
