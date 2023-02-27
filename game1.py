import pgzrun

WIDTH = 300
HEIGHT = 1200

box = Rect((50,50), (150,100))
box2 = Rect((400,50),(100,100))
bvx = 2
b2vx = -2

def draw():
    screen.fill('black')
    screen.draw.filled_rect(box,'yellow')
    screen.draw.filled_rect(box,'red')
  
def update():
    global bvx,b2vx
    box.x += bvx
    box2.x += b2vx
    # check for collision
    if box.colliderect(box2):
        bvx = -bvx
        b2vx = -b2vx
        sounds.cling.play()
    # check for wall collision box
    if box2.left < 0:
       bvx = -bvx
    # check for wall collision of box2
    if box2.right > 800:
       b2vx = -b2vx    

pgzrun.go()