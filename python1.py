import turtle

def draw_shapes():
  window = turtle.Screen()
  window.bgcolor("red")
  brad = turtle.Turtle()
  brad.speed("fastest")

  for j in range(0,100):
    for i in range (0,4):
      brad.forward(100)
      brad.right(90)
    brad.right(2)
  
def draw_triangle(brad, length, depth):
  brad.setheading(300)
  for i in range(0,3):    
    brad.forward(length)
    brad.right(120)

  if depth > 0:
    draw_triangle(brad, length / 2, depth - 1)
    brad.setheading(300)
    brad.forward(length / 2)
    draw_triangle(brad, length / 2, depth - 1)
    brad.setheading(300)
    brad.forward(length / 2)
    brad.right(120)
    brad.forward(length)
    brad.right(120)
    brad.forward(length / 2)
    draw_triangle(brad, length / 2, depth - 1)
    brad.setheading(60)
    brad.forward(length / 2)

def draw():
  window = turtle.Screen()
  window.bgcolor("red")
  brad = turtle.Turtle()

  draw_triangle(brad, 200, 3)

  # draw_triangle(brad, 150)
  # brad.forward(150)
  # draw_triangle(brad, 150)
  # brad.forward(150)
  # brad.right(120)
  # brad.forward(300)
  # brad.right(120)
  # brad.forward(150)
  # draw_triangle(brad,150)
  # brad.setheading(60)
  # brad.forward(150)

  window.exitonclick()

draw()