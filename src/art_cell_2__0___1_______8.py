import turtle
import random
from math import sin, cos, sqrt
from pyscreenshot import grab

from classes import (ArtCell, Fullness, ProbabilityDistribution, Art_2__0___1_____8___i__m_a_g__e,
                     GridOfArtCells, __default_dimensions__, __cell_dimensions__, get_date_string)


def main():
    turtle.setup(width=1900, height=950)
    turtle.bgcolor("black")
    turtle.pencolor("white")
    turtle.ht()

    t = turtle.Turtle()

    x_offset, y_offset = -900, -400
    x_spacing, y_spacing = __cell_dimensions__

    rows, cols = __default_dimensions__
    positions_xy = list(range(0, cols)), list(range(0, rows))
    art_cells = []

    for y in positions_xy[1]:
        for x in positions_xy[0]:
            position = x*x_spacing + x_offset, y*y_spacing + y_offset
            cell = ArtCell(t=t, dimensions=__cell_dimensions__, position=position, orientation=random.randint(0, 3))
            art_cells.append(cell)

    # circle y_offset
    # (cos(i / 15.) / 2. + 1) * 150, (sin(i / 15.) / 2. + 1) * 150)

    interesting_functions = {0: lambda x, y: ((sin(sin(x+i*sin(y-i**i))))+1)*2,
                             1: lambda x, y: min(sqrt(x)*i/(y+1), 3),
                             2: lambda x, y: max(min(sin(sin(y))*i/(y+1), 3), 0),
                             3: lambda x, y: int(random.randint(0, 3)),
                             4: lambda x, y: ((sin(x/(i+.001) + sin(y/(i+.001)/2.))+1)/.5),
                             5: lambda x, y: ((sin(sin(y / 20. * x / 20.)) + 1) * 2),
                             6: lambda x, y: (sin(x / (i / 10. + 1)) + 1) + (cos(y / (i / 30. + 1)) + 1),
                             7: lambda x, y: (sin(x / (i / 10. + 1)) + 1) + (cos(y / (i / 3. + 1)) + 1),
                             8: lambda x, y: abs(sin(x*y*i) * 4),
                             9: lambda x, y: abs(sin(x*y*i) * 4),
                             10: lambda x, y: abs(sin(sqrt(x*y*i)) * 4),
                             11: lambda x, y: abs((sin((x / (i/50. + 1)) + sin(x / 2. + sin(y / 3.))))) * 4}

    del x, y
    for i in range(1000):
        print("Animation: %s" % i)
        prob_dist = ProbabilityDistribution(value_func=interesting_functions[11])
        art_grid = GridOfArtCells(t, art_cells, prob_dist=prob_dist)

        image = Art_2__0___1_____8___i__m_a_g__e(turtle=t, grid=art_grid)

        image.t.clear()
        image.display(offset=(0, 0))

        # im = grab(bbox=[30, 150, 1620, 1040])
        # im.save("../images/%s.png" % (get_date_string() + "_" + str(i)))

    turtle.exitonclick()


if __name__ == '__main__':
    main()
