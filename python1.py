import turtle

def draw_triangle(brad, length, depth):
  brad.setheading(300)
  for i in range(0,3):    
    brad.forward(length)
    brad.right(120)

  if depth == 0:
    return
  
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

  window.exitonclick()

draw()