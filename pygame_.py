import math
import sys

import pygame
import pygame.locals


def main():
    pygame.init()
    windowsize = 1800, 800
    display = pygame.display.set_mode(windowsize, 0, 32)

    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    BLACK = 0, 0, 0
    RED = 255 * .8, 0, 80 * .8

    display.fill(BLACK)

    i = 0
    while True:
        # pygame.draw.rect(display, BLACK, (0, 0, *windowsize))
        event_handling()

        x = math.sin(200 + i / 10.) + 200
        y = 300
        width = math.sin((i ** math.sqrt(i / 500.)) / 200.) * 100
        height = math.cos(i / 120.) * 40

        pygame.draw.rect(display, [i % 255] + list(RED)[1:], (x, y, width, height))

        if not i % 1:
            pygame.display.update()

        i += 1


def event_handling():
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()


main()
