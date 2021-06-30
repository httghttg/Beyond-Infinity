from abc import ABCMeta, abstractmethod
import pygame
from Model.PlayerBulletFactory import BulletPlayerFactory
from View.ParentView import View, spritesFolder


class PlayerShip(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.startingX = 310
        self.startingY = 600
        self.width = 64
        self.height = 64
        self.energy = 0
        self.hitSound = pygame.mixer.Sound(spritesFolder + 'PlayerShips/Ship_Hit.wav')
        self.bulletType = None
        self.shotType = None
        self.fireRate = None
        self.playerSpeed = None
        self.playerDecay = 15
        self.playerCurrentSpeedY = 0
        self.playerEdgeY = 0
        self.playerCurrentSpeedX = 0
        self.playerEdgeX = 0
        self.bulletSpeedAdder = 0
        self.maxHealth = None
        self.health = None
        self.energyGain = None
        self.energyUsage = 100
        self.maxEnergy = 100
        self.ability = None
        self.currentShotType = None
        self.currentBullet = None
        self.damageAdder = 0
        self.explodeDamageAdder = 0
        self.images = None
        self.des_images = None
        self.deathSound = None
        self.hitBoxes = None


class PlayerInfinity(PlayerShip):

    def __init__(self):
        super().__init__()
        self.bulletType = 'Basic_Bullet'
        self.shotType = 'Single_Middle'
        self.abilityShotType = 'Single_Middle'
        self.fireRate = .25
        self.playerSpeed = 7
        self.bulletSpeedAdder = 0
        self.maxHealth = 100
        self.health = self.maxHealth
        self.energyGain = 8
        self.ability = 'Ion_Blast'
        self.currentBullet = BulletPlayerFactory.create_player_bullet(self.bulletType)
        self.specialBullet = BulletPlayerFactory.create_player_bullet(self.ability)
        self.damageAdder = 0
        self.images = View.load_images(spritesFolder + 'PlayerShips/Infinity/Infinity_Flying')
        self.des_images = View.load_images(spritesFolder + 'PlayerShips/Infinity/Infinity_Destroyed')
        self.deathSound = pygame.mixer.Sound(spritesFolder + 'PlayerShips/Infinity/Infinity_Destroyed.wav')
        self.hitBoxes = [[25, 0, 15, 50], [7, 35, 53, 10]]


class PlayerImperier(PlayerShip):

    def __init__(self):
        super().__init__()
        self.bulletType = 'Red_Bullet'
        self.shotType = 'Single_Middle'
        self.fireRate = .6
        self.playerSpeed = 6
        self.bulletSpeedAdder = 0
        self.maxHealth = 100
        self.health = self.maxHealth
        self.energyGain = 10
        self.ability = 'Mini_KZ'
        self.currentBullet = BulletPlayerFactory.create_player_bullet(self.bulletType)
        self.specialBullet = BulletPlayerFactory.create_player_bullet(self.ability)
        self.damageAdder = 10
        self.images = View.load_images(spritesFolder + 'PlayerShips/Imperier/Flying')
        self.des_images = View.load_images(spritesFolder + 'PlayerShips/Imperier/Destroyed')
        self.deathSound = pygame.mixer.Sound(spritesFolder + 'PlayerShips/Imperier/Imperier_Destroyed.wav')
        self.hitBoxes = [[20, 10, 25, 50], [5, 18, 55, 10]]


class PlayerScatter(PlayerShip):

    def __init__(self):
        super().__init__()
        self.bulletType = 'Red_Bullet'
        self.shotType = 'Tri_Spread'
        self.fireRate = .9
        self.playerSpeed = 6
        self.bulletSpeedAdder = 0
        self.maxHealth = 75
        self.health = self.maxHealth
        self.energyGain = 4
        self.ability = 'Scatter_Shot'
        self.currentBullet = BulletPlayerFactory.create_player_bullet(self.bulletType)
        self.specialBullet = BulletPlayerFactory.create_player_bullet(self.ability)
        self.damageAdder = 0
        self.images = View.load_images(spritesFolder + 'PlayerShips/Scatter/Flying')
        self.des_images = View.load_images(spritesFolder + 'PlayerShips/Scatter/Destroyed')
        self.deathSound = pygame.mixer.Sound(spritesFolder + 'PlayerShips/Scatter/Scatter_Destroyed.wav')
        self.hitBoxes = [[27, 13, 10, 50], [15, 25, 35, 20], [0, 20, 64, 20]]


class ShipPlayerFactory:

    @staticmethod
    def create_player_ship(ship_type):
        try:
            if ship_type == "Infinity":
                return PlayerInfinity()
            elif ship_type == "Imperier":
                return PlayerImperier()
            elif ship_type == "Scatter":
                return PlayerScatter()
            raise AssertionError("Ship not found.")
        except AssertionError as _e:
            print(_e)

