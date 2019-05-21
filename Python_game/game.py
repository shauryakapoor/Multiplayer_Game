'''Theory behind the project 
Online game development with Python 
sockets and networking to connect clients and server to connect what is know
as client or server or multiple clients to a server where they can send and
share information where they can send and share information and therefore 
we can create an online game. Massive amounts of info to the server and back
to the client. Start simply by getting eveything working on our local
network and then go ahead and deploy it on an external server which will
allow us to play from anywhere in the world and not just against people on
our local network. The way any online game work is we have multiple 
connecting to one main location known as the server. Command line will be
sending and receiving information and this is how an online game works. 
If ever an online game says, waiting for server --> Then it is doing exactly
that. Waiting to get a connection from the server and then grab information
from that. No frameworks will be used. The only thing that might be used
that is external is pygame just to create some basic graphics.
'''
import pygame 

width = 500 
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
#Use global variables after we create a caption 
#It is going to hold the current clients 
 
clientNumber = 0

class Player():
        
    def __init__(self, x, y, width, height, color):
        #ASK TA WHY IS IT NOT PROMPTING ME INIT CLASS 
        #IS THIS WHERE THE BUG IS? 
        #Just basic initialization
        self.x = x
        self.y = y
        self.width = width 
        self.height = height 
        self.color = color 
        #will make it faster when we are drawing our character
        self.rect = (x, y, width, height)
        self.vel = 3 
        
        

    def draw(self, win):
        #drawing a rectangle that represents our character on the screen
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        #check what key they press
        keys = pygame.key.get_pressed()
        #this will get us a dictionary of all the keys
        #the keys will have a value of 0 or 1
        #If 1 is true then we are pressing the key
        #If 0 we are not pressing the key
        #If you press more than 1 key at once, it will alow you to move
        #diagonally 
        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            slef.y += self.vel

def redrawWindow(win, player):
    win.fill((255, 255, 255))#white 
    player.draw(win)
    pygame.display.update()

#Game loop - Will run continiously while the game is being run 
#Will check for collisions, events, will constantly ask the server for info

def main():
    run = True 
    p = Player(50, 50, 100, 100, (0, 255, 0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p)

main()






     