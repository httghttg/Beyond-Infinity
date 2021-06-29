from Model.GameSpriteModel import GameSprite


class ExplosionSprite(GameSprite):
    def __init__(self, xcor, ycor, width, height, images, starting_frame, sound, damage, player):
        super().__init__(xcor, ycor, width, height, images, starting_frame)
        self.sound = sound
        self.soundPlayed = False
        self.hurtboxArray = []
        self.damage = damage
        self.player = player
        self.idArray = []

        if damage > 0:
            if width == 128:
                self.hurtboxArray.append([self.xcor + 56, self.ycor, 16, 128])
                self.hurtboxArray.append([self.xcor, self.ycor + 56, 128, 16])
                self.hurtboxArray.append([self.xcor + 20, self.ycor + 20, 87, 87])
            elif width == 176:
                self.hurtboxArray.append([self.xcor + 64, self.ycor, 48, 176])
                self.hurtboxArray.append([self.xcor, self.ycor + 64, 176, 48])
                self.hurtboxArray.append([self.xcor + 24, self.ycor + 24, 128, 128])

    def update_time_dependent(self, screen, dt):
        # Updates the image of Sprite based on animation_time. Must provide: (the window, milliseconds since last frame)
        if not self.soundPlayed:
            self.sound.play()
            self.soundPlayed = True
        self.currentTime += dt
        if self.currentTime >= self.animationTime:
            self.currentTime = 0
            if self.damage > 0 and self.index > 0:
                self.hurtboxArray = []
            self.index = (self.index + 1) % len(self.images)
            if self.index == len(self.images) - 1:
                self.kill()
        screen.blit(self.images[self.index], (self.xcor, self.ycor))