import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health=health
        self.strength=strength
    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health,strength)
        self.name=name


    def battleCry(self):
        # your code here
        return f"Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health,strength)

    def attack(self):
        # your code here
        return self.strength        

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"        

# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        self.viking=viking
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # your code here
        self.saxon=saxon
        self.saxonArmy.append(saxon)

    
    def vikingAttack(self):
        # your code here
        saxon=random.choice(self.saxonArmy)
        viking=random.choice(self.vikingArmy)
        
        result_viking_attack=saxon.receiveDamage(viking.strength)
        if saxon.health<=0:
            self.saxonArmy.remove(saxon)
        
        return result_viking_attack
    
    def saxonAttack(self):
        # your code here
        saxon=random.choice(self.saxonArmy)
        viking=random.choice(self.vikingArmy)
        
        result_saxon_attack=viking.receiveDamage(saxon.strength)
        if viking.health<=0:
            self.vikingArmy.remove(viking)
        
        return result_saxon_attack

    def showStatus(self):
        # your code here
        if len(self.saxonArmy)==0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return f"Saxons have fought for their lives and survive another day..."
        else: 
            return f"Vikings and Saxons are still in the thick of battle."
    #pass

#yop
#class War2:

    #def __init__(self):
        # your code here

    #def addViking(self, Viking):
        # your code here
    
    #def addSaxon(self, Saxon):
        # your code here
    
    #def vikingAttack(self):
        # your code here

    #def saxonAttack(self):
        # your code here

    #def showStatus(self):
        # your code here

    #pass


