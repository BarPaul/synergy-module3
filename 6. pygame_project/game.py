import pygame as pg
from constans import *
from sys import exit
from random import randint


class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = RIGHT
        self.head_right = pg.image.load("pictures/snake.png")
        self.head_right = pg.transform.scale(self.head_right, (BLOCKSIZE * self.head_right.get_width() // 100, BLOCKSIZE * self.head_right.get_height() // 100)).convert_alpha()
        self.head_down = pg.transform.rotate(self.head_right, -90)
        self.head_left = pg.transform.flip(self.head_right, True, False)
        self.head_up = pg.transform.rotate(self.head_right, 90)
        self.head_image = self.head_right
        self.body_image = pg.image.load("pictures/segment.png")
        self.body_image = pg.transform.scale(self.body_image, (BLOCKSIZE * self.body_image.get_width() // 100, BLOCKSIZE * self.body_image.get_height() // 100)).convert_alpha()

    def update(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (((cur[0] + (x * BLOCKSIZE)) % WIDTH), (cur[1] + (y * BLOCKSIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.length = 1
            self.positions = [((WIDTH // 2), (HEIGHT // 2))]
            pg.mixer.music.unload()
            while not pg.mixer.music.get_busy():
                pg.mixer.music.load("music/game_over.mp3")
                pg.mixer.music.play()
            pg.time.delay(1700)
            return
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

        
    def render(self):
        for i, p in enumerate(self.positions):
            if i == 0:
                game.screen.blit(pg.transform.scale(self.head_image, (BLOCKSIZE, BLOCKSIZE)), (p[0], p[1]))
            else:
                nxt = self.positions[i + 1] if i + 1 < len(self.positions) else None
                angle = self.angle(self.positions[i - 1], p, nxt)
                if angle == "flip":
                    rotated_body = pg.transform.rotate(self.body_image, -90)
                    rotated_body = pg.transform.flip(rotated_body, True, False)
                else:
                    rotated_body = pg.transform.rotate(self.body_image, angle)
                game.screen.blit(pg.transform.scale(rotated_body, (BLOCKSIZE, BLOCKSIZE)), (p[0], p[1]))

    def angle(self, prev, cur, nxt):
        if nxt:
            dx = nxt[0] - cur[0]
            dy = nxt[1] - cur[1]
        else:
            dx = cur[0] - prev[0]
            dy = cur[1] - prev[1]
        if (dx, dy) == (70, 0):
            return "flip"
        if dx == 0:
            return 0 if dy > 0 else 180
        elif dy == 0:
            return 90 if dx > 0 else 270
        else:
            if (dx > 0 and dy > 0) or (dx < 0 and dy < 0):
                return 45 if dx > 0 else 225
            return 135 if dx > 0 else 315
            
class Apple:
    def __init__(self):
        self.position = (randint(0, (WIDTH // BLOCKSIZE) - 1) * BLOCKSIZE,
                        randint(0, (HEIGHT // BLOCKSIZE) - 1) * BLOCKSIZE)
        self.image = pg.image.load("pictures/apple.png")
        self.image = pg.transform.scale(self.image, (BLOCKSIZE * self.image.get_width() // 100, BLOCKSIZE * self.image.get_height() // 100))

    def spawn(self, snake_positions: list):
            while self.position in snake_positions:
                self.position = (randint(0, (WIDTH // BLOCKSIZE) - 1) * BLOCKSIZE,
                                randint(0, (HEIGHT // BLOCKSIZE) - 1) * BLOCKSIZE)

    def render(self):
        game.screen.blit(pg.transform.scale(self.image, (BLOCKSIZE, BLOCKSIZE)), (self.position[0], self.position[1]))

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.mixer.music.set_volume(0.4)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.snake = Snake()
        self.apple = Apple()
        self.clock = pg.time.Clock()

    def handler(self):
        
        while not pg.mixer_music.get_busy():
            pg.mixer.music.load("music/game.mp3")
            pg.mixer.music.play(-1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type != pg.KEYDOWN:
                continue
            if event.key in (pg.K_UP, pg.K_w):
                if self.snake.direction == DOWN:
                    continue
                self.snake.direction = UP
                self.snake.head_image = self.snake.head_up
            elif event.key in (pg.K_DOWN, pg.K_s):
                if self.snake.direction == UP:
                    continue
                self.snake.direction = DOWN
                self.snake.head_image = self.snake.head_down
            elif event.key in (pg.K_LEFT, pg.K_a):
                if self.snake.direction == RIGHT:
                    continue
                self.snake.direction = LEFT
                self.snake.head_image = self.snake.head_left
            elif event.key in (pg.K_RIGHT, pg.K_d):
                if self.snake.direction == LEFT:
                    continue
                self.snake.direction = RIGHT
                self.snake.head_image = self.snake.head_right

    def game_run(self):
        while True:
            self.handler()
            self.snake.update()
            if self.snake.positions[0] == self.apple.position:
                self.snake.length += 1
                pg.mixer.Sound('music/apple.ogg').play()
                self.apple.spawn(self.snake.positions)
            self.screen.fill(BACKGROUND_COLOR)
            for obj in [self.snake, self.apple]:
                obj.render()
            pg.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.game_run()
