import random as r
def spawnEnemy(difficulty):
    opponents = []
    if difficulty == "easy":
        print("easy")
        numEnemies = r.randint(1,3)
        for i in range(numEnemies):
            opponents.append(r.choice([Slime(), Goblin()])) 
        return opponents
    elif dificulty == "normal":
        print("normal")
    else:
        print("hard")

class Enemy:
    def attackDmg(self):
        return self.damage()

class Slime(Enemy):
    def __init__(self):
        self.name = "Slime"
        self.health = random.randint(2,4)

    def damage(self):
        attack = r.randint(1,3)
        return attack

class Goblin(Enemy):
    def __init__(self):
        self.name = "Goblin"
        self.health = r.randint(5,7)

    def damage(self):
        attack = r.randint(2,4)
        return attack



if __name__ == "__main__":
    import random as r

    userIn = input("Generate an attacking party? ")

    while userIn.lower() == 'y':

        opp1 = spawnEnemy("easy")

        print("Attacking Party:")
        for enemy in opp1:
            print(enemy.name)

        print('')

        for enemy in opp1:
            print(f"{enemy.name} dealt {enemy.attackDmg()} damage")

        userIn = input("Generate a new attacking party? ")

    print("okay :(")

    
