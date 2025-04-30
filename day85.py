import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack_power = 20
        self.healing_potions = 3

    def attack(self, enemy):
        damage = random.randint(10, self.attack_power)
        enemy.hp -= damage
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")

    def heal(self):
        if self.healing_potions > 0:
            heal_amount = random.randint(15, 30)
            self.hp += heal_amount
            self.healing_potions -= 1
            print(f"{self.name} uses a healing potion and restores {heal_amount} HP.")
        else:
            print("No healing potions left!")

class Enemy:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, player):
        damage = random.randint(5, self.attack_power)
        player.hp -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage!")

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!\n")
    while enemy.hp > 0 and player.hp > 0:
        print(f"\n{player.name} HP: {player.hp} | {enemy.name} HP: {enemy.hp}")
        print("1. Attack\n2. Heal\n3. Run")
        choice = input("Choose your action: ")

        if choice == "1":
            player.attack(enemy)
        elif choice == "2":
            player.heal()
        elif choice == "3":
            print(f"{player.name} runs away!")
            return False
        else:
            print("Invalid choice!")
            continue

        if enemy.hp > 0:
            enemy.attack(player)

    if player.hp <= 0:
        print(f"\n{player.name} has been defeated!")
        return False
    elif enemy.hp <= 0:
        print(f"\n{enemy.name} has been defeated!")
        return True

def main():
    name = input("Enter your character's name: ")
    player = Player(name)
    enemies = [
        Enemy("Goblin", 30, 10),
        Enemy("Orc", 50, 15),
        Enemy("Dragon", 100, 25)
    ]

    for enemy in enemies:
        if not battle(player, enemy):
            break
    else:
        print(f"\nCongratulations, {player.name}! You defeated all the enemies!")

if __name__ == "__main__":
    main()
