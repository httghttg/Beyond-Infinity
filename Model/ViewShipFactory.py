from abc import ABCMeta, abstractmethod
from View.ParentView import View, Sprite, spritesFolder


class ViewShip(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        self.name = None
        self.health = None
        self.damage = None
        self.fireRate = None
        self.speed = None
        self.images = None
        self.shotType = None
        self.shotImage = None
        self.ability = None
        self.abilityImages = None


class ViewInfinity(ViewShip):

    def __init__(self):
        super().__init__()
        self.name = "Infinity"
        self.health = 3
        self.damage = 1
        self.fireRate = 3
        self.speed = 3
        self.images = Sprite(144, 425, 64, View.load_images(spritesFolder + 'PlayerShips/Infinity/Infinity_Flying'), 0)
        self.shotType = 'Single Shot'
        self.shotImage = Sprite(550, 365, 64, View.load_images(spritesFolder + 'Projectiles/Small_Basic_Bullet'), 0)
        self.ability = '  Ion Blast'
        self.abilityImages = Sprite(534, 494, 64, View.load_images(spritesFolder + 'Projectiles/Blue_Ion_Blast'), 0)


class ViewImperier(ViewShip):

    def __init__(self):
        super().__init__()
        self.name = "Imperier"
        self.images = Sprite(144, 425, 64, View.load_images(spritesFolder + 'PlayerShips/Imperier/Flying'), 0)
        self.health = 3
        self.damage = 3
        self.fireRate = 2
        self.speed = 2
        self.shotType = 'Single Shot'
        self.shotImage = Sprite(550, 365, 64, View.load_images(spritesFolder + 'Projectiles/Small_Red_Bullet'), 0)
        self.ability = 'Mini KZ Mine'
        self.abilityImages = Sprite(534, 500, 64, View.load_images(spritesFolder + 'Projectiles/Mini_KZ'),
                                    0)


class ViewScatter(ViewShip):

    def __init__(self):
        super().__init__()
        self.name = "Scatter"
        self.images = Sprite(144, 425, 64, View.load_images(spritesFolder + 'PlayerShips/Scatter/Flying'), 0)
        self.health = 2
        self.damage = 4
        self.fireRate = 1
        self.speed = 2
        self.shotType = ' Tri-Shot'
        self.shotImage = Sprite(550, 365, 64, View.load_images(spritesFolder + 'Projectiles/Tri-Small_Red_Bullet'), 0)
        self.ability = 'Scatter Shot'
        self.abilityImages = Sprite(534, 500, 64, View.load_images(spritesFolder + 'Projectiles/Scatter_Small_Red_Bullet'), 0)


class ShipViewFactory:

    @staticmethod
    def create_view_ship(ship_type):
        try:
            if ship_type == "ViewInfinity":
                return ViewInfinity()
            elif ship_type == "ViewImperier":
                return ViewImperier()
            elif ship_type == "ViewScatter":
                return ViewScatter()
            raise AssertionError("View Ship not found.")
        except AssertionError as _e:
            print(_e)

