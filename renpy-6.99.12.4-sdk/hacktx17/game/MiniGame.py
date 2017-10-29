#Visual Novel Sriracha- HackTX17 10/29/17
#Minigame code was based off from this site:
#https://pythonspot.com/en/snake-with-pygame/ <- code guide for minigame
#Step by step guide to create a snake minigame
#Verision that crashes and is not responsive when loaded onto game 


import random, os.path

#import basic pygame modules
import renpygame as pygame
from renpygame.locals import *

import renpy.store as store
import renpy.exports as renpy
from random import randint
import time
from pygame import surface

SCREENRECT     = Rect(0, 0, 640, 480)
SCORE = 0

def os_path_join(a, b):
    return a + "/" + b

class Apple:
    x = 0
    y = 0
    step = 44
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
 
 
class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[1] = 1*44
       self.x[2] = 2*44
 
    def update(self):
 
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
            self.updateCount = 0
 
 
    def moveRight(self):
        self.direction = 0
 
    def moveLeft(self):
        self.direction = 1
 
    def moveUp(self):
        self.direction = 2
 
    def moveDown(self):
        self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
 
class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False
 
class App:
 
    windowWidth = 800
    windowHeight = 600
    player = 0
    apple = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.player = Player(3) 
        self.apple = Apple(5,5)
        self.counter = 0;
        self.check = True
    
    def load_image(self,file):
        "loads an image, prepares it for play"
        #file = os_path_join('data', file)
        try:
            surface = pygame.image.load(file)
        except pygame.error:
            raise SystemExit, 'Could not load image "%s" %s'%(file, pygame.get_error())
        return surface.convert()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('MiniGame')
        self._running = True
        self._image_surf = self.load_image('Block.png')
        self._apple_surf = self.load_image('Chilli.png')
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.player.update()
        # does snake eat apple
        if self.check == True:
            for i in range(0,self.player.length):
                if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],44):
                   self.apple.x = randint(2,9) * 44
                   self.apple.y = randint(2,9) * 44
                   self.player.length = self.player.length + 1
                   self.counter = self.counter + 1;
          #check if it collides with wall       
            for i in range(2,self.player.length):
                if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[0],self.windowHeight,40):
                   time.sleep(5)
                   self.check = False
            pass
    
            for i in range(3,self.player.length):
                if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[0],0,40):
                   print(self.counter)
                   time.sleep(5)
                   self.check = False
            pass
    
            for i in range(4,self.player.length):
                if self.game.isCollision(self.player.x[0],self.player.y[0],0,self.player.y[0],40):
                   print(self.counter)
                   time.sleep(5)
                   self.check = False
            pass

            for i in range(0,self.player.length):
                if self.game.isCollision(self.player.x[0],self.player.y[0],self.windowWidth,self.player.y[0],40):
                   print(self.counter)
                   time.sleep(5)
                   self.check = False
            pass
        # does snake collide with itself?
            for i in range(2,self.player.length):
                if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],40):
                   print(self.counter)
                   time.sleep(10)
                   self.check = False
            pass 
        else:
            pass
    def gameCounter(self):
        return self.counter
       
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        #font = pygame.font.Font(None, 36)
        #text = font.render(str(self.counter), 1, (255, 255, 255))
        #self._display_surf.blit(text,(50,50))
        #pygame.display.flip()
 
    def on_cleanup(self):

        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[K_RIGHT]):
                self.player.moveRight()
 
            if (keys[K_LEFT]):
                self.player.moveLeft()
 
            if (keys[K_UP]):
                self.player.moveUp()
 
            if (keys[K_DOWN]):
                self.player.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
 
            time.sleep (30.0 / 1000.0);
        self.on_cleanup()

def main(winstyle = 0):
    pygame.init()
    if store._preferences.fullscreen:
        winstyle = FULLSCREEN
    else:
        winstyle = 0

    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    theApp = App()
    theApp.on_execute()
    return gameCounter()

if __name__ == "__main__" :
    main()