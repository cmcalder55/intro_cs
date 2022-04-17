
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

def sv_tree(trunk_length, levels):
    
    '''Takes an input of trunk length and tree levels.
    Outputs a drawing of a tree figure using recursion.'''
    
    if levels == 0:
        
        return
    
    turtle.speed(0)
    turtle.pencolor("green")
    turtle.pensize(5)

    turtle.forward(trunk_length)
    turtle.left(45)
    turtle.circle(5)
    sv_tree(trunk_length*.5, levels -1)
    turtle.right(90)
    sv_tree(trunk_length*.5, levels -1)
    turtle.left(45)

    turtle.penup()
    turtle.backward(trunk_length)
    turtle.pendown()

    return

    pass  # TODO

# Should take a few seconds to draw a tree.

sv_tree(100, 4)
