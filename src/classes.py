import turtle
import os
import glob
import random
import time
from math import sin, sqrt, cos


__default_dimensions__ = 22, 50
__default_position__ = 0, 0

class SquareDrawer:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.setheading(to_angle=0)
        self.t.tracer(0, 0)
        self.t.width(1)

    def get_canvas(self):
        cv = turtle.getcanvas()
        return cv

    def save_canvas(self, canvas, filename="abc.ps"):
        canvas.postscript(file=filename, colormode='color')

    def draw(self, pos=(0, 0), n=4, side=5, rotation=0):
        self.t.penup()
        self.t.setpos(pos)
        self.t.setheading(rotation)
        self.t.pendown()

        self._draw_ngon(n=n, side=side)

    def _draw_ngon(self, n=4, side=20):
        for _ in range(n):
            self.t.forward(side)
            self.t.left(360./n)


class SequenceGenerator:
    def __init__(self):
        pass

    def get_grid(self, offset=(0, 0), rows=20, cols=20, step_v=5, step_h=5):
        for row in range(rows):
            for col in range(cols):
                yield offset[0] + col*step_v, offset[1] - row*step_h


class CircleDrawer:
    def __init__(self, t):
        self.t = t
        self.t.pencolor("white")

    def draw(self, pos=(0, 0), angle=1, side=1, deformation_function=None):
        self.t.penup()
        self.t.setpos(pos)
        self.t.pendown()
        self.t.setheading(to_angle=0)

        for i in range(int(360 / angle)):
            if deformation_function is not None:
                angle += deformation_function(i/50.)/3.
            self.t.forward(side)
            self.t.left(angle)
        turtle.update()


class Art_2__0___1_____8___i__m_a_g__e:
    def __init__(self, grid=None, name="<anonymous> Art_2__0___1_____8___i__m_a_g__e <\\anonymous",
                 turtle=None):
        self.t = turtle
        self.name = name
        self.grid = grid
        self.t.pencolor("white")
        self.default_heading = 0

        self._setup_turtle()

    def _setup_turtle(self):
        turtle.tracer(0, 0)
        self.t.ht()
        self.t.setheading(self.default_heading)
        self.t.width(1)

    def __str__(self):
        return "Image: %s" % self.name

    def display(self, offset=(0, 0)):
        print("Displaying Image: %s ..." % self.name)

        self.t.ht()
        self.grid.draw(offset)


class DrawShapes:
    pass


class TriangleAngles:
    RIGHT_ANGLE = [90, 45, 45]
    ROOF = [45, 90, 45]


class TriangleSides:
    def __init__(self):
        pass

    def right_angle(self, side):
        return [side, side, sqrt(side**2 + side**2)]

    def roof(self, side):
        return [side, sqrt(2 * side ** 2) / 2., sqrt(2 * side ** 2) / 2.]


class StartingPositions:
    def __init__(self):
        pass

    def right_angle(self, x, y, side):
        return {0: (x, y),
                1: (x + side, y),
                2: (x + side, y + side),
                3: (x, y + side)}

    def roof(self, x, y, side):
        return self.right_angle(x, y, side)


class Orientations:
    def __init__(self):
        pass

    def right_angle(self):
        return {0: 0, 1: 90, 2: 180, 3: 270}

    def roof(self):
        return self.right_angle()


class DrawTriangle(DrawShapes):
    def __init__(self, t, position, side, color, orientation, filled):

        self.side = side
        self.position = position
        self.x, self.y = position
        self.t = t
        self.filled = filled

        self.orientations = Orientations().roof()
        self.starting_positions = StartingPositions().roof(self.x, self.y, self.side)
        self.orientation = self.orientations[orientation]

        self.t.penup()
        self.t.pencolor(color)

        self.angles = TriangleAngles.ROOF
        self.lengths = TriangleSides().roof(self.side)

        self.t.setheading(self.orientation)
        self.t.setpos(self.starting_positions[orientation])

        self.t.pendown()

        if self.filled:
            self.t.fillcolor("white")
            self.t.begin_fill()

        for i in range(0, 3):
            t.forward(self.lengths[i])
            t.left(180 - self.angles[i])

        if self.filled:
            self.t.end_fill()
        self.t.fill()

        # self.t.write(str(orientation))


class ArtCell:
    def __init__(self, t, position=__default_position__, image=None, orientation=None):
        self.t = t
        self.position = position
        self.fullness = Fullness()
        self.image = image
        self.orientation = orientation

        self.t.pendown()

    def __repr__(self):
        msg = "-- ArtCell _X%s__Y%s_ --" % (self.position[0], self.position[1])
        return msg

    def draw(self, orientation, offset=(0, 0)):
        drawing_position = self.position[0] + offset[0], self.position[1] + offset[1]
        self.t.penup()
        # print("ArtCell is being drawn: %s" % self)
        self.t.setpos(self.position)
        self.t.pendown()

        DrawTriangle(self.t,
                     position=drawing_position, side=30, color="white", orientation=orientation,
                     filled=False if orientation <= 2 else True)


class GridOfArtCells:
    def __init__(self, t=None, cells=None, cols=__default_dimensions__[0], rows=__default_dimensions__[1],
                 prob_dist=None):
        self.t = t
        self.cells = cells
        self.rows, self.cols = rows, cols
        self.prob_dist = prob_dist

    def __getitem__(self, xy):
        return self.get_item_by_xy(xy)

    def get_item_by_xy(self, xy):
        x, y = xy
        return self.cells[x*self.cols + y]

    def draw(self, offset=(0, 0)):
        self.t.ht()

        for i, cell in enumerate(self.cells):
            cell.draw(orientation=self.prob_dist.get_value((i % self.cols, i / self.rows)),
                      offset=offset)

            # if i % 500000 == 0:
        turtle.update()
        # time.sleep(.05)


class ProbabilityDistribution:
    def __init__(self, dimensions=__default_dimensions__, value_func=lambda x, y: 0):
        self.xy = dimensions
        self.x, self.y = dimensions
        self.values = {}

        for x in range(self.x):
            for y in range(self.y):
                value = value_func(x, y)
                self.values[x, y] = int(value)

    def get_value(self, xy):
        x, y = xy
        return self.values[x, y]


class Fullness:
    def __init__(self):
        self.fullness = None

    def __float__(self):
        float(self.fullness)
