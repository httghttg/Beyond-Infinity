import pygame


class GameSprite(pygame.sprite.Sprite):
    # class for a Sprite. To create a sprite you must provide: (x coordinate, y coordinate, size of the image, array of
    # all the images, and the starting frame)
    def __init__(self, xcor, ycor, width, height, images, starting_frame):
        super(GameSprite, self).__init__()
        self.xcor = xcor
        self.ycor = ycor
        # creates rectangle for the sprite
        self.rect = pygame.Rect((xcor, ycor), (width, height))
        self.images = images
        # time it takes for the the sprite moves to the next frame
        self.animationTime = .08
        self.currentTime = 0
        self.index = starting_frame

    def update_time_dependent(self, screen, dt):
        # Updates the image of Sprite based on animation_time. Must provide: (the window, milliseconds since last frame)
        self.currentTime += dt
        if self.currentTime >= self.animationTime:
            self.currentTime = 0
            self.index = (self.index + 1) % len(self.images)
        screen.blit(self.images[self.index], (self.xcor, self.ycor))

    def update(self, screen, dt):
        # This is the method that's being called when 'all_sprites.update(dt)' is called. Must provide:
        # (the window, milliseconds since last frame)
        self.update_time_dependent(screen, dt)

    def rotate(self, rotate):
        i = len(self.images)
        rotated_images = []
        while i > 0:
            rotated_image = pygame.transform.rotate(self.images[i-1], rotate)
            rotated_images.append(rotated_image)
            i -= 1
        return rotated_images

