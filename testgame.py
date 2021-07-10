import pygame

pygame.init()

win = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Test")
clock = pygame.time.Clock()

stand = pygame.image.load('./zelda/stand.png')

walk_down = [pygame.image.load("./zelda/animation/down1.png"), pygame.image.load("./zelda/animation/down2.png"),
             pygame.image.load("./zelda/animation/down3.png"), pygame.image.load("./zelda/animation/down4.png"),
             pygame.image.load("./zelda/animation/down5.png"), pygame.image.load("./zelda/animation/down6.png"),
             pygame.image.load("./zelda/animation/down7.png"), pygame.image.load("./zelda/animation/down8.png"),
             pygame.image.load("./zelda/animation/down9.png")]

walk_up = [pygame.image.load('./zelda/animation/up1.png'), pygame.image.load('./zelda/animation/up2.png'),
           pygame.image.load('./zelda/animation/up3.png'), pygame.image.load('./zelda/animation/up4.png'),
           pygame.image.load('./zelda/animation/up5.png'), pygame.image.load('./zelda/animation/up6.png'),
           pygame.image.load('./zelda/animation/up7.png'), pygame.image.load('./zelda/animation/up8.png'),
           pygame.image.load('./zelda/animation/up9.png')]

walk_left = [pygame.image.load('./zelda/animation/left1.png'), pygame.image.load('./zelda/animation/left2.png'),
             pygame.image.load('./zelda/animation/left3.png'), pygame.image.load('./zelda/animation/left4.png'),
             pygame.image.load('./zelda/animation/left5.png'), pygame.image.load('./zelda/animation/left6.png'),
             pygame.image.load('./zelda/animation/left7.png'), pygame.image.load('./zelda/animation/left8.png'),
             pygame.image.load('./zelda/animation/left9.png')]

walk_right = [pygame.image.load('./zelda/animation/right1.png'), pygame.image.load('./zelda/animation/right2.png'),
              pygame.image.load('./zelda/animation/right3.png'), pygame.image.load('./zelda/animation/right3.png'),
              pygame.image.load('./zelda/animation/right5.png'), pygame.image.load('./zelda/animation/right6.png'),
              pygame.image.load('./zelda/animation/right7.png'), pygame.image.load('./zelda/animation/right8.png'),
              pygame.image.load('./zelda/animation/right9.png')]

background = pygame.image.load("background.png")

pygame.mixer.music.load("19 - AcyOrt.wav")
pygame.mixer.music.play(-1)

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walk_count = 0
        self.Right = False
        self.Left = False
        self.isJump = False
        self.Up = False
        self.Down = False
        self.jumpCount = 0
        self.vel = 5

    def draw(self, win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        if self.Left:
            win.blit(walk_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

        elif self.Right:
            win.blit(walk_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

        elif self.Up:
            win.blit(walk_up[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

        elif self.Down:
            win.blit(walk_down[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

        else:
            win.blit(stand, (self.x, self.y))
            self.walk_count = 0

def redrawGameWindow():
    win.blit(background, (0, 0))
    man.draw(win)
    pygame.display.update()

man = Player(200, 410, 32, 42)
run = True

while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.Left = True
        man.Right = False
        man.Up = False
        man.Down = False

    elif keys[pygame.K_RIGHT] and man.x < 800 - man.width - man.vel:
        man.x += man.vel
        man.Right = True
        man.Up = False
        man.Down = False
        man.Left = False

    elif keys[pygame.K_DOWN] and man.y < 480 - man.height - man.vel:
        man.y += man.vel
        man.Right = False
        man.Up = False
        man.Down = True
        man.Left = False

    elif keys[pygame.K_UP] and man.y > man.vel:
        man.y -= man.vel
        man.Right = False
        man.Up = True
        man.Down = False
        man.Left = False

    else:
        man.Right = False
        man.Left = False
        man.Up = False
        man.Down = False
        man.walk_count = 0

    if not man.isJump:
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.Right = False
            man.Left = False
            man.Up = False
            man.Down = False
            man.walk_count = 0

    else:
        if man.jumpCount >= -10:
            man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.07
            man.jumpCount -= 1
        else:
            man.jumpCount = 10
            man.isJump = False

    redrawGameWindow()
pygame.quit()
