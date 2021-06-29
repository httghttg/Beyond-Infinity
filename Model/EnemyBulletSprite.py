from Model.GameSpriteModel import GameSprite


class EnemyBulletSprite(GameSprite):
    # bullet class (xcor, ycor, width, height, folder containing the images, starting frame, player)
    def __init__(self, xcor, ycor, width, height, images, starting_frame, enemy_bullet, x):
        super().__init__(xcor, ycor, width, height, images, starting_frame)
        self.xcor = xcor
        self.ycor = ycor
        self.width = width
        self.height = height
        self.speed = enemy_bullet.speed
        self.damage = enemy_bullet.damage
        self.name = enemy_bullet.name
        self.sound = enemy_bullet.sound
        self.x = x
        self.hurtbox = []

    def move(self):
        if self.name == 'Red_Bullet':
            self.hurtbox = [self.xcor + 10, self.ycor + 4, 12, 24]
            self.xcor += self.x
            self.ycor += self.speed
            self.hurtbox[0] += self.x
            self.hurtbox[1] += self.speed
