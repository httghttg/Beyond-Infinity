from abc import ABCMeta
import pygame
from View.ParentView import View, spritesFolder


class EnemyBullet(metaclass=ABCMeta):

    def __init__(self):
        self.name = None
        self.images = None
        self.width = None
        self.height = None
        self.sound = None
        self.speed = None
        self.damage = None


class RedEnemyBullet(EnemyBullet):
    def __init__(self):
        super().__init__()
        self.name = "Red_Bullet"
        self.image = View.load_images(spritesFolder + 'Projectiles/Small_Enemy_Red_Bullet')
        self.width = 10
        self.height = 24
        self.sound = pygame.mixer.Sound(spritesFolder + 'Projectiles/Small_Red_Bullet.wav')
        self.speed = 7
        self.damage = 25


class BulletEnemyFactory:

    @staticmethod
    def create_enemy_bullet(bullet_type):
        try:
            if bullet_type == "Red_Bullet":
                return RedEnemyBullet()
            raise AssertionError("Bullet not found.")
        except AssertionError as _e:
            print(_e)
