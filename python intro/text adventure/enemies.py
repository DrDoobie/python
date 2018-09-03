class Enemy ():
    def __init__ (self, name, legend, hp, damage)
        self.name = name
        self.legend = legend
        self.hp = hp
        self.damage = damage

    def isAlive (self):
        return self.hp > 0

class Leprechaun (Enemy):
    def __init__ (self):
        super().__init__(name = "Leprechaun",
                         legend = "A type of elf that likes getting into mischief.",
                         hp = 60,
                         damage = 6)

class Centaur (Enemy):
    def __init__ (self):
        super().__init__(name = "Centaur",
                         legend = "It has the upper body of a human and the lower body of a horse...",
                         hp = 200,
                         damage = 50)
