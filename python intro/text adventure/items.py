class Item ():
    def __init__ (self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__ (self):
        return "{}, {}, Value: {}".format(self.name, self.description, self.value)

class Weapon (Item):
    def __init__ (self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__ (self):
        return "{}, {}, Value: {}, Damage: {}".format(self.name, self.description, self.value, self.damage)

class Dagger (Weapon):
    def __init__ (self):
        super().__init__(name = "Dull Dagger",
                         description = "It's just an old rusty dagger.",
                         value = 3,
                         damage = 8)

class Sword (Weapon):
    def __init__ (self):
        super().__init__(name = "Short Sword",
                         description = "It's an old knight's sword.",
                         value = 20,
                         damage = 15)