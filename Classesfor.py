import pygame
import random

WIDTH = 900
HEIGHT = 700
FPS = 60
pygame.init()
screen = pygame.Surface((WIDTH, HEIGHT))



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
        self.dx = random.randrange(-2, 2)
        self.height = 30
        self.width = 150
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
            exit()

def main():
# Initialize Everything
    background = pygame.image.load('images/I5ram.png')
    background_size = background.get_size()
    background_rect = background.get_rect()
    screen = pygame.display.set_mode(background_size)

    pygame.display.set_caption('UoN Invaders')
    w, h = background_size
    x = 0
    y = 0

    x1 = 0
    y1 = -h

    screen.blit(background, background_rect)


# МУЗЫКА

    music = pygame.mixer.music.load ("audio/sp1.mp3")
    pygame.mixer.music.play(-1)



# ИНИЦИАЛИЗАЦИЯ ИГРОВЫХ ОБЪЕКТОВ
    global clock

    clock = pygame.time.Clock()

    i = 0
    i += 1




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

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

                going = False

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

if __name__ == '__main__':

    main()