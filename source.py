import pygame 
from pygame.locals import *
from sys import exit
from random import *
import multiprocessing
import time

def process_image1():
  
  for i in range(250000):
    random_color = (randint(0,255), randint(0,255), randint(0,255))
    random_pos = (randint(0,639), randint(0,479))
    random_size = (639-randint(random_pos[0], 639), 479-randint(random_pos[1],479))
    
    rectangles1.append(Rectangle(random_pos, random_color, random_size))
  
def process_image2():
  
  for i in range(250000):
    random_color = (randint(0,255), randint(0,255), randint(0,255))
    random_pos = (randint(0,639), randint(0,479))
    random_size = (639-randint(random_pos[0], 639), 479-randint(random_pos[1],479))
    
    rectangles2.append(Rectangle(random_pos, random_color, random_size))
  

def process_image3():
  
  for i in range(250000):
    random_color = (randint(0,255), randint(0,255), randint(0,255))
    random_pos = (randint(0,639), randint(0,479))
    random_size = (639-randint(random_pos[0], 639), 479-randint(random_pos[1],479))
    
    rectangles3.append(Rectangle(random_pos, random_color, random_size))
  

def process_image4():
  
  for i in range(250000):
    random_color = (randint(0,255), randint(0,255), randint(0,255))
    random_pos = (randint(0,639), randint(0,479))
    random_size = (639-randint(random_pos[0], 639), 479-randint(random_pos[1],479))
    
    rectangles4.append(Rectangle(random_pos, random_color, random_size))
  
    
  
  
class Rectangle:
    def __init__(self, pos, color, size):
        self.pos = pos
        self.color = color
        self.size = size
    def draw(self):
        pygame.draw.rect(screen, self.color, Rect(self.pos, self.size))

rectangles1 = []
rectangles2 = []
rectangles3 = []
rectangles4 = []
p1 = multiprocessing.Process(target=process_image1())
p1.start()
p2 = multiprocessing.Process(target=process_image2())
p2.start()
p3 = multiprocessing.Process(target=process_image3())
p3.start()
p4 = multiprocessing.Process(target=process_image4())
p4.start()
p1.join()
p2.join()
p3.join()
p4.join()

pygame.init()

screen = pygame.display.set_mode((640, 480), 0,32)
while 1:


 
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.lock()
    for rectangle in rectangles1:
      rectangle.draw()
    for rectangle in rectangles2:
      rectangle.draw()
    for rectangle in rectangles3:
      rectangle.draw()
    screen.unlock()
    pygame.display.update()

