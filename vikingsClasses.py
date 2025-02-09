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
        self.health-= damage

    

# # Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)
        self.name=name


    def battleCry(self):
        # your code here
        return "Odin Owns You All!"
        

    def receiveDamage(self, damage):
        # your code here
        super().receiveDamage(damage)
        self.damage=damage
        self.health-=self.damage
        if self.health>0:
            return f'{self.name} has received {self.damage} points of damage'
        elif self.health<=0:
            return f'{self.name} has died in act of combat'
        

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health,strength)

    def receiveDamage(self, damage):
        #super().receiveDamage(damage)
        # your code here
        self.damage=damage
        self.health-=self.damage
        if self.health>0:
            return f'A Saxon has received {self.damage} points of damage'
        elif self.health<=0:
            return f'A Saxon has died in combat'
# # Davicente

class War:
    def __init__(self):
        # your code here
        self.vikingArmy=[]
        self.saxonArmy=[]
    def addViking(self, Viking):
        # your code here
        self.vikingArmy.append(Viking)
  
    def addSaxon(self, Saxon):
        # your code here
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        # your code here
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        viking=random.choice(self.vikingArmy)
        saxon=random.choice(self.saxonArmy)
        saxon_damage=saxon.receiveDamage(viking.strength)

        if saxon.health<=0:
            self.saxonArmy.remove(saxon)
            return saxon_damage

        
    
    def saxonAttack(self):
        # your code here
        if len(self.vikingArmy)==0:
            return "Vikings have won the war of the century!"
        viking=random.choice(self.vikingArmy)
        saxon=random.choice(self.saxonArmy)
        viking_damage=viking.receiveDamage(saxon.strength)
        

        if viking.health<=0:
            self.vikingArmy.remove(viking)
            return viking_damage
        return f"{viking.name} has received {saxon.strength} points of damage"



    def showStatus(self):
        # your code here
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        

        pass

# #yop
# class War2:

#     def __init__(self):
#         # your code here

#     def addViking(self, Viking):
#         # your code here
    
#     def addSaxon(self, Saxon):
#         # your code here
    
#     def vikingAttack(self):
#         # your code here

#     def saxonAttack(self):
#         # your code here

#     def showStatus(self):
#         # your code here

#     pass