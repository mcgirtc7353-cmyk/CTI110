# Cedric McGirt
# 3/18/2026
#P4LAB - Use loops to draw a house 

import turtle

#creat a window to draw in 
window = turtle.Screen()
window.bgcolor("Green")

# creat your turtle drawing object 
GEO = turtle.Turtle()
GEO.shape("turtle")
GEO.pensize(3)
GEO.pencolor("black")


# draw the square 
for i in range (4):
    GEO.forward(200)
    GEO.right(90)

# draw the triangele 
for i in range (3):
    GEO.forward(200)
    GEO.left(120)



window.mainloop()