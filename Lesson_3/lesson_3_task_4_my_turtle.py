from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)
my_turtle.width(1)
my_turtle.pencolor("green")

# Нарисовать дугу
def draw_rect(t):
    r = 250
    u = 30
    t.circle(r,u)
    t.right(500)

colors = ["red","yellow","green","blue","violet"]

# Рисует дугу в цикле
for c in colors:
    my_turtle.pencolor(c)

    for x in range(0, 25):
        draw_rect(my_turtle)
        my_turtle.right(5)

# Необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()
