import pygame

class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    pass

def redrawWindow(surface):
    win.fill((0, 0, 0))
    drawGrid(surface)
    pygame.display.update()
    pass

def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))
    s = snake((255, 0, 0), (10, 10))
    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)

    pass