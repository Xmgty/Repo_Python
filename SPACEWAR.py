import pygame
import sys
import random




window = pygame.display.set_mode((800, 700))
pygame.display.set_caption('Spacewar')
screen = pygame.Surface((800, 700))
screen2 = (720, 530)
screen3 = (720, 530)
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

    self.centerx = 350
    self.centery = 300

    self.speed = 10

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



###### МЕТЕОРИТЫ


class Meteor():
    def __init__(self):
        self.height = 5
        self.width = 5

        self.curIMG = pygame.image.load("images/Enemy.png")
        self.curvIMG = pygame.image.load("images/Enemy.png")
        self.curvaIMG = pygame.image.load("images/Enemy.png")

        self.speed = 5
        ### Начальные координаты
        self.centerx = random.randint(100, 500)
        self.centery = 0


        self.moveLeft, self.moveRight, self.moveUp, self.moveDown = False, False, False, False
        self.moveLeft1, self.moveRight1, self.moveUp1, self.moveDown1 = False, False, False, False
        self.moveLeft2, self.moveRight2, self.moveUp2, self.moveDown2 = False, False, False, False


        self.rect = pygame.Rect(self.centerx - self.width / 2, self.centery - self.height / 2, self.width, self.height)
        self.rect1 = pygame.Rect(self.centerx - self.width / 2, self.centery - self.height / 2, self.width, self.height)
        self.rect2 = pygame.Rect(self.centerx - self.width / 2, self.centery - self.height / 2, self.width, self.height)
    def update(self):
        if self.moveLeft and self.rect.left > 0:
            self.rect.centerx -= self.speed
        if self.moveRight and self.rect.right < screen3[0] - 1:
            self.rect.centerx += self.speed
        if self.moveUp and self.rect.top > 0:
            self.rect.centery -= self.speed
        if self.moveDown and self.rect.bottom < screen3[1] - 1:
            self.rect.centery += self.speed


    def update1(self):
        if self.moveLeft1 and self.rect1.left > 0:
            self.rect1.centerx -= self.speed
        if self.moveRight1 and self.rect1.right < screen3[0] - 1:
            self.rect1.centerx += self.speed
        if self.moveUp1 and self.rect1.top > 0:
            self.rect1.centery -= self.speed
        if self.moveDown1 and self.rect1.bottom < screen3[1] - 1:
            self.rect1.centery += self.speed

    def update2(self):
        if self.moveLeft2 and self.rect2.left > 0:
            self.rect2.centerx -= self.speed
        if self.moveRight2 and self.rect2.right < screen3[0] - 1:
            self.rect2.centerx += self.speed
        if self.moveUp2 and self.rect2.top > 0:
            self.rect2.centery -= self.speed
        if self.moveDown2 and self.rect2.bottom < screen3[1] - 1:
            self.rect2.centery += self.speed

    def render(self):
        window.blit(self.curIMG, self.rect)
    def render1(self):
        window.blit(self.curvIMG, self.rect1)

    def render2(self):
        window.blit(self.curvaIMG, self.rect2)




##### БЭКГРАУНД


background = pygame.image.load('images/I5ram.png')
background_size = background.get_size()
background_rect = background.get_rect()
screens = pygame.display.set_mode([900, 600])

clock=pygame.time.Clock()



w,h = background_size
x = 0
y = 0

x1 = 0
y1 = -h



def terminate():
    pygame.quit()
    sys.exit()


###### ЗВУК


pygame.mixer.init()
pygame.mixer.music.load('audio/sp1.mp3')
pygame.mixer.music.play(0)

############ СПАУН









# КОРАБЛЬ В БГ
run = True
meteor = Meteor()
spaceship = Spaceship()
flag = 0
qwer = 0
qwer1 = 0
qwer2 = 0
sub2 = 0
sub1 = 0
sub = 0
count = 0
count1 = 0
count2 = 0
frames = 0
while run:
    FPS = 36


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



######################### ДВИЖЕНИЕ ENEMY РАБОТАТЬ НАДО

    if count < 45:
         meteor.moveDown = True
         meteor.moveUp = False
         count += 1
    else:
        meteor.moveDown = False
        meteor.moveUp = False
    if count1 < 155:
         meteor.moveDown1 = True
         meteor.moveUp1 = False
         count1 += 1
    else:
        meteor.moveDown1 = False
        meteor.moveUp1 = False
    if qwer1 < 85:
        meteor.moveRight1 = True
        meteor.moveLeft1 = False
        qwer1+=1
        if qwer1 == 84:
            sub1 = 0
    elif sub1 < 85:
        meteor.moveRight1 = False
        meteor.moveLeft1 = True
        sub1+=1
        if sub1 == 84:
            qwer1 = 0
    if qwer < 125:
        meteor.moveRight = False
        meteor.moveLeft = True
        qwer+=1
        if qwer == 124:
            sub = 0
    elif sub < 125:
        meteor.moveRight = True
        meteor.moveLeft = False
        sub+=1
        if sub == 124:
            qwer = 0
    if qwer2 < 185:
        meteor.moveDown2 = False
        meteor.moveUp2 = False
        meteor.moveRight2 = True
        meteor.moveLeft2 = False
        qwer2 += 1
        if qwer2 == 184:
            sub2 = 0
    elif sub2 < 185:
        meteor.moveDown2 = False
        meteor.moveUp2 = False
        meteor.moveRight2 = False
        meteor.moveLeft2 = True
        sub2 += 1
        if sub2 == 184:
            qwer2 = 0



#####################################
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

    frames += 1




    meteor.update()
    meteor.render()
    if frames > 128:
        meteor.update1()
        meteor.render1()
    if frames > 256:
        meteor.update2()
        meteor.render2()
    spaceship.update()
    spaceship.render()
    pygame.display.update()
    clock.tick(FPS)