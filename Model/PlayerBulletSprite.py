from Model.GameSpriteModel import GameSprite


class PlayerBulletSprite(GameSprite):
    # bullet class (xcor, ycor, width, height, folder containing the images, starting frame, player)
    def __init__(self, xcor, ycor, width, height, images, starting_frame, player_bullet, player, x):
        super().__init__(xcor, ycor, width, height, images, starting_frame)
        self.xcor = xcor
        self.ycor = ycor
        self.width = width
        self.height = height
        self.speed = player_bullet.speed + player.bulletSpeedAdder
        self.damage = player_bullet.damage + player.damageAdder
        self.explodeDamage = player_bullet.explodeDamage + player.explodeDamageAdder
        self.name = player_bullet.name
        self.playerBullet = player_bullet
        self.sound = player_bullet.sound
        self.hitSound = player_bullet.hitSound
        self.x = x
        self.hurtbox = [self.xcor + player_bullet.hurtbox[0], self.ycor + player_bullet.hurtbox[1], player_bullet.hurtbox[2], player_bullet.hurtbox[3]]

    def move(self):
        # moves the bullet. can customize bullet pathing
        if self.playerBullet.movement == 'Straight' or self.playerBullet.movement == 'Straight_Full_Decay':
            self.xcor += self.x
            self.ycor -= self.speed
            self.hurtbox[0] += self.x
            self.hurtbox[1] -= self.speed
            if self.playerBullet.movement == 'Straight_Full_Decay':
                if self.speed > 0:
                    self.speed -= self.playerBullet.decay
                else:
                    self.speed = 0

