import pygame
import sys
from enum import Enum
import random


class Snake:
    class Body:
        coordX = None
        coordY = None

        def __init__(self, x, y):
            self.coordX = x
            self.coordY = y

    class Direction(Enum):
        Up = 1
        Down = 2
        Right = 3
        Left = 4

    timer = None
    snake = [Body(0, 0)]
    direction = None
    squareSize = None
    HEIGHT = squareSize = None
    WIDTH = squareSize = None
    bg_color = None
    appleID = None

    def keys_eventer(self, event):
        if event.type == pygame.KEYDOWN:
            match event.key: 
                case pygame.K_UP:
                    if self.direction == self.Direction.Left or self.direction == self.Direction.Right:
                        self.direction = self.Direction.Up

                case pygame.K_DOWN:
                    if self.direction == self.Direction.Left or self.direction == self.Direction.Right:
                        self.direction = self.Direction.Down

                case pygame.K_LEFT:
                    if self.direction == self.Direction.Up or self.direction == self.Direction.Down:
                        self.direction = self.Direction.Left

                case pygame.K_RIGHT:
                    if self.direction == self.Direction.Up or self.direction == self.Direction.Down:
                        self.direction = self.Direction.Right
                
                case pygame.K_KP_PLUS:
                    self.timer += 1

                case pygame.K_KP_MINUS:
                    self.timer -= 1

    def eating(self):
        if self.snake[0].coordX == self.appleID[0] and self.snake[0].coordY == self.appleID[1]:
            while True :
                void = True
                self.appleID[0] = random.randrange(0, 800, 40)
                self.appleID[1] = random.randrange(0, 800, 40)
                for i in range(0, len(self.snake)):
                    if self.appleID[0] == self.snake[i].coordX and self.appleID[1] == self.snake[i].coordY:
                        void = False
                if void == True:
                    break
            pygame.mixer.music.load('eating.mp3')
            pygame.mixer.music.play(0)
            self.snake.append(self.Body(0, 0))

    def game_process(self, screen, clock):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                self.keys_eventer(event)
            self.eating()

            for i in range(len(self.snake)-1, 1, -1):
                self.snake[i].coordX = self.snake[i-1].coordX
                self.snake[i].coordY = self.snake[i-1].coordY

            if len(self.snake) > 1:
                self.snake[1].coordX = self.snake[0].coordX
                self.snake[1].coordY = self.snake[0].coordY
            self.mooving()
            screen.fill(self.bg_color)

            pygame.draw.rect(screen, (255, 0, 0), ((
                self.appleID[0], self.appleID[1]), (self.squareSize, self.squareSize)))

            for i in range(1, len(self.snake)):
                pygame.draw.rect(screen, (128, 128, 128), ((self.snake[i].coordX, self.snake[i].coordY),
                (self.squareSize, self.squareSize)))
                if(self.snake[0].coordX == self.snake[i].coordX and self.snake[0].coordY == self.snake[i].coordY):
                    run = False

            pygame.draw.rect(screen, (70, 70, 70), ((self.snake[0].coordX, self.snake[0].coordY),
            (self.squareSize, self.squareSize)))

            for i in range(0, self.HEIGHT, self.squareSize):
                pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, self.HEIGHT), 1)
                pygame.draw.line(screen, (0, 0, 0), (0, i), (self.WIDTH, i), 1)

            pygame.display.update()
            clock.tick(self.timer)

    def mooving(self):
        match self.direction:
            case self.Direction.Up:
                if self.snake[0].coordY - self.squareSize < 0:
                    self.snake[0].coordY = self.HEIGHT - self.squareSize
                else:
                    self.snake[0].coordY = self.snake[0].coordY - self.squareSize 

            case self.Direction.Down:
                if self.snake[0].coordY + self.squareSize >= self.WIDTH:
                    self.snake[0].coordY = 0
                else:
                    self.snake[0].coordY = self.snake[0].coordY + self.squareSize

            case self.Direction.Left:
                if self.snake[0].coordX - self.squareSize < 0:
                    self.snake[0].coordX = self.WIDTH - self.squareSize
                else:
                    self.snake[0].coordX = self.snake[0].coordX - self.squareSize

            case self.Direction.Right:
                if self.snake[0].coordX + self.squareSize >= self.HEIGHT:
                    self.snake[0].coordX = 0
                else:
                    self.snake[0].coordX = self.snake[0].coordX + self.squareSize

    def display(self):
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.HEIGHT, self.WIDTH), vsync=1)
        pygame.display.set_caption("Snake_test")
        self.game_process(screen, clock)

    def __init__(self):
        self.timer = 3
        self.direction = self.Direction.Right
        self.squareSize = 40
        self.appleID = [80, 80]
        self.HEIGHT = self.squareSize * 20
        self.WIDTH = self.squareSize * 20
        self.bg_color = (208, 240, 192)

game = Snake()
game.display()
sys.exit()