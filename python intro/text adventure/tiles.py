import enemies, items

class Tile:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def enterTileNotif (self):
        raise NotImplementedError()

    def modifyPlayer (self, player):
        raise NotImplementedError()

class StartRoom (Tile):
    def enterTileNotif (self):
        return "Test"

    def modifyPlayer (self, player):
        # No action
        pass

class LootRoom (Tile):
    def __init__ (self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def addLoot (self, player):
        player.inventory.append(self.item)

    def modifyPlayer (self, player):
        self.addLoot(player)

class EnemyRoom (Tile):
    def __init__ (self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modifyPlayer (self, thePlayer):
        if self.enemy.isAlive():
            thePlayer.hp = thePlayer.hp - self.enemy.damage
            print("Enemy deals {} damage to you. You have {}hp remaining.".format(self.enemy.damage, thePlayer.hp))

