####################################################### IMPORT #######################################################

from turtle import *
from random import *
from math import *

##################################################### FUNCTIONS ######################################################

# Function to draw filled circle at a specific position
def draw_ball(x_pos,y_pos,ball_radius,ball_color):
    draw.penup()
    draw.goto(x_pos,y_pos-ball_radius) # move to the bottom of the circle
    draw.pendown()
    draw.fillcolor(ball_color)
    draw.begin_fill()
    draw.circle(ball_radius)
    draw.end_fill()

# Function to calculate the centre distance of two balls
def distance (x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    centre_distance = sqrt(dx**2 + dy**2)
    return centre_distance

# Function to check ball overlapping while spawning
def is_overlapping(x_new, y_new, ball_radius, x_old, y_old):
    centre_distance = distance(x_new,y_new,x_old,y_old)
    return centre_distance < 2 * ball_radius

# Function to handle balls colliding with the animation window boundary
def boundary_collision (ball_position,ball_radius,ball_velocity):
    x_pos, y_pos = ball_position
    vel_x, vel_y = ball_velocity
    # Side walls
    if x_pos > sw//2 - ball_radius:
        x_pos = sw//2 - ball_radius
        vel_x = -vel_x
    elif  x_pos <= -sw//2 + ball_radius:
        x_pos = -sw//2 + ball_radius
        vel_x = -vel_x
    # Top and bottom walls
    if y_pos >= sh//2 - ball_radius:
        y_pos = sh//2 - ball_radius
        vel_y = -vel_y
    elif y_pos < -sh//2 + ball_radius:
        y_pos = -sh//2 + ball_radius
        vel_y = -vel_y
    # return changed velocity and positions
    return (x_pos, y_pos), (vel_x, vel_y)

# Function to check the direction of the ball
def direction(vel_x, vel_y):
    ball_direction = []
    # Check direction of ball 1
    if vel_x > 0 < vel_y: # vx , vy = 1 , 1
        ball_direction = 'NE'
    elif vel_x < 0 > vel_y: # vx , vy = -1 , -1
        ball_direction = 'SW'
    elif vel_x > 0 > vel_y: # vx , vy = 1 , -1
        ball_direction = 'SE'
    elif vel_x < 0 < vel_y: # vx , vy = -1 , 1
        ball_direction = 'NW'
    # return direction
    return ball_direction

# Function to handle balls colliding with each other
def ball_collision (p1,p2,ball_radius,v1,v2):
    # call function to calculate the distance between the two balls to determine if they are colliding
    x1, y1 = p1
    x2, y2 = p2
    vx1, vy1 = v1
    vx2, vy2 = v2
    collide = is_overlapping(x1,y1,ball_radius,x2,y2)
    if collide:
        d = distance(x1,y1,x2,y2) # distance between two balls
        overlap = radius - d/2 # length of the overlap between two balls
        dir1 = direction(vx1, vy1) # get direction of ball 1
        dir2 = direction(vx2, vy2) # get direction of ball 2
        # Head on collision >> reverse direction
        if vx1 == -vx2 and vy1 == -vy2:
            if dir1 == 'NE' and dir2 == 'SW':
                p1 = x1 - overlap / 2, y1 - overlap / 2 # NE
                p2 = x2 + overlap / 2, y2 + overlap / 2 # SW
            elif dir1 == 'SW' and dir2 == 'NE':
                p1 = x1 + overlap / 2, y1 + overlap / 2
                p2 = x2 - overlap / 2, y2 - overlap / 2
            elif dir1 == 'SE' and dir2 == 'NW':
                p1 = x1 - overlap / 2, y1 + overlap / 2
                p2 = x2 + overlap / 2, y2 - overlap / 2
            elif dir1 == 'NW' and dir2 == 'SE':
                p1 = x1 + overlap / 2, y1 - overlap / 2
                p2 = x2 - overlap / 2, y2 + overlap / 2
            v1 = (-vx1, -vy1)
            v2 = (-vx2, -vy2)
        # Orthogonal collision >> mirror reflection
        elif vx1 == -vx2 and vy1 == vy2:
            if dir1 == 'NE' and dir2 == 'SE':
                p1 = x1 - overlap / 2, y1 - overlap / 2  # NE
                p2 = x2 - overlap / 2, y2 + overlap / 2  # SW
            elif dir1 == 'SE' and dir2 == 'NE':
                p1 = x1 - overlap / 2, y1 + overlap / 2
                p2 = x2 - overlap / 2, y2 - overlap / 2
            elif dir1 == 'NW' and dir2 == 'SW':
                p1 = x1 + overlap / 2, y1 - overlap / 2
                p2 = x2 + overlap / 2, y2 + overlap / 2
            elif dir1 == 'SW' and dir2 == 'NW':
                p1 = x1 + overlap / 2, y1 + overlap / 2
                p2 = x2 + overlap / 2, y2 - overlap / 2
            v1 = (-vx1, vy1)
            v2 = (-vx2, vy2)
        elif vx1 == vx2 and vy1 == -vy2:
            if dir1 == 'NE' and dir2 == 'NW':
                p1 = x1 - overlap / 2, y1 - overlap / 2  # NE
                p2 = x2 + overlap / 2, y2 - overlap / 2  # SW
            elif dir1 == 'NW' and dir2 == 'NE':
                p1 = x1 + overlap / 2, y1 - overlap / 2
                p2 = x2 - overlap / 2, y2 - overlap / 2
            elif dir1 == 'SE' and dir2 == 'SW':
                p1 = x1 - overlap / 2, y1 + overlap / 2
                p2 = x2 + overlap / 2, y2 + overlap / 2
            elif dir1 == 'SW' and dir2 == 'SE':
                p1 = x1 + overlap / 2, y1 + overlap / 2
                p2 = x2 - overlap / 2, y2 + overlap / 2
            v1 = (vx1, -vy1)
            v2 = (vx2, -vy2)
    # return changed velocity
    return p1, p2, v1, v2

#################################################### INITIALIZATION ##################################################

# Create a window for animation and setup drawing
sw = 1400 # Window width
sh = 800 # Window height
window = Screen()
window.setup(sw,sh)
window.tracer (0) # turn off animation
window.colormode(255)  # RGB color
draw = Turtle()  # redefine the turtle function as draw for ease of use
draw.hideturtle()  # hide the turtle/drawing

# input variables
num_ball = 10
radius = 30
speed = 2

p = [] # Ball position matrix
v = [] # Ball velocity matrix
colors = [] # Ball color matrix

# Initial p and direction of ball movement
while len (p) < num_ball: # loop will end while desired number of balls are created
    # generate random position to draw ball
    x = randint((radius-(sw//2)), ((sw//2)-radius))
    y = randint((radius-(sh//2)), ((sh//2)-radius))

    # Check the position of the new ball with old ones, return true if balls overlap, otherwise false
    overlapping = any(is_overlapping(x,y,radius,px,py) for px, py in p)

    # check for overlap >>> if overlap = false, not overlap = true
    if not overlapping:
        color = (randint(0, 255), randint(0, 255), randint(0, 255)) # generate random color
        vel = [(speed * choice([1, -1])), (speed * choice([1, -1]))] # generate velocity >> SE,SW,NE,NW

        p.append((x,y)) # store the x,y values to the p matrix
        colors.append(color) # store color
        v.append(vel) # store velocity

        draw_ball(x, y, radius, color) # execute draw_ball function create a new ball

window.update() # Update the screen to show all circles

################################################## BALL MOTION LOOP ##################################################

while True:
    for i in range (num_ball):
        x, y = p[i] # extract x and y component of the ball position from matrix
        vx, vy = v[i] # extract x and y component of the ball velocity from matrix
        # Move ball position
        x += vx
        y += vy
        p[i] = (x, y) # Store updated position

        # check boundary collision >> return reversed velocity if collides
        p[i], v[i] = boundary_collision(p[i], radius, v[i])

        # loop through all the balls to check ball collision with one another
        for j in range (num_ball):
            if j == i:
                continue
            p[i], p[j], v[i], v[j] = ball_collision(p[i], p[j], radius, v[i], v[j])

    # Clear screen and redraw balls with updated position values
    draw.clear()
    for i in range (num_ball):
        draw_ball(p[i][0], p[i][1], radius, colors[i])

    window.update()  # Update the screen to show all circles

######################################################### END ########################################################





