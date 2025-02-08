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
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        # your code here
        return "Odin Own You All"

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has died in act of combat!"
        else:
            return f"{self.name} has received {damage} points of damage."


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)


    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health <= 0:
            return f"Saxon has died in battle."
        else:
            return f"Saxon has received {damage} points of damage."

# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
        if self.vikingArmy and self.saxonArmy:
            viking = random.choice(self.vikingArmy)
            saxon = random.choice(self.saxonArmy)
            result = saxon.receiveDamage(viking.attack())
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
                return result
            
        
    
    def saxonAttack(self):
        # your code here
        import random
        if self.saxonArmy and self.vikingArmy:
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            result = viking.receiveDamage(saxon.attack())
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
                return result

    def showStatus(self):
        # your code here
        if not self.saxonArmy:
            return "Vikings have won the war"
        elif not self.vikingArmy:
            return "Saxons have fought for their loves and survived another day"
        else:
            return "Vikings and Saxons are still in the thick of the battle"
        

#yop
class War2:

    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, Viking):
        # your code here
        self.vikingArmy.append(Viking)

    
    def addSaxon(self, Saxon):
        # your code here
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        # your code here
        if self.vikingArmy and self.saxonArmy:
            viking = random.choice(self.vikingArmy)
            saxon = random.choice(self.saxonArmy)
            result = saxon.receiveDamage(viking.attack())
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
                return result
            
    
    def saxonAttack(self):
        # your code here
        if self.saxonArmy and self.vikingArmy:
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            result = viking.receiveDamage(saxon.attack())
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
                return result
            

    def showStatus(self):
        # your code here
        if not self.saxonArmy:
            print("Vikings have won the war")
        elif not self.vikingArmy:
            print("Saxons have fought for their lives and survived another day")
        else:
            print("Vikings and Saxons are still in the thick of the battle")

        print(f"Viking army: {len(self.vikingArmy)}")
        print(f"Saxon army: {len(self.saxonArmy)}")
        if self.vikingArmy:
            print(f"Viking health: {self.vikingArmy[0].health}")
        if self.saxonArmy:
            print(f"Saxon health: {self.saxonArmy[0].health}")
        



