# importation for pygame, MainMenuView and View and Sprite class
import pygame
import View.MainMenuView as Main
import View.PlayerControlView as Controls
from Model.ViewShipFactory import ShipViewFactory
from View.ParentView import View, spritesFolder
# Ship select view controls ship select menu


class ShipSelectView(View):
    # ShipSelectView, child class of ParentView
    def __init__(self):
        super(ShipSelectView, self).__init__()
        self.name = "ShipSelect"
        self.bg = pygame.image.load(spritesFolder + 'Menu/Select_Page.png')
        # 146x44
        self.backButton = ButtonOption("back", pygame.image.load(spritesFolder + 'Options/Back.png'),
                                       pygame.image.load(spritesFolder + 'Options/Back_Highlighted.png'), 25, 675)
        self.playButton = ButtonOption("play", pygame.image.load(spritesFolder + 'Options/Play.png'),
                                       pygame.image.load(spritesFolder + 'Options/H_Play.png'), 529, 675)
        self.leftArrow = ButtonOption("left", pygame.image.load(spritesFolder + 'Options/Left_Arrow.png'),
                                      pygame.image.load(spritesFolder + 'Options/Left_Arrow_Highlighted.png'), 67, 425)
        self.rightArrow = ButtonOption("right", pygame.image.load(spritesFolder + 'Options/Right_Arrow.png'),
                                       pygame.image.load(spritesFolder + 'Options/Right_Arrow_Highlighted.png'), 218, 425)
        self.index = 0
        ViewInfinity = ShipViewFactory.create_view_ship("ViewInfinity")
        ViewImperier = ShipViewFactory.create_view_ship("ViewImperier")
        ViewScatter = ShipViewFactory.create_view_ship("ViewScatter")
        self.ships = [ViewInfinity, ViewImperier, ViewScatter]

    def draw(self, mouse, dt):
        # repeatedly draws the screen, must provide: (mouse position, milliseconds since last frame)
        self.screen.blit(self.bg, (0, 0))
        # pygame.draw.rect(self.screen, (255, 255, 255),
        # (self.baseShip.xcor - 20, self.baseShip.ycor - 15, 100, 100), 2)
        self.ships[self.index].images.update(self.screen, dt)
        self.ships[self.index].shotImage.update(self.screen, dt)
        self.ships[self.index].abilityImages.update(self.screen, dt)
        self.display_text()
        self.display_button(mouse)
        pygame.display.update()

    def display_button(self, mouse):
        # displays back button. Highlights if hovered
        if self.backButton.xAxis + 146 > mouse[0] > self.backButton.xAxis and self.backButton.yAxis + 44 > mouse[
            1] > self.backButton.yAxis:
            self.screen.blit(self.backButton.highlighted, (self.backButton.xAxis, self.backButton.yAxis))
            self.screen.blit(self.playButton.unhighlighted, (self.playButton.xAxis, self.playButton.yAxis))
            self.screen.blit(self.leftArrow.unhighlighted, (self.leftArrow.xAxis, self.leftArrow.yAxis))
            self.screen.blit(self.rightArrow.unhighlighted, (self.rightArrow.xAxis, self.rightArrow.yAxis))
        elif self.playButton.xAxis + 146 > mouse[0] > self.playButton.xAxis and self.playButton.yAxis + 44 > mouse[
            1] > self.playButton.yAxis:
            self.screen.blit(self.playButton.highlighted, (self.playButton.xAxis, self.playButton.yAxis))
            self.screen.blit(self.backButton.unhighlighted, (self.backButton.xAxis, self.backButton.yAxis))
            self.screen.blit(self.leftArrow.unhighlighted, (self.leftArrow.xAxis, self.leftArrow.yAxis))
            self.screen.blit(self.rightArrow.unhighlighted, (self.rightArrow.xAxis, self.rightArrow.yAxis))
        elif self.leftArrow.xAxis + 64 > mouse[0] > self.leftArrow.xAxis and self.leftArrow.yAxis + 64 > mouse[
            1] > self.leftArrow.yAxis:
            self.screen.blit(self.backButton.unhighlighted, (self.backButton.xAxis, self.backButton.yAxis))
            self.screen.blit(self.playButton.unhighlighted, (self.playButton.xAxis, self.playButton.yAxis))
            self.screen.blit(self.leftArrow.highlighted, (self.leftArrow.xAxis, self.leftArrow.yAxis))
            self.screen.blit(self.rightArrow.unhighlighted, (self.rightArrow.xAxis, self.rightArrow.yAxis))
        elif self.rightArrow.xAxis + 64 > mouse[0] > self.rightArrow.xAxis and self.rightArrow.yAxis + 64 > mouse[
            1] > self.rightArrow.yAxis:
            self.screen.blit(self.backButton.unhighlighted, (self.backButton.xAxis, self.backButton.yAxis))
            self.screen.blit(self.playButton.unhighlighted, (self.playButton.xAxis, self.playButton.yAxis))
            self.screen.blit(self.leftArrow.unhighlighted, (self.leftArrow.xAxis, self.leftArrow.yAxis))
            self.screen.blit(self.rightArrow.highlighted, (self.rightArrow.xAxis, self.rightArrow.yAxis))
        else:
            self.screen.blit(self.backButton.unhighlighted, (self.backButton.xAxis, self.backButton.yAxis))
            self.screen.blit(self.playButton.unhighlighted, (self.playButton.xAxis, self.playButton.yAxis))
            self.screen.blit(self.leftArrow.unhighlighted, (self.leftArrow.xAxis, self.leftArrow.yAxis))
            self.screen.blit(self.rightArrow.unhighlighted, (self.rightArrow.xAxis, self.rightArrow.yAxis))

    def click_event(self, mouse):
        # returns MainMenuView if an button is clicked. Otherwise it returns self. Must provide: (mouse position)
        if self.backButton.xAxis + 146 > mouse[0] > self.backButton.xAxis and self.backButton.yAxis + 44 > mouse[
            1] > self.backButton.yAxis:
            self.transition()
            return Main.MainMenuView()
        if self.playButton.xAxis + 146 > mouse[0] > self.playButton.xAxis and self.playButton.yAxis + 44 > mouse[
            1] > self.playButton.yAxis:
            self.transition()
            return Controls.PlayerControlView(self.ships[self.index].name)
        elif self.leftArrow.xAxis + 64 > mouse[0] > self.leftArrow.xAxis and self.leftArrow.yAxis + 64 > mouse[
            1] > self.leftArrow.yAxis:
            self.index -= 1
            if self.index < 0:
                self.index = len(self.ships) - 1
            return self
        elif self.rightArrow.xAxis + 64 > mouse[0] > self.rightArrow.xAxis and self.rightArrow.yAxis + 64 > mouse[
            1] > self.rightArrow.yAxis:
            self.index += 1
            if self.index >= len(self.ships):
                self.index = 0
            return self
        else:
            return self

    def key_event(self, key):
        # returns to MainMenuView after user pushes escape. Otherwise returns self. Must provide: (key pressed)
        if key[pygame.K_ESCAPE]:
            self.transition()
            return Main.MainMenuView()
        elif key[pygame.K_KP_ENTER] or key[pygame.K_RETURN]:
            self.transition()
            return Controls.PlayerControlView(self.ships[self.index].name)
        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            self.index -= 1
            if self.index < 0:
                self.index = len(self.ships) - 1
            return self
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.index += 1
            if self.index >= len(self.ships):
                self.index = 0
            return self
        else:
            return self

    def display_text(self):
        pygame.font.init()
        allFonts = pygame.font.get_fonts()
        font = pygame.font.SysFont(allFonts[8], 30)
        sm_font = pygame.font.SysFont(allFonts[8], 26)
        text = font.render(self.ships[self.index].name, False, (255, 255, 255))
        text_rect = text.get_rect(center=(self.windowWidth / 4, 600))
        text_health = sm_font.render('Health', False, (255, 255, 255))
        text_damage = sm_font.render('Damage', False, (255, 255, 255))
        text_fire_rate = sm_font.render('Fire Rate', False, (255, 255, 255))
        text_speed = sm_font.render('Speed', False, (255, 255, 255))
        text_shot_type = sm_font.render('Shot Type:', False, (255, 255, 255))
        text_ability = sm_font.render('Ability:', False, (255, 255, 255))
        temp = self.ships[self.index].health
        spacing = 0
        while temp > 0:
            pygame.draw.rect(self.screen, (8, 101, 255), [325 + spacing, 355, 30, 5], 0)
            pygame.draw.rect(self.screen, (4, 89, 201), [325 + spacing, 360, 30, 5], 0)
            spacing += 35
            temp -= 1
        temp = self.ships[self.index].damage
        spacing = 0
        while temp > 0:
            pygame.draw.rect(self.screen, (8, 101, 255), [325 + spacing, 430, 30, 5], 0)
            pygame.draw.rect(self.screen, (4, 89, 201), [325 + spacing, 435, 30, 5], 0)
            spacing += 35
            temp -= 1
        temp = self.ships[self.index].fireRate
        spacing = 0
        while temp > 0:
            pygame.draw.rect(self.screen, (8, 101, 255), [325 + spacing, 505, 30, 5], 0)
            pygame.draw.rect(self.screen, (4, 89, 201), [325 + spacing, 510, 30, 5], 0)
            spacing += 35
            temp -= 1
        temp = self.ships[self.index].speed
        spacing = 0
        while temp > 0:
            pygame.draw.rect(self.screen, (8, 101, 255), [325 + spacing, 580, 30, 5], 0)
            pygame.draw.rect(self.screen, (4, 89, 201), [325 + spacing, 585, 30, 5], 0)
            spacing += 35
            temp -= 1
        self.screen.blit(text_health, (325, 325))
        self.screen.blit(text_damage, (325, 400))
        self.screen.blit(text_fire_rate, (325, 475))
        self.screen.blit(text_speed, (325, 550))
        self.screen.blit(text_shot_type, (500, 325))
        self.screen.blit(sm_font.render(self.ships[self.index].shotType, False, (255, 255, 255)), (496, 430))
        self.screen.blit(text_ability, (516, 475))
        self.screen.blit(sm_font.render(self.ships[self.index].ability, False, (255, 255, 255)), (486, 570))
        self.screen.blit(text, text_rect)


class ButtonOption(object):
    # button option class. (name of button, unhighlighted image of button, highlighted image of button, x axis, y axis)
    def __init__(self, name, unhighlighted, highlighted, xAxis, yAxis):
        self.name = name
        self.unhighlighted = unhighlighted
        self.highlighted = highlighted
        self.xAxis = xAxis
        self.yAxis = yAxis



