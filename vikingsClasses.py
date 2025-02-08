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
        return None
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    

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
            return f"A Saxon has died in combat"
        else:
            return f"A Saxon has received {damage} points of damage"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
       self.vikingArmy.append(viking) 
       return None
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon) 
        return None   
    
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        estado = saxon.receiveDamage(viking.strength)

        if saxon.health <= 0: 
            self.saxonArmy.remove(saxon)
        return estado
    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        estado = viking.receiveDamage(saxon.strength)

        if viking.health <= 0: 
            self.vikingArmy.remove(viking)
        return estado


    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!" 
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    pass

#yop
class War2:

    def __init__(self):
        pass 

    def addViking(self, Viking):
        pass
    
    def addSaxon(self, Saxon):
        pass
    
    def vikingAttack(self):
        pass

    def saxonAttack(self):
        pass

    def showStatus(self):
        pass

    pass


