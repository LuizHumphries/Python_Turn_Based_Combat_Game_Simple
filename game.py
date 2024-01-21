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
    

class Hero(Character):
    """ Hero character class """
    def __init__(self, name, life, level, hability) -> None:
        super().__init__(name, life, level)
        self.__hability = hability
    
    def get_hability(self):
        return self.__hability
    
    def exibit_details(self):
        return f"{super().exibit_details()}\n Hability: {self.get_hability()}"

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

            input("Pressione Enter para atacar...")
            choice = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

#Creating Game 
game = Game()
game.start_batle()
