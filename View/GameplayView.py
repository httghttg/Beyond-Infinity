# importation for pygame and os
import random
import pygame
from Model.EnemyShipFactory import ShipEnemyFactory
from Model.ExplosionSprite import ExplosionSprite
from Model.FormationFactory import FactoryFormation
from Model.PlayerBulletSprite import PlayerBulletSprite
from Model.PlayerShipFactory import ShipPlayerFactory
from Model.SectionModel import Section
from View.ParentView import View, Sprite
from View.PlayerModel import Player


class GameplayView(View):
    def __init__(self, selected_ship):
        super(GameplayView, self).__init__()
        self.name = "Gameplay"
        self.bg = pygame.image.load('Sprites/Menu/Blank_Page.png')
        # Player Ship
        self.playerShip = ShipPlayerFactory.create_player_ship(selected_ship)
        self.player = Player(self.playerShip.startingX, self.playerShip.startingY, self.playerShip.width,
                             self.playerShip.height, self.playerShip.images, 0, self.playerShip)
        self.playerAcceleration = self.playerShip.playerSpeed / self.playerShip.playerDecay
        self.margin = .01
        # List of each bullet
        self.bulletArray = pygame.sprite.Group()
        self.enemyBulletArray = pygame.sprite.Group()
        self.bulletTimer = 0
        # List of Explosions
        self.explosionArray = pygame.sprite.Group()
        # Display
        self.heart = View.load_images('Sprites/Player_Info/Heart')
        self.allFonts = pygame.font.get_fonts()
        self.font = pygame.font.SysFont(self.allFonts[8], 24)
        self.font1 = pygame.font.SysFont(self.allFonts[8], 20)
        self.rect = pygame.Rect((self.player.xcor, self.player.ycor), (self.playerShip.width, self.playerShip.height))
        # Sections
        self.section1 = Section(1, 0, 180, -96, 6, 9, 1)
        self.section2 = Section(2, 244, 392, -96, 6, 9, 3)
        self.section3 = Section(3, 456, 604, -96, 6, 9, 1)
        self.sectionArray = [self.section1, self.section2, self.section3]
        # Formations
        self.VFormation = FactoryFormation.create_formation("VFormation")
        self.CaretFormation = FactoryFormation.create_formation("CaretFormation")
        self.DiagonalOneFormation = FactoryFormation.create_formation("DiagonalOneFormation")
        self.DiagonalTwoFormation = FactoryFormation.create_formation("DiagonalTwoFormation")
        self.RhombusFormation = FactoryFormation.create_formation("RhombusFormation")
        self.formationList = [self.VFormation, self.CaretFormation, self.DiagonalOneFormation, self.DiagonalTwoFormation, self.RhombusFormation]
        # Enemy list
        self.imperier = ShipEnemyFactory.create_enemy_ship("Imperier")
        self.scatter = ShipEnemyFactory.create_enemy_ship("Scatter")
        self.impaler = ShipEnemyFactory.create_enemy_ship("Impaler")
        self.kzbomber = ShipEnemyFactory.create_enemy_ship("KZBomber")
        self.enemyType = [self.imperier, self.scatter, self.kzbomber, self.impaler]
        self.enemyList = pygame.sprite.Group()
        # Background
        self.starArray = [self.star1, self.star2, self.star3]
        self.backgroundArray = pygame.sprite.Group()
        self.addedBackground = False
        self.initBackgroundCD = 1
        self.backgroundCD = self.initBackgroundCD

    # Draws background and Player ship

    def draw(self, mouse, dt):
        # decreases bullet timer to manage fire rate
        self.bulletTimer -= dt
        # repeatedly draws the screen, must provide: (mouse position, milliseconds since last frame)
        self.screen.blit(self.bg, (0, 0))
        for i in self.sectionArray:
            self.spawn_enemies(i, dt)
        self.move_background(dt)
        self.move_enemies(dt)
        self.move_bullets(dt)
        self.check_enemy_hit()
        self.check_player_hit(dt)
        self.player.update(self.screen, dt)
        for j in self.explosionArray:
            j.update(self.screen, dt)
        self.display_player_info(self.screen)
        # Debug Player Hitbox
        # for hitbox in self.player.hitboxArray:
        #   pygame.draw.rect(self.screen, (255, 0, 0), hitbox, 3)
        pygame.display.update()

    def add_background_objects(self, num_objects, y_start, y_end):
        while num_objects > 0:
            randomXAxis = random.randint(0, self.windowWidth-34)
            randomYAxis = random.randint(y_start, y_end)
            randomStar = random.choice(self.starArray)
            randomFrame = random.randint(0, 2)
            self.backgroundArray.add(Sprite(randomXAxis, randomYAxis, 32, randomStar, randomFrame))
            num_objects = num_objects - 1

    def move_background(self, dt):
        if not self.addedBackground:
            self.add_background_objects(random.randint(20, 30), 0, self.windowHeight - 34)
            self.addedBackground = True
        for background_object in self.backgroundArray:
            background_object.ycor += self.playerShip.playerSpeed/10
            background_object.update(self.screen, dt)
            if background_object.ycor > self.windowHeight + 96:
                self.backgroundArray.remove(background_object)
        self.backgroundCD -= dt
        if self.backgroundCD <= 0:
            numberOfObjects = random.randint(1, 3)
            self.add_background_objects(numberOfObjects, -64, 0)
            self.backgroundCD = self.initBackgroundCD

    def move_player_y(self, speed):
        self.player.ycor += speed
        for hitbox in self.player.hitboxArray:
            hitbox[1] += speed

    def move_player_x(self, speed):
        self.player.xcor += speed
        for hitbox in self.player.hitboxArray:
            hitbox[0] += speed

    def check_edge_y(self):
        if self.windowHeight - self.playerShip.height <= self.player.ycor:
            self.playerShip.playerEdgeY = -1
            if self.playerShip.playerCurrentSpeedY > 0:
                self.playerShip.playerCurrentSpeedY = 0
        elif self.player.ycor <= 0:
            self.playerShip.playerEdgeY = 1
            if self.playerShip.playerCurrentSpeedY < 0:
                self.playerShip.playerCurrentSpeedY = 0

    def check_edge_x(self):
        if self.windowWidth - self.playerShip.width <= self.player.xcor:
            self.playerShip.playerEdgeX = -1
            if self.playerShip.playerCurrentSpeedX > 0:
                self.playerShip.playerCurrentSpeedX = 0
        elif self.player.xcor <= 0:
            self.playerShip.playerEdgeX = 1
            if self.playerShip.playerCurrentSpeedX < 0:
                self.playerShip.playerCurrentSpeedX = 0

    def deceleration_y(self):
        # up
        if self.playerShip.playerCurrentSpeedY < 0:
            if self.windowHeight - self.playerShip.height > self.player.ycor > 0:
                self.playerShip.playerCurrentSpeedY += self.playerAcceleration
                if self.player.ycor + self.playerShip.playerCurrentSpeedY < 0:
                    self.move_player_y(-self.player.ycor)
                else:
                    self.move_player_y(self.playerShip.playerCurrentSpeedY)
            else:
                self.check_edge_y()
        # down
        elif self.playerShip.playerCurrentSpeedY > 0:
            if self.windowHeight - self.playerShip.height > self.player.ycor > 0:
                self.playerShip.playerCurrentSpeedY -= self.playerAcceleration
                if self.player.ycor + self.playerShip.playerCurrentSpeedY > self.windowHeight - self.playerShip.height:
                    diff = (self.windowHeight - self.playerShip.height) - self.player.ycor
                    self.move_player_y(diff)
                else:
                    self.move_player_y(self.playerShip.playerCurrentSpeedY)
            else:
                self.check_edge_y()

    def deceleration_x(self):
        # left
        if self.playerShip.playerCurrentSpeedX < 0:
            if self.windowWidth - self.playerShip.width > self.player.xcor > 0:
                self.playerShip.playerCurrentSpeedX += self.playerAcceleration
                if self.player.xcor + self.playerShip.playerCurrentSpeedX < 0:
                    self.move_player_x(-self.player.xcor)
                else:
                    self.move_player_x(self.playerShip.playerCurrentSpeedX)
            else:
                self.check_edge_x()
        # right
        elif self.playerShip.playerCurrentSpeedX > 0:
            if self.windowWidth - self.playerShip.width > self.player.xcor > 0:
                self.playerShip.playerCurrentSpeedX -= self.playerAcceleration
                if self.player.xcor + self.playerShip.playerCurrentSpeedX > self.windowWidth - self.playerShip.width:
                    diff = (self.windowWidth - self.playerShip.width) - self.player.xcor
                    self.move_player_x(diff)
                else:
                    self.move_player_x(self.playerShip.playerCurrentSpeedX)
            else:
                self.check_edge_y()

    def key_event(self, key):
        if self.playerShip.health > 0:
            if (key[pygame.K_DOWN] or key[pygame.K_s]) and self.playerShip.playerEdgeY != -1:
                if self.playerShip.playerCurrentSpeedY < self.playerShip.playerSpeed:
                    self.playerShip.playerEdgeY = 0
                    if self.playerShip.playerCurrentSpeedY < 0:
                        self.playerShip.playerCurrentSpeedY += self.playerAcceleration*2
                    else:
                        self.playerShip.playerCurrentSpeedY += self.playerAcceleration
                    if self.player.ycor + self.playerShip.playerCurrentSpeedY > self.windowHeight - self.playerShip.height:
                        diff = (self.windowHeight - self.playerShip.height) - self.player.ycor
                        self.move_player_y(diff)
                    else:
                        self.move_player_y(self.playerShip.playerCurrentSpeedY)
                    self.check_edge_y()
                else:
                    self.deceleration_y()
            elif (key[pygame.K_UP] or key[pygame.K_w]) and self.playerShip.playerEdgeY != 1:
                if self.playerShip.playerCurrentSpeedY > -self.playerShip.playerSpeed:
                    self.playerShip.playerEdgeY = 0
                    if self.playerShip.playerCurrentSpeedY > 0:
                        self.playerShip.playerCurrentSpeedY -= self.playerAcceleration*2
                    else:
                        self.playerShip.playerCurrentSpeedY -= self.playerAcceleration
                    if self.player.ycor + self.playerShip.playerCurrentSpeedY < 0:
                        self.move_player_y(-self.player.ycor)
                    else:
                        self.move_player_y(self.playerShip.playerCurrentSpeedY)
                    self.check_edge_y()
                else:
                    self.deceleration_y()
            else:
                self.deceleration_y()
                # Rounds current speed to 0 if current speed is lower than the margin
                if (0 < self.playerShip.playerCurrentSpeedY < self.margin) or (
                        0 > self.playerShip.playerCurrentSpeedY > -self.margin):
                    self.playerShip.playerCurrentSpeedY = 0
            if key[pygame.K_LEFT] or key[pygame.K_a] and self.playerShip.playerEdgeX != 1:
                if self.playerShip.playerCurrentSpeedX > -self.playerShip.playerSpeed:
                    self.playerShip.playerEdgeX = 0
                    # If player pushes left and is deceleration right, double the acceleration of left
                    if self.playerShip.playerCurrentSpeedX > 0:
                        self.playerShip.playerCurrentSpeedX -= self.playerAcceleration * 2
                    else:
                        self.playerShip.playerCurrentSpeedX -= self.playerAcceleration
                    # Prevents player from going over the edge
                    if self.player.xcor + self.playerShip.playerCurrentSpeedX < 0:
                        self.move_player_x(-self.player.xcor)
                    else:
                        self.move_player_x(self.playerShip.playerCurrentSpeedX)
                    self.check_edge_x()
                else:
                    self.deceleration_x()
            elif key[pygame.K_RIGHT] or key[pygame.K_d] and self.playerShip.playerEdgeX != -1:
                if self.playerShip.playerCurrentSpeedX < self.playerShip.playerSpeed:
                    self.playerShip.playerEdgeX = 0
                    if self.playerShip.playerCurrentSpeedX < 0:
                        self.playerShip.playerCurrentSpeedX += self.playerAcceleration * 2
                    else:
                        self.playerShip.playerCurrentSpeedX += self.playerAcceleration
                    if self.player.xcor + self.playerShip.playerCurrentSpeedX > self.windowWidth - self.playerShip.width:
                        diff = (self.windowWidth - self.playerShip.width) - self.player.xcor
                        self.move_player_x(diff)
                    else:
                        self.move_player_x(self.playerShip.playerCurrentSpeedX)
                    self.check_edge_x()
                else:
                    self.deceleration_x()
            else:
                self.deceleration_x()
                # Rounds current speed to 0 if current speed is lower than the margin
                if (0 < self.playerShip.playerCurrentSpeedX < self.margin) or (
                        0 > self.playerShip.playerCurrentSpeedX > -self.margin):
                    self.playerShip.playerCurrentSpeedX = 0
            if key[pygame.K_SPACE]:
                if self.bulletTimer <= 0:
                    self.bulletTimer = self.playerShip.fireRate
                    self.shoot_bullet()
            if key[pygame.K_e]:
                if self.playerShip.energy >= 100:
                    self.playerShip.energy -= self.playerShip.energyUsage
                    self.bulletTimer = self.use_ability()

    def display_player_info(self, screen):
        # displays player info
        score_text = self.font.render('Score:' + str(self.player.score), False, (255, 255, 255))
        energy_text = self.font1.render(str(self.playerShip.energy) + '%', False, (255, 255, 255))
        self.screen.blit(score_text, (15, 10))
        pygame.draw.rect(self.screen, (240, 39, 39),
                         [15, 45, self.playerShip.maxHealth-(self.playerShip.maxHealth-self.playerShip.health), 10], 0)
        pygame.draw.rect(self.screen, (255, 255, 255), [15, 45, self.playerShip.maxHealth, 10], 2)
        screen.blit(self.heart[0], (2, 35))
        pygame.draw.rect(self.screen, (7, 82, 184), [15, 70, (100/self.playerShip.maxEnergy)*self.playerShip.energy, 25], 0)
        pygame.draw.rect(self.screen, (255, 255, 255), [15, 70, 100, 25], 2)
        scoreLength = len(str(self.playerShip.energy)) - 1
        self.screen.blit(energy_text, (55 - (scoreLength*5), 75))

    def check_player_hit(self, dt):
        if self.player.invincible is False and self.playerShip.health > 0:
            damaged = False
            for hitbox in self.player.hitboxArray:
                for enemy in self.enemyList:
                    for hurtbox in enemy.hurtboxArray:
                        if self.check_hit(hurtbox, hitbox):
                            damaged = self.player_hit(damaged, enemy.damage)
                            if enemy.enemyShip.category == 'explode':
                                self.explosionArray.add(
                                    ExplosionSprite(enemy.xcor - (enemy.enemyShip.explosion.width - enemy.width) / 2,
                                                    enemy.ycor,
                                                    enemy.enemyShip.explosion.height, enemy.enemyShip.explosion.width,
                                                    enemy.enemyShip.explosion.images, 0,
                                                    enemy.enemyShip.explosionSound, True, False))
                                self.enemyList.remove(enemy)
                            break
                for bullet in self.enemyBulletArray:
                    if self.check_hit(bullet.hurtbox, hitbox):
                        damaged = self.player_hit(damaged, bullet.damage)
                        self.enemyBulletArray.remove(bullet)
                        break
                for explosion in self.explosionArray:
                    if explosion.damage > 0:
                        for hurtbox in explosion.hurtboxArray:
                            # Debug explosion hurtbox
                            # pygame.draw.rect(self.screen, (0, 0, 255), hurtbox, 3)
                            if self.check_hit(hurtbox, hitbox):
                                damaged = self.player_hit(damaged, explosion.damage)
                                break
        elif self.playerShip.health <= 0:
            self.player.invincible = False
            self.gameOver = self.player.dead
        else:
            if self.player.iFrames < self.player.collisionTime:
                self.player.invincible = False
                self.player.collisionTime = 0
            else:
                self.player.collisionTime += dt

    def player_hit(self, damaged, damage):
        if not damaged:
            self.playerShip.health -= damage
            if self.playerShip.health < 0:
                self.playerShip.health = 0
            self.player.invincible = True
            self.playerShip.hitSound.play()
        return True

    def check_enemy_hit(self):
        for bullet in self.bulletArray:
            for enemy in self.enemyList:
                for hitbox in enemy.hitboxArray:
                    if self.check_hit(bullet.hurtbox, hitbox):
                        destoryed = self.check_enemy_destroyed(enemy, bullet.damage)
                        if bullet.playerBullet.explode:
                            self.explosionArray.add(
                                ExplosionSprite(
                                    bullet.xcor - ((bullet.playerBullet.explosion.width / 2) - (bullet.width / 2)),
                                    bullet.ycor - ((bullet.playerBullet.explosion.height / 2) - (bullet.height / 2)),
                                    bullet.playerBullet.explosion.width, bullet.playerBullet.explosion.height,
                                    bullet.playerBullet.explosion.images, 0, bullet.hitSound, 40, True))
                        else:
                            if not bullet.playerBullet.explode and not destoryed:
                                self.explosionArray.add(
                                    ExplosionSprite(bullet.xcor + bullet.width/2, bullet.ycor, bullet.width, bullet.height,
                                              bullet.playerBullet.explosion.images, 0, bullet.hitSound, 0, True))
                        self.bulletArray.remove(bullet)
                        break
        for explosion in self.explosionArray:
            if explosion.damage > 0 and explosion.player is True:
                for enemy in self.enemyList:
                    for hurtbox in explosion.hurtboxArray:
                        for hitbox in enemy.hitboxArray:
                            if self.check_hit(hurtbox, hitbox) and (enemy.id not in explosion.idArray):
                                explosion.idArray.append(enemy.id)
                                self.check_enemy_destroyed(enemy, explosion.damage)

    def check_enemy_destroyed(self, enemy, damage):
        enemy.health = enemy.health - damage
        self.player.playerShip.energy += self.player.playerShip.energyGain
        if self.player.playerShip.energy > self.player.playerShip.maxEnergy:
            self.player.playerShip.energy = self.player.playerShip.maxEnergy
        if enemy.health <= 0:
            if enemy.enemyShip.explosion.width != enemy.enemyShip.width:
                if enemy.enemyShip.category == 'explode':
                    self.explosionArray.add(
                        ExplosionSprite(enemy.xcor - ((enemy.enemyShip.explosion.width - enemy.enemyShip.width) / 2),
                                  enemy.ycor,
                                  enemy.enemyShip.explosion.width, enemy.enemyShip.explosion.height, enemy.enemyShip.explosion.images, 0,
                                  enemy.enemyShip.explosionSound, 40, False))
                else:
                    self.explosionArray.add(
                        ExplosionSprite(enemy.xcor - (enemy.enemyShip.explosion.width - enemy.enemyShip.width) / 2,
                                        enemy.ycor,
                                        enemy.enemyShip.explosion.width, enemy.enemyShip.explosion.height,
                                        enemy.enemyShip.explosion.images, 0,
                                        enemy.enemyShip.explosionSound, 0, True))
            else:
                self.explosionArray.add(
                    ExplosionSprite(enemy.xcor, enemy.ycor, enemy.enemyShip.explosion.width,
                                    enemy.enemyShip.explosion.height,
                                    enemy.enemyShip.explosion.images, 0, enemy.enemyShip.explosionSound, 0, True))
            self.player.score += enemy.enemyShip.score
            self.enemyList.remove(enemy)
            return True
        return False

    def check_hit(self, hurtbox, hitbox):
        if hurtbox[0] + hurtbox[2] > hitbox[0] and hurtbox[0] < hitbox[0] + hitbox[2]:
            if hurtbox[1] + hurtbox[3] > hitbox[1] and hurtbox[1] < hitbox[1] + hitbox[3]:
                return True
        return False

    def shoot_bullet(self):
        # player shoots bullet. shootType can be customized to change the starting position of the bullet and how
        # many bullets shot
        if self.playerShip.shotType == 'Single_Middle':
            bullet = PlayerBulletSprite(self.player.xcor + (self.rect.width / 2 - 5) - 10, self.player.ycor - 12,
                                        self.playerShip.currentBullet.width, self.playerShip.currentBullet.height,
                                        self.playerShip.currentBullet.image, 0, self.playerShip.currentBullet,
                                        self.playerShip, 0)
            self.bulletArray.add(bullet)
            bullet.sound.play()
        elif self.playerShip.shotType == 'Tri_Spread':
            bullet1 = PlayerBulletSprite(self.player.xcor + (self.rect.width / 2 - 5) - 10, self.player.ycor - 12,
                                         self.playerShip.currentBullet.width, self.playerShip.currentBullet.height,
                                         self.playerShip.currentBullet.image, 0, self.playerShip.currentBullet,
                                         self.playerShip, 0)
            bullet2 = PlayerBulletSprite(self.player.xcor + (self.rect.width / 2 - 5) - 10, self.player.ycor - 12,
                                         self.playerShip.currentBullet.width, self.playerShip.currentBullet.height,
                                         self.playerShip.currentBullet.image, 0, self.playerShip.currentBullet,
                                         self.playerShip, .5)
            bullet3 = PlayerBulletSprite(self.player.xcor + (self.rect.width / 2 - 5) - 10, self.player.ycor - 12,
                                         self.playerShip.currentBullet.width, self.playerShip.currentBullet.height,
                                         self.playerShip.currentBullet.image, 0, self.playerShip.currentBullet,
                                         self.playerShip, -.5)
            self.bulletArray.add(bullet1)
            self.bulletArray.add(bullet2)
            self.bulletArray.add(bullet3)
            bullet1.sound.play()
            bullet2.sound.play()
            bullet3.sound.play()

    def use_ability(self):
        # player uses ability.
        if self.playerShip.ability == 'Ion_Blast' or self.playerShip.ability == 'Mini_KZ':
            bullet = PlayerBulletSprite(self.player.xcor, self.player.ycor, self.playerShip.specialBullet.width,
                                        self.playerShip.specialBullet.height,
                                        self.playerShip.specialBullet.image, 0, self.playerShip.specialBullet,
                                        self.playerShip, 0)
            self.bulletArray.add(bullet)
            bullet.sound.play()
        elif self.playerShip.ability == 'Scatter_Shot':
            bullet = PlayerBulletSprite(self.player.xcor + (self.player.rect.width / 2 - 5) - 10, self.player.ycor - 12, self.playerShip.specialBullet.width,
                                        self.playerShip.specialBullet.height,
                                        self.playerShip.specialBullet.image, 0, self.playerShip.specialBullet,
                                        self.playerShip, 0)
            self.bulletArray.add(bullet)
            counter = self.playerShip.specialBullet.counter
            angle = self.playerShip.specialBullet.angle
            bullet.sound.play()
            while counter > 0:
                bullet1 = PlayerBulletSprite(self.player.xcor + (self.player.rect.width / 2 - 5) - 10, self.player.ycor - 12, self.playerShip.specialBullet.width,
                                        self.playerShip.specialBullet.height,
                                        self.playerShip.specialBullet.image, 0, self.playerShip.specialBullet,
                                        self.playerShip, angle)
                bullet2 = PlayerBulletSprite(self.player.xcor + (self.player.rect.width / 2 - 5) - 10,
                                             self.player.ycor - 12, self.playerShip.specialBullet.width,
                                             self.playerShip.specialBullet.height,
                                             self.playerShip.specialBullet.image, 0, self.playerShip.specialBullet,
                                             self.playerShip, -angle)
                self.bulletArray.add(bullet1)
                self.bulletArray.add(bullet2)
                counter -= 1
                angle += 1
        self.bulletTimer = self.playerShip.fireRate
        return self.bulletTimer

    def move_bullets(self, dt):
        # moves all player bullets on the screen and removes them when they leave the screen shows bullet hurtbox
        for bullet in self.bulletArray:
            bullet.move()
            bullet.update(self.screen, dt)
            # Debug player bullet
            # pygame.draw.rect(self.screen, (0, 0, 255), bullet.hurtbox, 1)
            if bullet.ycor < -20 or bullet.ycor > self.windowHeight + 20:
                self.bulletArray.remove(bullet)
        for bullet in self.enemyBulletArray:
            bullet.move()
            bullet.update(self.screen, dt)
            # Debug enemy bullet
            # pygame.draw.rect(self.screen, (0, 0, 255), bullet.hurtbox, 1)
            if bullet.ycor < -20 or bullet.ycor > 770:
                self.enemyBulletArray.remove(bullet)

    # Use to determine where to spawn enemies and the type of enemies that come out in each spawn section.
    def spawn_enemies(self, section, dt):
        section.CD -= dt
        if section.CD <= 0:
            section.CD = random.uniform(section.earliestCD, section.latestCD)
            chosenFormation = random.choice(self.formationList)
            for formation in chosenFormation.placement:
                if formation[0] == 0:
                    self.enemyList.add(random.choice(self.enemyType).create_enemy_sprite(section.startPoint + formation[1], section.yaxis + formation[2]))
                elif formation[0] == 1:
                    self.enemyList.add(random.choice(self.enemyType).create_enemy_sprite(section.midPoint + formation[1], section.yaxis + formation[2]))
                else:
                    self.enemyList.add(
                        random.choice(self.enemyType).create_enemy_sprite(section.endPoint + formation[1],
                                                                          section.yaxis + formation[2]))

    def move_enemies(self, dt):
        # moves all enemies on the screen and removes them when they leave the screen
        for i in self.enemyList:
            i.move(self.windowWidth)
            if i.enemyShip.hasAbility and i.ability_timer(dt):
                self.enemyBulletArray = i.enemyShip.use_ability(i, self.enemyBulletArray)
            i.update(self.screen, dt)
            # Debug Enemy. Shows enemy hitboxes in red rectangle.
            # for hitbox in i.hitboxArray:
            #     pygame.draw.rect(self.screen, (255, 0, 0), hitbox, 3)
            # for hurtbox in i.hurtboxArray:
            #     pygame.draw.rect(self.screen, (0, 0, 255), hurtbox, 3)
            if i.ycor > self.windowHeight + 96:
                self.enemyList.remove(i)

    def game_over(self):
        return self.gameOver

    def get_score(self):
        return self.player.score
