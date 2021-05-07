# Código modificado por:
# Autor: Sergio Adolfo Sanoja Hernández
# Autor: Fabián Castillo Rodríguez


from random import randrange
from turtle import *
from freegames import vector


ball = vector(-200, -200)    # Define the position of the ball.
speed = vector(0, 0)         # Define the initial velocity.
targets = []                 # Define the list of targets.


def tap(x, y):
    """
    Respond to screen tap.
    """
    # Prevent the user from tapping multiple times when the ball is within the boundries,
    # and define the launch speed.
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15


def inside(xy):
    """
    Return True if xy within screen.
    """
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """
    Draw ball and targets.
    """
    clear()
    
    # Generate the shape, size and color of the targets.
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
        
    # Generate the shape, size and color of the ball.
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """
    Move ball and targets.
    """
    # Create and locate a new target according to a randomizer.
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Define the speed of the target
    for target in targets:
        target.x -= 3

    # Define the parable of the ball.
    if inside(ball):
        speed.y -= .35
        ball.move(speed)

    dupe = targets.copy()    # Duplicate all targets.
    targets.clear()          # Clear all targets.

    # Create a new target if the result of the substraction is greater than 13.
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()    # Draw everything.

    ontimer(move, 50)    # Define the rate of the game.


setup(420, 420, 370, 0)    # Create the workspace.
hideturtle()
up()
tracer(False)              # Deactivate the turtle's animation.
onscreenclick(tap)         # Call "tap" function when there's a click on screen.
move()                     # Call the function. 
done()