from pygame import *
import sys
from random import randint

init()

sc = display.set_mode((500, 550))
display.set_caption("Муравьиная колония")

class Ant:
    def __init__(self, x, y, width, height):
        self.rect = Rect(x, y, width, height)

    def move(self, dx, dy, maze_surface):
        # Проверяем, есть ли черный цвет в будущем положении муравья
        future_rect = self.rect.move(dx, dy)
        for x in range(future_rect.left, future_rect.right):
            for y in range(future_rect.top, future_rect.bottom):
                if maze_surface.get_at((x, y)) == (0, 0, 0):
                    return  # Не перемещаем муравья, если будущее положение содержит черный цвет

        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        draw.rect(surface, (randint(0, 255), randint(0, 255), randint(0, 255)), self.rect)

class Maze:
    def __init__(self, maze_layout):
        self.maze_layout = maze_layout
        self.block_size = 50
        self.maze_rects = []
        self.surface = Surface((500, 550), SRCALPHA)  # Используем SRCALPHA для сохранения альфа-канала

        for row_index, row in enumerate(self.maze_layout):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    rect = Rect(col_index * self.block_size, row_index * self.block_size, self.block_size, self.block_size)
                    self.maze_rects.append(rect)
                    draw.rect(self.surface, (0, 0, 0), rect)

    def draw(self, surface):
        surface.blit(self.surface, (0, 0))

maze_layout = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

maze = Maze(maze_layout)
a = 0
ants = []

for i in range(10):
    ant = Ant(25, 125, 5, 5)  # Изменили размер муравья на 5x5 пикселей
    ants.append(ant)

x, y = 100, 100

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()

    keys = key.get_pressed()

    sc.fill((255, 255, 255))
    maze.draw(sc)

    for ant in ants:
        ant.draw(sc)

        for rect in maze.maze_rects:
            if ant.rect.colliderect(rect):
                # Обработка столкновения с препятствием
                ant.rect.clamp_ip(rect)

        if keys[K_LEFT]:
            ant.move(-5, 0, maze.surface)
        if keys[K_RIGHT]:
            ant.move(5, 0, maze.surface)
        if keys[K_UP]:
            ant.move(0, -5, maze.surface)
        if keys[K_DOWN]:
            ant.move(0, 5, maze.surface)

        # Ограничиваем движение муравьев внутри экрана
        ant.rect.clamp_ip(sc.get_rect())

    display.update()
