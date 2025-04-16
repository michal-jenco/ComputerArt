import sys

import pygame
import pygame.locals

import random
from math import sin, cos, sqrt, gcd, log


base_path = f"C:/Users/misko/Desktop/computer-art-2025/output"


def main():
    interesting_functions = {
        0: lambda x, y: ((sin(sin(x + i * sin(y - i ** (.0087 * i))))) + 1) * 2,
        1: lambda x, y: min(sqrt(x) * i / (y + 1), 3),
        2: lambda x, y: max(min(sin(sin(y)) * i / (y + 1), 3), 0),
        3: lambda x, y: random.randint(0, 3),
        4: lambda x, y: ((sin(x / (i + .001) + sin(y / (i + .001) / 2.)) + 1) / .5),
        5: lambda x, y: ((sin(sin(y / 20. * x / 20.)) + 1) * 2),
        6: lambda x, y: (sin(x / (i / 10. + 1)) + 1) + (cos(y / (i / 30. + 1)) + 1),
        7: lambda x, y: (sin(x / (i / 10. + 1)) + 1) + (cos(y / (i / 3. + 1)) + 1),
        8: lambda x, y: abs(sin(x * y * i) * 4),
        9: lambda x, y: abs(sin(x * y * i / 100.) * 4),
        10: lambda x, y: abs(sin(sqrt(x * y * i)) * 4),
        11: lambda x, y: abs((sin((x / (i / 150. + 1)) + sin(x / 2. + sin(y / 3.))))) * 4,
        12: lambda x, y: (x / 10. + y / 20. + i / 30.) % 4,
        13: lambda x, y: sin(x + y + i / 15.) + cos(x + y - i / 17.),
        14: lambda x, y: sqrt(abs(sin(cos(y + i / 10.))) * 8) * sqrt(abs(sin(cos(x - i / 30.))) * 6) % 4,
        15: lambda x, y: abs(i / 10. + sin(x) + sin(x / 3.) + sin(x / 5.) + cos(y / 2.) + cos(y / 7.)) % 4,
        16: lambda x, y: (gcd(x, y) + i) % 4,
        17: lambda x, y: log(x + y + i + 1, 2) % 4,
        18: lambda x, y: abs(sin(x * y + i)),
        19: lambda x, y: (sin(x + i / 4.) + sin(y + i / (sin(i / 6.) + .001)) + 2),
        20: lambda x, y: (sin(x * i / 15.) + sin(y * i / 5.)) % 4,
        21: lambda x, y: (sin(x * i / 105.) + sin(y * i / 50.)),
        22: lambda x, y: (sin(x * i / 505.) + sin(y * i / 450.) % 4),
    }

    pygame.init()
    windowsize = 500, 500
    w, h = windowsize

    surface = pygame.display.set_mode(windowsize, 0, 32)

    BLACK = 0, 0, 0

    x_step = 8
    y_step = 8

    surface.fill(BLACK)

    for i in range(1, 1000):
        pygame.draw.rect(surface, BLACK, (0, 0, *windowsize))
        for x in range(0, w, x_step):
            for y in range(0, h, y_step):
                event_handling()

                center = x, y
                f = interesting_functions[22](*center)

                radius = f * x_step / 8

                color = 255, 255, 255

                pygame.draw.circle(surface=surface, color=color, center=center, radius=radius)
        pygame.display.update()

        fname = f"{base_path}/pygame/{i}.png"
        print(f"saving frame {i}")
        # pygame.image.save(surface, fname)


def event_handling():
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()


main()
