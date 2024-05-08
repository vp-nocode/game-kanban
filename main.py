import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        self.attack_power = random.randint(10, 20)
        other.health -= self.attack_power
        if other.health < 0:
            other.health = 0
        print(f"{self.name} attacks {other.name} and deals {self.attack_power} damage.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Computer")

    def start(self):
        print("The battle of heroes begins!")
        # turn = 0  # Игрок начинает первым
        turn = random.randint(0, 1)  # random choice begin player

        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)

            print(f"Health {self.player.name}: {self.player.health}")
            print(f"Health {self.computer.name}: {self.computer.health}")
            turn += 1

        if self.player.is_alive():
            print(f"{self.player.name} win!")
        else:
            print(f"{self.computer.name} win!")


if __name__ == "__main__":
    player_name = input("Input player name: ")
    game = Game(player_name)
    game.start()
