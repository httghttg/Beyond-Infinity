from Model.GameSpriteModel import GameSprite


class Player(GameSprite):
    # player class (xcor, ycor, width, height, folder containing the images, starting frame, player's shooting type)
    def __init__(self, xcor, ycor, width, height, images, starting_frame, player_ship):
        super().__init__(xcor, ycor, width, height, images, starting_frame)
        self.playerShip = player_ship
        self.score = 0
        self.iFrames = 1.5
        self.collisionTime = 0
        self.dead = False
        self.deathSoundPlayed = False
        self.invincible = False
        self.hitboxArray = []
        for x in player_ship.hitBoxes:
            self.hitboxArray.append([self.xcor + x[0], self.ycor + x[1], x[2], x[3]])

    def update_time_dependent(self, screen, dt):
        self.currentTime += dt
        if self.playerShip.health > 0:
            if self.currentTime >= self.animationTime:
                self.currentTime = 0
                self.index = (self.index + 1) % len(self.images)
            # Sprite flickers if invincible
            if not self.invincible:
                screen.blit(self.images[self.index], (self.xcor, self.ycor))
            else:
                if self.index % 2:
                    screen.blit(self.images[self.index], (self.xcor, self.ycor))
        # Sprite dead animation
        else:
            if not self.deathSoundPlayed:
                self.playerShip.deathSound.play()
                self.deathSoundPlayed = True
            if self.currentTime >= self.animationTime:
                self.currentTime = 0
                self.index = (self.index + 1) % len(self.playerShip.des_images)
                if self.index == len(self.playerShip.des_images) - 1:
                    self.dead = True
                    self.kill()
            screen.blit(self.playerShip.des_images[self.index], (self.xcor, self.ycor))

