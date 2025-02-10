import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health= health
        self.strength=strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage=damage
        self.health -= damage

     
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        self.health= health
        self.strength=strength

    def attack(self):
        return self.strength

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health>0 :
            return "{self.name} ha recibido {self.damage}} puntos de daño"
        else :
            return "{self.name} ha muerto en acto de combate"

        


# Saxon

class Saxon(Soldier):
     def __init__(self, health, strength):
        self.health = health
        self.strength = strength


     def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f"Un 'Saxon' ha recibido {damage} puntos de daño"
        else:
            return f"Un 'Saxon' ha muerto en combate"
# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        
        result = random_saxon.receiveDamage(random_viking.attack())
    
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
            print(f"VIKING | I am deleting random_saxon, Health:{random_saxon.health}, Strength: {random_saxon.strength}")

        return result
    def saxonAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        
        result = random_viking.receiveDamage(random_saxon.attack())

        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
            print(f"SAXON | I am deleting viking {random_viking.name}, Health:{random_viking.health}, Strength: {random_viking.strength}")
            
        return result


    def showStatus(self):
        if len(self.saxonArmy) < 1:
            return "¡Los Vikingos han ganado la guerra del siglo!"
        elif len(self.vikingArmy) < 1:
            return "Los Sajones han luchado por sus vidas y sobreviven otro día..."
        else:
            return  "Los Vikingos y los Sajones todavía están en plena batalla."

    pass
