import pygame
import random
import sys

WIDTH = 900
HEIGHT = 700
FPS = 60
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.Surface((900, 700))
info = pygame.Surface((900, 700))
pygame.display.set_caption('Space Invaders')
black = (0,0,0)
white = (255, 255, 255)
yellow = (255, 255, 30)
red = (255, 0, 0)

















class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.height = 30
        self.width = 50
        self.lasertimer = 0
        self.lasermax = 10
        self.image = pygame.image.load("images/Spaceship.png")

        self.centerx = 350
        self.centery = 500

        self.speed = 12

        self.moveLeft, self.moveRight, self.moveUp, self.moveDown, self.Shoot = False, False, False, False, False

        self.rect = pygame.Rect(self.centerx - self.width / 2, self.centery - self.height / 2, self.width, self.height)

    def update(self):
        if self.moveLeft and self.rect.left > 0:
            self.rect.centerx -= self.speed
        if self.moveRight and self.rect.right < 800:
            self.rect.centerx += self.speed
        if self.moveUp and self.rect.top > 0:
            self.rect.centery -= self.speed
        if self.moveDown and self.rect.bottom < 500:
            self.rect.centery += self.speed



        # Lasers
        if self.Shoot == True:
            self.lasertimer = self.lasertimer + 1
            if self.lasertimer == self.lasermax:
                laserSprites.add(Laser(self.rect.midtop))
                self.lasertimer = 1



    def render(self):
        screen.blit(self.image, self.rect)

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/beam1.png')
        self.height = 20
        self.width = 20
        self.centerx = 400
        self.centery = 400
        self.rect = pygame.Rect(self.centerx - self.width / 2, self.centery - self.height / 2, self.width, self.height)
        self.rect.center = pos

    def update(self):
        if self.rect.right > 700:
            self.kill()
        else:
            self.rect.move_ip(0, -15)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/Enemy.png')
        self.dy = 6
        self.centerx = random.randint(100, 800)
        self.centery = 0
        self.dx = random.randrange(-4, 4)
        self.height = 20
        self.width = 50
        self.rect = pygame.Rect(self.centerx - self.width / 2, self.centery - self.height / 2, self.width, self.height)


    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top > 600:
            self.kill()

        # ЛАЗЕР попадание
        if pygame.sprite.groupcollide(enemySprites, laserSprites, 1, 1):
           explosionSprites.add(EnemyExplosion(self.rect.center))

        # Враг попадание в игрока
        if pygame.sprite.groupcollide(enemySprites, playerSprite, 1, 1):
           explosionSprites.add(EnemyExplosion(self.rect.center))
           explosionSprites.add(PlayerExplosion(self.rect.center))





    #   Функция для автореспауна если вылетел за горизонт
    # def reset(self):
    #     self.rect.bottom = 0
    #     self.rect.centerx = random.randrange(200, 600)
    #     self.dy = random.randrange(4, 5)
    #     self.dx = random.randrange(-2, 2)

    def spawn(FPS, total_frames):
        ping = FPS
        ping2 = FPS


        if (total_frames % ping == 0):
            r = random.randint(1, 3)
            if r == 2:
                enemySprites.add(Enemy(300))
            if r == 1:
                enemySprites.add(Enemy(400))
            if r == 3:
                enemySprites.add(Enemy(200))
                enemySprites.add(Enemy(500))


class EnemyExplosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/explosion.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.counter = 0
        self.maxcount = 10

    def update(self):
        self.counter = self.counter + 1
        if self.counter == self.maxcount:
            self.kill()

class PlayerExplosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/explosion.png')
        self.height = 100
        self.width = 0
        self.centerx = 0
        self.centery = 0
        self.rect = pygame.Rect(self.centerx - self.width / 2, self.centery - self.height / 2, self.width, self.height)
        self.rect.center = pos
        self.counter = 0
        self.maxcount = 10

    def update(self):
        self.counter = self.counter + 1
        if self.counter == self.maxcount:
            self.kill()
            pygame.mixer.music.stop()
            game.menu()

def main():
# Фон загрузка
    background = pygame.image.load('images/I5ram.png')
    background_size = background.get_size()
    background_rect = background.get_rect()
    screen = pygame.display.set_mode(background_size)


    w, h = background_size
    x = 0
    y = 0

    x1 = 0
    y1 = -h



# МУЗЫКА

    music = pygame.mixer.music.load ("audio/sp1.mp3")
    pygame.mixer.music.play(-1)



# ИНИЦИАЛИЗАЦИЯ ИГРОВЫХ ОБЪЕКТОВ
    global clock

    clock = pygame.time.Clock()

    i = 0





    global player

    player = Player()


# ОБНОВЛЯЕМЫЕ ОБЪЕКТЫ


    # ИГРОК
    global playerSprite
    playerSprite = pygame.sprite.RenderPlain((player))

    # ВРАГ
    global enemySprites
    enemySprites = pygame.sprite.RenderPlain(())
    enemySprites.add(Enemy(200))
    enemySprites.add(Enemy(300))



    # СНАРЯДЫ
    global laserSprites
    laserSprites = pygame.sprite.RenderPlain(())

    # ПОПАДАНИЯ
    global enemyExplosion
    enemyExplosion = pygame.sprite.RenderPlain(())
    global playerExplosion
    playerExplosion = pygame.sprite.RenderPlain(())
    global explosionSprites
    explosionSprites = pygame.sprite.RenderPlain(())



# ГЛАВНЫЙ ЦИКЛ
    total_frames = 0
    going = True

    while going:



        # ФОН,БГ
        y1 += 5
        y += 5
        screen.blit(background, (x, y))
        screen.blit(background, (x1, y1))
        # Если выйдем за границы изображения
        if y > h:
            y = -h
        if y1 > h:
            y1 = -h



        total_frames += 1
        clock.tick(FPS)
        Enemy.spawn(FPS, total_frames)



        # ИВЕНТЫ НАЖАТИЕ КЛАВИШ

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.moveUp = True
                    player.moveDown = False
                if event.key == pygame.K_DOWN:
                    player.moveUp = False
                    player.moveDown = True
                if event.key == pygame.K_LEFT:
                    player.moveRight = False
                    player.moveLeft = True
                if event.key == pygame.K_RIGHT:
                    player.moveRight = True
                    player.moveLeft = False
                if event.key == pygame.K_SPACE:
                    player.Shoot = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.moveUp = False
                if event.key == pygame.K_DOWN:
                    player.moveDown = False
                if event.key == pygame.K_LEFT:
                    player.moveLeft = False
                if event.key == pygame.K_RIGHT:
                    player.moveRight = False
                if event.key == pygame.K_SPACE:
                    player.Shoot = False



            if event.type == pygame.QUIT:

                going = False
                exit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

                going = False
                pygame.mixer.music.stop()
                game.menu()

        # ОБНОВЛЕНИЯ
        player.update()
        player.render()
        enemySprites.update()
        laserSprites.update()
        enemyExplosion.update()
        playerExplosion.update()
        explosionSprites.update()






        # ОТОБРАЖЕНИЕ

        playerSprite.draw(screen)
        enemySprites.draw(screen)
        laserSprites.draw(screen)
        enemyExplosion.draw(screen)
        playerExplosion.draw(screen)
        explosionSprites.draw(screen)

        pygame.display.update()
        clock.tick(FPS)




    pygame.quit()





class Menu:
    def __init__(self, punkts=[400, 350, u'Punkt', (250, 250, 30), (255, 255, 30)]):
        self.punkts = punkts

    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1] - 30))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1] - 30))

    def menu(self):
        done = True
        font_menu = pygame.font.Font(None, 90)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            info.fill((0, 0, 0))
            screen.fill((0, 0, 0))

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
                        if __name__ == '__main__':
                            main()
                    elif punkt == 1:
                        exit()
            window.blit(info, (0, 0))
            window.blit(screen, (0, 0))
            pygame.display.flip()






pygame.font.init()

punkts = [(360, 300, u'PLAY', (255, 255, 255), (0, 0, 255), 0),
          (360, 380, u'EXIT', (255, 255, 255), (255, 0, 0), 1),
          (200, 100, u'Space Invaders', (250, 250, 30), (250, 250, 30), 2)]
game = Menu(punkts)
game.menu()