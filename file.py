import vikingsClasses, random as rand

def main():
    war = vikingsClasses.War()
    war.saxonArmy = []
    war.vikingArmy = []
    soldiers = [
        "Hermenegildo",
        "Crescencio",
        "Abundio",
        "Telesforo",
        "Policarpo",
        "Gumersindo",
        "Casimiro",
        "Anacleto",
        "Petronila",
        "Escolástica",
        "Hermenegilda",
        "Purificación",
        "Encarnación",
        "Remedios",
        "Sinforosa"
    ]

    for soldier in soldiers:
        if rand.randint(0, 1):
            war.addSaxon(vikingsClasses.Saxon(rand.randint(60, 100), rand.randint(25, 50)))
        else:
            war.addViking(vikingsClasses.Viking(soldier, rand.randint(100, 200), rand.randint(10, 30)))

    while len(war.saxonArmy) > 0 and len(war.vikingArmy) > 0:
        print(war.showStatus())
        if rand.randint(0, 1):
            print(war.vikingAttack())
        else:
            print(war.saxonAttack())

    print(war.showStatus())

if __name__ == "__main__":
    main()