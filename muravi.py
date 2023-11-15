from pygame import *
import sys

init()

screen = display.set_mode((1000,700))
display.set_caption("Муравьиная колония")


while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
    draw.rect(100,100,10,10)
    
    display.update()
