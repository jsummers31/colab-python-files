
def BattleSequence(player, enemyList):
    print("Battle Start")
    while(player.health != 0 and len(enemyList) != 0):
        
        userAction = actionMenu()
        
        if userAction == '1':
            userWeapon, userTarget = atkMenu(player, enemyList)
            enemyList[userTarget].health -= player.weapons[userWeapon]
            print(f"Dealt {player.weapons[userWeapon]} damage to {enemyList[userTarget].name}")

            if(enemyList[userTarget].health <= 0):
                del enemyList[userTarget]

            enemyTurn(player, enemyList)

        elif userAction == '2':
            dispInventory(player)
            
        elif userAction == '3':
            dispStatus(player, enemyList)

    return True
            

def actionMenu():
    return input("""Select Action:
1: Attack
2: Inventory
3: Status
""")

def atkMenu(player, enemyList):
    print("Select Weapon:")
    print(player.weapons)
    weapon = input()

    print("Select Enemy:")
    for i, enemy in enumerate(enemyList, start = 1):
        print(f"{i}: {enemy.name}, Health = {enemy.health}")
    target = int(input()) - 1

    return weapon, target

def dispInventory(player):
    print("Inventory:")
    print(player.inventory)

def dispStatus(player, enemyList):
    print(f"Player Health: {player.health}")
    print("Enemy Health:")
    for enemy in enemyList:
        print(f"{enemy.name}, Health = {enemy.health}")

def enemyTurn(player, enemyList):
    for enemy in enemyList:
        print(f"{enemy.name} dealt {enemy.attack} damage")
        player.health -= enemy.attack


if __name__ == "__main__":

    class player:
        def __init__(self):
            self.health = 100
            self.weapons = {"sword" : 10, "bow" : 5}
            self.inventory = {"potion" : 2}

    class enemy:
        def __init__(self):
            self.name = "Goblin"
            self.health = 10
            self.attack = 3

    plyr = player()

    attackingParty = [enemy(), enemy(), enemy()]

    BattleSequence(plyr, attackingParty)

    print("done")
