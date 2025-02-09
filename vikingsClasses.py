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
    

    def attack(self):
        return("Odin Owns You All!") 

    def battleCry(self):
        return("¡Odin os posee a todos!")

    def receiveDamage(self, damage):
        self.health -=damage
        if self.health > 0:
            return f"{self.name} ha recibido {damage} puntos de daño"
        else:
            return f"{self.name} ha muerto en acto de combate"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -=damage
        if self.health > 0:
            return f"Un Saxon ha recibido {damage} puntos de daño"
        else:
            return f"Un Saxon ha muerto en acto de combate"

    def attack(self, strength):
        self.strength = strength

# Davicente
class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.vikingArmy.append(saxon)
    
    def vikingAttack(self):
        if self.saxonArmy and self.vikingArmy:
            attacking_vicking = random.choice(self.vikingArmy)
            defending_saxon = random.choice(self.saxonArmy)

            result = defending_saxon.receiveDamage (attacking_vicking.attack())

            if defending_saxon.health <= 0:
                self.saxonArmy.remove(defending_saxon)
            
            return result    
    
    def saxonAttack(self):
        if self.saxonArmy and self.vikingArmy:
            attacking_saxon = self.saxonArmy [0]
            defending_viking = self.vikingArmy [0]

            result = defending_viking.receiveDamage (attacking_saxon.attack())

            if defending_viking.health <= 0:
                self.vikingArmy.remove(defending_viking)

            return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Los Vikingos han ganado la guerra del siglo!"
        elif len(self.vikingArmy) == 0:
            return "Los Sajones han luchado por sus vidas y sobreviven otro día..."
        else:
            return "Los Vikingos y los Sajones todavía están en plena batalla."
    pass

