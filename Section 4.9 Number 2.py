# ----------------------------------------
# Program:   4.9 Exercise 2
# Author:    ynvj
# Name:      Jovanny Cano
# Date:      06/12/2026
# ----------------------------------------

import turtle

def draw_square(t, sz):
    """Make turtle t draw a square of sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)
def move_square(t):
    """Reposition pen to fit square within square"""
    for o in range(1): 
        t.penup()
        t.backward(10)
        t.right(90)
        t.forward(10)
        t.left(90)
        t.pendown()

wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("brown")
wn.title("Squares In Squares")
alex = turtle.Turtle()      # Create alex

size = 20
for i in range(5):
    draw_square(alex, size) # Call the function to draw the square
    size = size + 20
    move_square(alex)       # Call the function to move pen
    
wn.mainloop()
