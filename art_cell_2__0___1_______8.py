### 2025 update

import turtle
import random
from math import sin, cos, sqrt, gcd, log
from PIL import ImageGrab

from classes import (
    ArtCell, ProbabilityDistribution, Art_2__0___1_____8___i__m_a_g__e, GridOfArtCells, __cell_dimensions__,
    WhatToDrawSettings,
)


def save_layout(filename: str) -> None:
    base_path = f"C:/Users/misko/Desktop/computer-art-2025"

    im = ImageGrab.grab(bbox=(1050, 500, 1550, 1000))
    im.save(f"{base_path}/output/{filename}.png", format="PNG")


def main():
    turtle.setup(width=600, height=600)
    turtle.bgcolor("black")
    turtle.pencolor("white")
    turtle.ht()

    t = turtle.Turtle()

    x_offset, y_offset = -250, -250
    x_spacing, y_spacing = __cell_dimensions__

    rows, cols = 50, 50
    positions_xy = list(range(int(cols))), list(range(int(rows)))
    art_cells = []

    for y in positions_xy[1]:
        for x in positions_xy[0]:
            position = x*x_spacing + x_offset, y*y_spacing + y_offset
            cell = ArtCell(t=t, dimensions=__cell_dimensions__, position=position, orientation=random.randint(0, 3))
            art_cells.append(cell)
    del x, y

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
        21: lambda x, y: (sin(x * i / 105.) + sin(y * i / 50.)) % 4,
        22: lambda x, y: (sin(x * i / 305.) + sin(y * i / 250.)) % 4,
    }

    for i in range(2000, 5000):
        print("Animation: %s" % i)
        prob_dist = ProbabilityDistribution(value_func=interesting_functions[22])
        art_grid = GridOfArtCells(t, art_cells, prob_dist=prob_dist)
        what_to_draw = WhatToDrawSettings(cell_background=0,
                                          triangles=0,
                                          cell_boundary=0,
                                          half_circles=0,
                                          scaled_dots=1,
                                          sticks=0,
                                          ngon=0,
                                          experiment=0)

        image = Art_2__0___1_____8___i__m_a_g__e(turtle=t, grid=art_grid)

        image.t.clear()
        image.display(offset=(0, 0), what_to_draw=what_to_draw)

        save_layout(filename=str(i))

        # im = grab(bbox=[30, 150, 1620, 1040])
        # im.save("../images3/%s.png" % (get_date_string() + "_" + str(i)))

    turtle.exitonclick()


if __name__ == '__main__':
    main()
