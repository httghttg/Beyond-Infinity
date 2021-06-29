import copy
import random
import uuid
from Model.GameSpriteModel import GameSprite


class EnemyShipSprite(GameSprite):
    def __init__(self, xcor, ycor, width, height, images, starting_frame, enemy_ship, cd):
        super().__init__(xcor, ycor, width, height, images, starting_frame)
        self.xcor = xcor
        self.ycor = ycor
        self.width = width
        self.height = height
        self.enemyShip = enemy_ship
        self.name = enemy_ship.name
        self.speed = enemy_ship.speed
        self.damage = enemy_ship.damage
        self.health = enemy_ship.health
        self.id = uuid.uuid4()
        self.right = bool(random.getrandbits(1))
        self.hitboxArray = []
        for i in enemy_ship.hitBox:
            self.hitboxArray.append([self.xcor + i[0], self.ycor + i[1], i[2], i[3]])
        # cd is added here because it's random and different for every ship
        self.abilitycd = cd
        self.cd = self.abilitycd
        self.hurtboxArray = copy.deepcopy(self.hitboxArray)

    def move(self, window_width):
        if self.enemyShip.movement == 'zig-zag':
            self.ycor += self.speed
            if self.xcor >= window_width - self.width:
                self.right = True
            elif self.xcor <= 0:
                self.right = False
            if not self.right:
                self.xcor += self.speed / 2
            else:
                self.xcor -= self.speed / 2
            for hitbox in self.hitboxArray:
                hitbox[1] += self.speed
                if not self.right:
                    hitbox[0] += self.speed / 2
                else:
                    hitbox[0] -= self.speed / 2
            for hurtbox in self.hurtboxArray:
                hurtbox[1] += self.speed
                if not self.right:
                    hurtbox[0] += self.speed / 2
                else:
                    hurtbox[0] -= self.speed / 2
        else:
            self.ycor += self.speed
            for hitbox in self.hitboxArray:
                hitbox[1] += self.speed
            for hurtbox in self.hurtboxArray:
                hurtbox[1] += self.speed

    def ability_timer(self, dt):
        if not self.abilitycd == 0:
            self.cd -= dt
            if self.cd <= 0:
                self.cd = self.abilitycd
                return True
            else:
                return False
        else:
            return False
