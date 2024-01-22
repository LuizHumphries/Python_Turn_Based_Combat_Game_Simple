import random

class Character:
    """ General Character class """
    def __init__(self, name, life, level) -> None:
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name
    def get_life(self):
        return self.__life
    def get_level(self):
        return self.__level
    def exibit_details(self):
        return f"Name: {self.get_name()}\nLife: {self.get_life()}\nLevel: {self.get_level()}"
    
    def recieve_damage(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0
    def atack(self, target):
        damage = random.randint(self.get_level() * 2, self.get_level() * 4)
        target.recieve_damage(damage)
        print(f"{self.get_name()} atacked {target.get_name()} and gave {damage} of damage")
        
class Hero(Character):
    """ Hero character class """
    def __init__(self, name, life, level, hability) -> None:
        super().__init__(name, life, level)
        self.__hability = hability
    
    def get_hability(self):
        return self.__hability
    
    def exibit_details(self):
        return f"{super().exibit_details()}\nHability: {self.get_hability()}"
    
    def special_atack(self, target):
        damage = random.randint(self.get_level() * 5, self.get_level() * 8)
        target.recieve_damage(damage)
        print(f"{self.get_name()} use the special hability {self.get_hability()} on {target.get_name()} and did {damage} of damage")

class Enemy(Character):
    """ Enemy character class """
    def __init__(self, name, life, level, enemy_type) -> None:
        super().__init__(name, life, level)
        self.__enemy_type = enemy_type

    def get_enemy_type(self):
        return self.__enemy_type
    
    def exibit_details(self):
        return f"{super().exibit_details()}\nEnemy Type: {self.get_enemy_type()}"

class Game:
    """ Class for game management """
    def __init__(self) -> None:
        self.hero = Hero("Hero", 100, 5, "Super Strength")
        self.enemy = Enemy("Bat", 50, 3, "fly")
    
    def start_batle(self):
        """ management of turn based batle """
        print("Starting Batle")
        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nCharacter Details:")
            print(self.hero.exibit_details())
            print(self.enemy.exibit_details())

            input("Press Enter to atack...")
            choice = input("Chose (1 - Normal atack, 2 - Special atack): ")
            if choice == "1":
                self.hero.atack(self.enemy)

            elif choice == "2":
                self.hero.special_atack(self.enemy)

            else:
                print("Invalid comand, choose again")    
            if self.enemy.get_life() > 0:
                self.enemy.atack(self.hero)

        if self.hero.get_life() > 0:
            print("\nCongratulations, you won the battle!!")
        else:
            print("\n You lose!")

#Creating Game 
game = Game()
game.start_batle()
