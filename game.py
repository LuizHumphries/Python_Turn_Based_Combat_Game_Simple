class Character:
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
    def __init__(self, name, life, level, hability) -> None:
        super().__init__(name, life, level)
        self.__hability = hability
    
    def get_hability(self):
        return self.__hability
    
    def exibit_details(self):
        return f"{super().exibit_details()}\n Hability: {self.get_hability()}"

class Enemy(Character):
    def __init__(self, name, life, level, enemy_type) -> None:
        super().__init__(name, life, level)
        self.__enemy_type = enemy_type

    def get_enemy_type(self):
        return self.__enemy_type
    
    def exibit_details(self):
        return f"{super().exibit_details()}\nEnemy Type: {self.get_enemy_type()}"

heroi = Hero("Hero", 100, 5, "Super Strength")
print(heroi.exibit_details())
enemy = Enemy("Bat", 50, 3, "fly")
print(enemy.exibit_details())