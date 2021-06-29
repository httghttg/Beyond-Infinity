from abc import ABCMeta
import pygame
from Model.ExplosionFactory import CreateExplosionFactory
from View.ParentView import View


class PlayerBullet(metaclass=ABCMeta):

    def __init__(self):
        self.name = None
        self.images = None
        self.width = None
        self.height = None
        self.sound = None
        self.hitSound = None
        self.explosion = None
        self.speed = None
        self.explode = None
        self.explodeDamage = 0
        self.damage = None
        self.movement = 'Straight'
        self.hurtbox = []

#    @abstractmethod
#    def get_bullet(self):
#        """Returns Bullet"""

#    @abstractmethod
#    def get_bullet_damage(self):
#        """Returns Bullet Damage"""

#    @abstractmethod
#    def get_bullet_speed(self):
#        """Returns Bullet Damage"""


class BasicPlayerBullet(PlayerBullet):
    def __init__(self):
        super().__init__()
        self.name = "Basic_Bullet"
        self.image = View.load_images('Sprites/Projectiles/Small_Basic_Bullet')
        self.width = 10
        self.height = 24
        self.sound = pygame.mixer.Sound('Sprites/Projectiles/Basic_Bullet.wav')
        self.hitSound = pygame.mixer.Sound('Sprites/Projectiles/Basic_Bullet_Hit.wav')
        self.explosion = CreateExplosionFactory.create_explosion("16_Basic")
        self.speed = 10
        self.explode = False
        self.damage = 10
        self.hurtbox = [10, 4, 12, 24]


class RedPlayerBullet(PlayerBullet):
    def __init__(self):
        super().__init__()
        self.name = "Red_Bullet"
        self.image = View.load_images('Sprites/Projectiles/Small_Red_Bullet')
        self.width = 10
        self.height = 24
        self.sound = pygame.mixer.Sound('Sprites/Projectiles/Small_Red_Bullet.wav')
        self.hitSound = pygame.mixer.Sound('Sprites/Projectiles/Basic_Bullet_Hit.wav')
        self.explosion = CreateExplosionFactory.create_explosion("16_Red")
        self.speed = 7
        self.explode = False
        self.damage = 10
        self.hurtbox = [10, 4, 12, 24]


class IonBlast(PlayerBullet):
    def __init__(self):
        super().__init__()
        self.name = "Ion_Blast"
        self.image = View.load_images('Sprites/Projectiles/Blue_Ion_Blast')
        self.width = 64
        self.height = 64
        self.sound = pygame.mixer.Sound('Sprites/Projectiles/Ion_Blast.wav')
        self.hitSound = pygame.mixer.Sound('Sprites/Explosions/Ion_Explosion.wav')
        self.explosion = CreateExplosionFactory.create_explosion("176_Blue")
        self.speed = 8
        self.explode = True
        self.explodeDamage = 3
        self.damage = 0
        self.hurtbox = [24, 24, 16, 16]


class MiniKZ(PlayerBullet):
    def __init__(self):
        super().__init__()
        self.name = "Mini_KZ"
        self.image = View.load_images('Sprites/Projectiles/Mini_KZ')
        self.width = 64
        self.height = 64
        self.sound = pygame.mixer.Sound('Sprites/Projectiles/Deploy_Mine.wav')
        self.hitSound = pygame.mixer.Sound('Sprites/Explosions/Ion_Explosion.wav')
        self.explosion = CreateExplosionFactory.create_explosion("176_Red")
        self.speed = 8
        self.explode = True
        self.explodeDamage = 4
        self.damage = 0
        self.movement = 'Straight_Full_Decay'
        self.decay = .15
        self.hurtbox = [20, 20, 24, 246]


class ScatterShot(PlayerBullet):
    def __init__(self):
        super().__init__()
        self.name = "Scatter_Shot"
        self.image = View.load_images('Sprites/Projectiles/Small_Red_Bullet')
        self.width = 10
        self.height = 24
        self.sound = pygame.mixer.Sound('Sprites/Projectiles/Multi_Red_Bullets.wav')
        self.hitSound = pygame.mixer.Sound('Sprites/Projectiles/Basic_Bullet_Hit.wav')
        self.explosion = CreateExplosionFactory.create_explosion("176_Red")
        self.explosion = CreateExplosionFactory.create_explosion("16_Red")
        self.speed = 7
        self.explode = False
        self.damage = 10
        self.counter = 4
        self.angle = 1
        self.hurtbox = [10, 4, 12, 24]


class BulletPlayerFactory:

    @staticmethod
    def create_player_bullet(bullet_type):
        try:
            if bullet_type == "Basic_Bullet":
                return BasicPlayerBullet()
            elif bullet_type == "Red_Bullet":
                return RedPlayerBullet()
            elif bullet_type == "Ion_Blast":
                return IonBlast()
            elif bullet_type == "Mini_KZ":
                return MiniKZ()
            elif bullet_type == "Scatter_Shot":
                return ScatterShot()
            raise AssertionError("Bullet not found.")
        except AssertionError as _e:
            print(_e)
