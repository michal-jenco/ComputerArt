import turtle
from math import sqrt
import random
import datetime
from math import sin, cos, radians, degrees


# version 1.0
__default_dimensions__ = int(25), int(50)
__default_position__ = 0, 0
__cell_dimensions__ = 30, 30
#
# # version 2.0
# __default_dimensions__ = 20, 30
# __default_position__ = 0, 0
# __cell_dimensions__ = 30 * 25, 30 * 50


def get_date_string():
    return str(datetime.datetime.now()).split(".")[0].replace(":", "-").replace(" ", "-")


def range_to_range(r1, r2, value):
    """Scale value with range1 to range2"""

    OldMin, OldMax = r1
    NewMin, NewMax = r2

    OldRange = OldMax - OldMin

    if OldRange == 0:
        NewValue = NewMin

    else:
        NewRange = NewMax - NewMin
        NewValue = (((value - OldMin) * NewRange) / OldRange) + NewMin

    return NewValue


class Ranges(object):
    ZERO_FOUR = 0, 4


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
            if deformation_function:
                angle += deformation_function(i / 50.) / 3.
            self.t.forward(side)
            self.t.left(angle)
        turtle.update()


class DrawShapes(object):
    def __init__(self, draw=True):
        if not draw:
            return


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

    @staticmethod
    def right_angle(x, y, side):
        return {0: (x, y),
                1: (x + side, y),
                2: (x + side, y + side),
                3: (x, y + side)}

    def roof(self, x, y, side):
        return self.right_angle(x, y, side)

    @staticmethod
    def half_circle(x, y, radius):
        return {0: (x + radius, y),
                1: (x + 2 * radius, y + radius),
                2: (x + radius, y + 2 * radius),
                3: (x, y + radius)}

    @staticmethod
    def dot(x, y, cell_side):
        return x + cell_side / 2., y + cell_side / 2.

    def stick(self, x, y, cell_side, angle):
        center_x, center_y = self.dot(x, y, cell_side)
        return get_position_on_circle_based_on_angle(radius=cell_side / 2.,
                                                     angle=radians(angle), center_x=center_x, center_y=center_y)

    def ngon(self, x, y, cell_side, angle):
        return self.stick(x, y, cell_side, angle)


def get_position_on_circle_based_on_angle(radius, angle, center_x, center_y):
    x = cos(angle) * radius + center_x
    y = sin(angle) * radius + center_y
    return x, y


class Orientations:
    def __init__(self):
        pass

    def right_angle(self):
        return {0: 0, 1: 90, 2: 180, 3: 270}

    def roof(self):
        return self.right_angle()

    def half_circle(self):
        return self.right_angle()

    def stick(self, prob_dist_value):
        return range_to_range(Ranges.ZERO_FOUR, (0, 360), prob_dist_value)

    def ngon(self, prob_dist_value):
        return self.stick(prob_dist_value)


class DrawTriangle(DrawShapes):
    def __init__(self, draw, t, position, side, color, orientation, filled):
        super(DrawTriangle, self).__init__(draw=draw)

        self.side = side
        self.position = position
        self.x, self.y = position
        self.t = t
        self.filled = filled

        self.orientations = Orientations().roof()
        self.starting_positions = StartingPositions().roof(self.x, self.y, self.side)
        self.orientation = self.orientations[int(orientation)]

        self.t.penup()
        self.t.pencolor(color)

        self.angles = TriangleAngles.ROOF
        self.lengths = TriangleSides().roof(self.side)

        self.t.setheading(self.orientation)
        self.t.setpos(self.starting_positions[int(orientation)])

        self.t.pendown()

        if self.filled:
            self.t.fillcolor("white")
            self.t.begin_fill()

        for i in range(3):
            t.forward(self.lengths[i])
            t.left(180 - self.angles[i])

        if self.filled:
            self.t.end_fill()
            # self.t.fill()


class DrawHalfCircles(DrawShapes):
    def __init__(self, draw, t, position, radius, color, fill_color, probability_distribution_value, filled):
        super(DrawHalfCircles, self).__init__(draw=draw)

        if not draw:
            return

        x, y = position
        orientations = Orientations().half_circle()
        starting_positions = StartingPositions().half_circle(x, y, radius)
        orientation = orientations[int(probability_distribution_value)]

        t.penup()
        t.setheading(orientation)
        t.setpos(starting_positions[int(probability_distribution_value)])
        t.pencolor(color)
        t.pendown()

        if filled:
            t.fillcolor(fill_color)
            t.begin_fill()

        cut = {0: 0,
               1: 180,
               2: 180,
               3: 360}[int(probability_distribution_value)]

        t.circle(radius, cut)

        if filled:
            t.end_fill()


class DrawSykora(DrawShapes):
    def __init__(self):
        pass


class DrawScaledDots(DrawShapes):
    def __init__(self, draw, t, position, cell_size, probability_distribution_value, color):
        super(DrawScaledDots, self).__init__(draw=draw)

        if not draw:
            return

        x, y = position
        t.penup()
        t.setpos(StartingPositions().dot(x, y, cell_size))
        t.pendown()

        radius = range_to_range(Ranges.ZERO_FOUR, (0, cell_size), probability_distribution_value)
        t.dot(radius, color)


class DrawStick(DrawShapes):
    def __init__(self, draw, t, position, cell_size, probability_distribution_value, color, width):
        super(DrawStick, self).__init__(draw=draw)

        if not draw:
            return

        angle = Orientations().stick(prob_dist_value=probability_distribution_value)
        x, y = position

        t.penup()
        t.setpos(StartingPositions().stick(x, y, cell_size, angle=angle))
        t.setheading(angle-180)
        t.pencolor(color)
        t.width(width)
        t.pendown()
        t.forward(range_to_range(Ranges.ZERO_FOUR, (cell_size, cell_size*3), probability_distribution_value))


class DrawNgon(DrawShapes):
    def __init__(self, draw, t, position, side, probability_distribution_value, color, n=4, width=1):
        super(DrawNgon, self).__init__(draw=draw)

        if not draw:
            return

        x, y = position
        angle = Orientations().ngon(prob_dist_value=probability_distribution_value)

        t.penup()
        t.setpos(StartingPositions().ngon(x, y, side, angle=angle))
        t.setheading(angle-180)
        t.pendown()

        for i in range(n):
            t.forward(side)
            t.left(360 / n)
        t.penup()


class DrawCellBoundary(DrawShapes):
    def __init__(self, draw, t, side, position, color):
        super(DrawCellBoundary, self).__init__(draw=draw)

        if not draw:
            return

        self.x, self.y = position

        t.penup()
        t.setheading(0)
        t.setpos(position)
        t.pendown()
        t.pencolor(color)

        for i in range(4):
            t.forward(side)
            t.left(90)


class DrawCellGrid(DrawShapes):
    def __init__(self, draw, t, dimensions, start_pos, cell_side, color, width):
        cols, rows = dimensions

        t.setheading(0)
        t.setpos(start_pos)
        t.width(width)
        t.pencolor(color)

        for i in range(rows):
            pass


class DrawCellBackground(DrawShapes):
    def __init__(self, draw, t, position, probability_distribution_value, cell_side):
        if not draw:
            return

        color = "black" if probability_distribution_value < 2 else "white"

        t.fillcolor(color)
        t.pencolor(color)
        t.setheading(0)
        t.setpos(position)
        t.pendown()
        t.begin_fill()

        for i in range(4):
            t.forward(cell_side)
            t.left(90)

        t.end_fill()
        t.penup()


class DrawExperiment(DrawShapes):
    def __init__(self, draw, t, position, probability_distribution_value):
        if not draw:
            return

        t.penup()
        t.setpos(position)
        t.pendown()

        t.circle(probability_distribution_value)


class ProbabilityDistribution:
    def __init__(self, value_func, dimensions=__default_dimensions__):
        self.xy = dimensions
        self.x, self.y = dimensions
        self.values = {}

        for x in range(int(self.x)):
            for y in range(int(self.y)):
                value = value_func(x, y)
                self.values[(x, y)] = float(value)

    def get_value(self, xy):
        return self.values[xy]


class WhatToDrawSettings(object):
    def __init__(self, cell_background=0, triangles=0, cell_boundary=0, half_circles=0, scaled_dots=0, sticks=0,
                 ngon=0, experiment=0):
        self.cell_background = bool(cell_background)
        self.triangles = bool(triangles)
        self.cell_boundary = bool(cell_boundary)
        self.half_circles = bool(half_circles)
        self.scaled_dots = bool(scaled_dots)
        self.sticks = bool(sticks)
        self.ngon = bool(ngon)
        self.experiment = bool(experiment)


class Art_2__0___1_____8___i__m_a_g__e:
    def __init__(self, grid=None, name="<anonymous> Art_2__0___1_____8___i__m_a_g__e <\\anonymous", turtle=None):
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

    def __str__(self):
        return "Image: %s" % self.name

    def display(self, what_to_draw, offset=(0, 0)):
        print("Displaying Image: %s ..." % self.name)

        self.t.ht()
        self.grid.draw(offset=offset, what_to_draw=what_to_draw)


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

    def draw(self, what_to_draw, offset=(0, 0)):
        self.t.ht()

        for i, cell in enumerate(self.cells):
            cell.draw(probability_distribution_value=self.prob_dist.get_value((i % self.cols, i // self.rows)),
                      offset=offset, what_to_draw=what_to_draw)
        turtle.update()


class ArtCell:
    def __init__(self, t, dimensions, position=__default_position__, image=None, orientation=None):
        self.t = t
        self.dimensions = dimensions
        self.side = dimensions[0]
        self.position = position
        self.image = image
        self.orientation = orientation

    def __repr__(self):
        msg = "-- ArtCell _X%s__Y%s_ --" % (self.position[0], self.position[1])
        return msg

    def __str__(self):
        return self.__repr__()

    def draw(self, probability_distribution_value, what_to_draw, offset=(0, 0)):
        drawing_position = self.position[0] + offset[0], self.position[1] + offset[1]
        self.t.penup()
        self.t.setpos(self.position)

        if what_to_draw.cell_background:
            DrawCellBackground(draw=True, t=self.t, cell_side=self.dimensions[0], position=drawing_position,
                               probability_distribution_value=probability_distribution_value)

        if what_to_draw.triangles:
            DrawTriangle(t=self.t, draw=True,
                         position=drawing_position, side=30, color="white", orientation=probability_distribution_value,
                         filled=False if probability_distribution_value <= 2 else True, )

        if what_to_draw.cell_boundary:
            DrawCellBoundary(draw=True, t=self.t, side=self.side, position=drawing_position, color="white")

        if what_to_draw.half_circles:
            DrawHalfCircles(draw=True, t=self.t, position=drawing_position, radius=self.side / 2, color="white",
                            fill_color="white", filled=probability_distribution_value < 9,
                            probability_distribution_value=probability_distribution_value)

        if what_to_draw.scaled_dots:
            DrawScaledDots(draw=True, t=self.t, position=drawing_position, cell_size=self.dimensions[0], color="white",
                           probability_distribution_value=probability_distribution_value)

        if what_to_draw.sticks:
            DrawStick(draw=True, t=self.t, position=drawing_position, cell_size=self.dimensions[0], color="white",
                      probability_distribution_value=probability_distribution_value, width=1)

        if what_to_draw.ngon:
            DrawNgon(draw=True, t=self.t, position=drawing_position, side=self.side,
                     probability_distribution_value=probability_distribution_value, color="w", width=1)

        if what_to_draw.experiment:
            DrawExperiment(draw=True, t=self.t, position=drawing_position,
                           probability_distribution_value=probability_distribution_value)
