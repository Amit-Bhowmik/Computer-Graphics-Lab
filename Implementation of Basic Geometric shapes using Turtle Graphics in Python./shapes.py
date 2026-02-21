import time

def draw_square(t):
    t.fillcolor('red')
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
        time.sleep(0.01)
    t.end_fill()


def draw_rectangle(t):
    t.fillcolor('blue')
    t.begin_fill()
    for i in range(2):
        t.forward(150)
        t.left(90)
        t.forward(80)
        t.left(90)
        time.sleep(0.01)
    t.end_fill()


def draw_triangle(t):
    t.fillcolor('green')
    t.begin_fill()
    for i in range(3):
        t.forward(120)
        t.left(120)
        time.sleep(0.01)
    t.end_fill()


def draw_circle(t):
    t.fillcolor('orange')
    t.begin_fill()
    t.circle(70)
    t.end_fill()


def draw_pentagon(t):
    t.fillcolor('cyan')
    t.begin_fill()
    for i in range(5):
        t.forward(100)
        t.left(72)
        time.sleep(0.01)
    t.end_fill()


def draw_hexagon(t):
    t.fillcolor('purple')
    t.begin_fill()
    for i in range(6):
        t.forward(100)
        t.left(60)
        time.sleep(0.01)
    t.end_fill()


def draw_star(t):
    t.fillcolor('yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(150)
        t.right(144)
        time.sleep(0.01)
    t.end_fill()
