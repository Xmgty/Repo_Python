import pygame
import sys





window = pygame.display.set_mode((800, 700))
pygame.display.set_caption('Spacewar')
screen = pygame.Surface((800, 700))
screen2 = (640, 480)
info = pygame.Surface((800, 30))



class Menu:
    def __init__(self, punkts=[400, 350, u'Punkt', (250, 250, 30), (250, 30, 250)]):
        self.punkts = punkts

    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1] - 30))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1] - 30))

    def menu(self):
        done = True
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            info.fill((0, 100, 200))
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        exit()
            window.blit(info, (0, 0))
            window.blit(screen, (0, 30))
            pygame.display.flip()





pygame.font.init()
score_f = pygame.font.SysFont('Arial', 32)
lifes_f = pygame.font.SysFont('Arial', 32)
end = pygame.font.SysFont('Times new roman', 80)
again = pygame.font.SysFont('Times new roman', 40)

punkts = [(350, 300, u'Play', (11, 0, 77), (250, 250, 30), 0),
          (350, 340, u'Exit', (11, 0, 77), (250, 250, 30), 1)]
game = Menu(punkts)
game.menu()


#### КОРАБЛЬ

class Spaceship():
  def __init__(self):
    self.height = 32
    self.width = 28

    self.ssIMG = pygame.image.load("images/Spaceship.png")

    self.centerx = 320
    self.centery = 240

    self.speed = 5

    self.moveLeft, self.moveRight, self.moveUp, self.moveDown = False, False, False, False

    self.rect = pygame.Rect(self.centerx - self.width / 2, self.centery - self.height / 2, self.width, self.height)

  def update(self):
        if self.moveLeft and self.rect.left > 0:
            self.rect.centerx -= self.speed
        if self.moveRight and self.rect.right < screen2[0] - 1:
            self.rect.centerx += self.speed
        if self.moveUp and self.rect.top > 0:
            self.rect.centery -= self.speed
        if self.moveDown and self.rect.bottom < screen2[1] - 1:
            self.rect.centery += self.speed

  def render(self):
     window.blit(self.ssIMG, self.rect)














##### БЭКГРАУНД

theClock = pygame.time.Clock()
background = pygame.image.load('images/I5ram.png')
background_size = background.get_size()
background_rect = background.get_rect()
screens = pygame.display.set_mode([800, 700])
w,h = background_size
x = 0
y = 0

x1 = 0
y1 = -h


def terminate():
    pygame.quit()
    sys.exit()


# КОРАБЛЬ В БГ

run = True
spaceship = Spaceship()
while run:
    screens.blit(background,background_rect)

    y1 += 5
    y += 5
    screens.blit(background,(x,y))
    screens.blit(background,(x1,y1))
# Если выйдем за границы изображения
    if y > h:
        y = -h
    if y1 > h:
        y1 = -h


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()
            if event.key == pygame.K_UP:
                spaceship.moveUp = True
                spaceship.moveDown = False
            if event.key == pygame.K_DOWN:
                spaceship.moveUp = False
                spaceship.moveDown = True
            if event.key == pygame.K_LEFT:
                spaceship.moveRight = False
                spaceship.moveLeft = True
            if event.key == pygame.K_RIGHT:
                spaceship.moveRight = True
                spaceship.moveLeft = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                spaceship.moveUp = False
            if event.key == pygame.K_DOWN:
                 spaceship.moveDown = False
            if event.key == pygame.K_LEFT:
                spaceship.moveLeft = False
            if event.key == pygame.K_RIGHT:
                 spaceship.moveRight = False

    spaceship.update()
    spaceship.render()
    pygame.display.update()











