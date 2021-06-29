import random
from abc import ABCMeta
import pygame
from Model.EnemyBulletFactory import BulletEnemyFactory
from Model.EnemyBulletSprite import EnemyBulletSprite
from Model.EnemyShipSprite import EnemyShipSprite
from Model.ExplosionFactory import CreateExplosionFactory
from View.ParentView import View


class EnemyShip(metaclass=ABCMeta):

    def __init__(self):
        self.width = None
        self.height = None
        self.name = None
        self.speed = None
        self.health = None
        self.damage = None
        self.score = None
        self.images = None
        self.explosion = None
        self.explosionSound = None
        self.shoots = None
        self.cdLow = None
        self.cdHigh = None
        self.hitBox = []
        self.category = 'normal'
        self.movement = 'straight'
        self.hasAbility = True

    def create_enemy_sprite(self, xcor, ycor):
        return EnemyShipSprite(xcor, ycor, self.width, self.height, self.images, 0, self,
                               random.uniform(self.cdLow, self.cdHigh))


class Imperier(EnemyShip):
    def __init__(self):
        super().__init__()
        self.width = 64
        self.height = 64
        self.name = "Imperier"
        self.speed = 1
        self.health = 30
        self.damage = 25
        self.score = 175
        self.images = View.load_images('Sprites/EnemyShips/Lvl1_Enemy_Imperier')
        self.explosion = CreateExplosionFactory.create_explosion("64_Basic")
        self.explosionSound = pygame.mixer.Sound('Sprites/Explosions/Explosion1.wav')
        self.shoots = True
        self.bullet = BulletEnemyFactory.create_enemy_bullet("Red_Bullet")
        self.cdLow = 2
        self.cdHigh = 6
        self.hitBox.append([20, 10, 24, 50])
        self.hitBox.append([3, 35, 59, 10])

    def use_ability(self, enemy, enemy_bullet_array):
        bullet = EnemyBulletSprite(enemy.xcor + (self.width/2)-16, enemy.ycor + self.height - 30, self.bullet.width, self.bullet.height, self.bullet.image, 0, self.bullet, 0)
        enemy_bullet_array.add(bullet)
        bullet.sound.play()
        return enemy_bullet_array


class Scatter(EnemyShip):
    def __init__(self):
        super().__init__()
        self.width = 64
        self.height = 64
        self.name = "Scatter"
        self.speed = 1
        self.health = 20
        self.damage = 25
        self.score = 200
        self.images = View.load_images('Sprites/EnemyShips/Lvl1_Enemy_Scatter')
        self.explosion = CreateExplosionFactory.create_explosion("64_Basic")
        self.explosionSound = pygame.mixer.Sound('Sprites/Explosions/Explosion1.wav')
        self.shoots = True
        self.bullet = BulletEnemyFactory.create_enemy_bullet("Red_Bullet")
        self.cdLow = 2
        self.cdHigh = 7
        self.hitBox.append([27, 13, 10, 50])
        self.hitBox.append([15, 25, 35, 20])
        self.hitBox.append([0, 20, 64, 20])

    def use_ability(self, enemy, enemy_bullet_array):
        bullet1 = EnemyBulletSprite(enemy.xcor + (self.width/2)-16, enemy.ycor + self.height - 12, self.bullet.width, self.bullet.height, self.bullet.image, 0, self.bullet, .5)
        bullet2 = EnemyBulletSprite(enemy.xcor + (self.width / 2) - 16, enemy.ycor + self.height - 12, self.bullet.width,
                                    self.bullet.height, self.bullet.image, 0, self.bullet, -.5)
        bullet3 = EnemyBulletSprite(enemy.xcor + (self.width / 2) - 16, enemy.ycor + self.height - 12, self.bullet.width,
                                    self.bullet.height, self.bullet.image, 0, self.bullet, 0)
        enemy_bullet_array.add(bullet1)
        enemy_bullet_array.add(bullet2)
        enemy_bullet_array.add(bullet3)
        bullet1.sound.play()
        bullet2.sound.play()
        bullet3.sound.play()
        return enemy_bullet_array


class Impaler(EnemyShip):
    def __init__(self):
        super().__init__()
        self.width = 96
        self.height = 96
        self.name = "Impaler"
        self.speed = 1.5
        self.health = 40
        self.damage = 40
        self.score = 175
        self.images = View.load_images('Sprites/EnemyShips/Lvl1_Enemy_Impaler')
        self.explosion = CreateExplosionFactory.create_explosion("96_Basic")
        self.explosionSound = pygame.mixer.Sound('Sprites/Explosions/Explosion1.wav')
        self.shoots = False
        self.cdLow = 1
        self.cdHigh = 4
        self.hitBox.append([10, 20, 75, 40])
        self.hitBox.append([15, 50, 5, 40])
        self.hitBox.append([35, 50, 5, 40])
        self.hitBox.append([35, 50, 5, 40])
        self.hitBox.append([75, 50, 5, 40])

    def use_ability(self, enemy, enemy_bullet_array):
        enemy.speed += 1.5
        return enemy_bullet_array


class KZBomber(EnemyShip):
    def __init__(self):
        super().__init__()
        self.width = 64
        self.height = 64
        self.name = "KZBomber"
        self.speed = 1.5
        self.health = 1
        self.damage = 40
        self.score = 75
        self.images = View.load_images('Sprites/EnemyShips/Lvl1_Enemy_KZ_Bomber')
        self.explosion = CreateExplosionFactory.create_explosion("176_Red")
        self.explosionSound = pygame.mixer.Sound('Sprites/Explosions/Explosion2.wav')
        self.shoots = False
        self.cdLow = 1
        self.cdHigh = 4
        self.movement = 'zig-zag'
        self.category = "explode"
        self.hasAbility = False
        self.hitBox.append([5, 30, 55, 10])
        self.hitBox.append([12, 10, 40, 45])


class ShipEnemyFactory:

    @staticmethod
    def create_enemy_ship(enemy_type):
        try:
            if enemy_type == "Imperier":
                return Imperier()
            elif enemy_type == "Scatter":
                return Scatter()
            elif enemy_type == "Impaler":
                return Impaler()
            elif enemy_type == "KZBomber":
                return KZBomber()
            raise AssertionError("Enemy not found.")
        except AssertionError as _e:
            print(_e)
