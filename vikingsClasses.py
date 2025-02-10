import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength
    
    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health-=damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        self.name = name
        super().__init__(health, strength)

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"
    
    def receiveDamage(self, damage):
        # your code here
        self.health-=damage
        if self.health > 0:
            return f"{self.name} ha recibido PUNTOS DE DAÑO {damage}"
        else:
            return f"{self.name} ha muerto en acto de combate"
              

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health <= 0:
            return f"A Saxon has died in combat"
        else:
            return f"A Saxon has received {damage} points of damage"

# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking) 
        return None
    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon) 
        return None 
    
    def vikingAttack(self):
        # your code here
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        estado = saxon.receiveDamage(viking.strength)

        if saxon.health <= 0: 
            self.saxonArmy.remove(saxon)
        return estado
    
    def saxonAttack(self):
        # your code here
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        estado = viking.receiveDamage(saxon.strength)

        if viking.health <= 0: 
            self.vikingArmy.remove(viking)
        return estado

    def showStatus(self):
        # your code here
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
        # your code here
        pass

    def addViking(self, Viking):
        # your code here
        pass
    
    def addSaxon(self, Saxon):
        # your code here
        pass
    
    def vikingAttack(self):
        # your code here
        pass

    def saxonAttack(self):
        # your code here
        pass

    def showStatus(self):
        # your code here
        pass

    pass


