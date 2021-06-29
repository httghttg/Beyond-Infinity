from _py_abc import ABCMeta
from abc import abstractmethod
from View.ParentView import View


class Explosion(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.name = None
        self.images = None
        self.width = None
        self.height = None


class XSmallBasicExplosion(Explosion):
    def __init__(self):
        super().__init__()
        self.name = "16_Basic"
        self.images = View.load_images('Sprites/Explosions/16x16_Basic_Explosion')
        self.width = 16
        self.height = 16


class XSmallRedExplosion(Explosion):
    def __init__(self):
        super().__init__()
        self.name = "16_Red"
        self.images = View.load_images('Sprites/Explosions/16x16_Red_Explosion')
        self.width = 16
        self.height = 16


class SmallBasicExplosion(Explosion):
    def __init__(self):
        super().__init__()
        self.name = "64_Basic"
        self.images = View.load_images('Sprites/Explosions/64x64_Basic_Explosion')
        self.width = 64
        self.height = 64


class BasicExplosion(Explosion):
    def __init__(self):
        super().__init__()
        self.name = "96_Basic"
        self.images = View.load_images('Sprites/Explosions/96x96_Basic_Explosion')
        self.width = 96
        self.height = 96


class LargeRedExplosion(Explosion):
    def __init__(self):
        super().__init__()
        self.name = "128_Red"
        self.images = View.load_images('Sprites/Explosions/128x128_Red_Explosion')
        self.width = 128
        self.height = 128

class XLargeBlueExplosion:
    def __init__(self):
        super().__init__()
        self.name = "176_Blue"
        self.images = View.load_images('Sprites/Explosions/176x176_Blue_Explosion')
        self.width = 176
        self.height = 176


class XLargeRedExplosion:
    def __init__(self):
        super().__init__()
        self.name = "176_Red"
        self.images = View.load_images('Sprites/Explosions/176x176_Red_Explosion')
        self.width = 176
        self.height = 176


class CreateExplosionFactory:

    @staticmethod
    def create_explosion(explosion_type):
        try:
            if explosion_type == "16_Basic":
                return XSmallBasicExplosion()
            elif explosion_type == "16_Red":
                return XSmallRedExplosion()
            elif explosion_type == "64_Basic":
                return SmallBasicExplosion()
            elif explosion_type == "96_Basic":
                return BasicExplosion()
            elif explosion_type == "128_Red":
                return LargeRedExplosion()
            elif explosion_type == "176_Blue":
                return XLargeBlueExplosion()
            elif explosion_type == "176_Red":
                return XLargeRedExplosion()
            raise AssertionError("Explosion not found.")
        except AssertionError as _e:
            print(_e)
