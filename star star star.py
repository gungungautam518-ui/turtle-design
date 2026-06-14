import turtle


a=turtle.Turtle()

a.getscreen().bgcolor("#994444")

"""for i in range(5):
    a.forward(300)
    a.left(216)
    for j in range(5):
        a.forward(150)
        a.left(216)"""


def star(turtle,size):
    for i in range(5):
        turtle.forward(size)
        turtle.left(216)

for j in range(5):
    star(a,300)
    star(a,100)
    star(a,10)


turtle.done()
 
