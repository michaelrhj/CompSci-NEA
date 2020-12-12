import pygame, math, sys, random, copy
from pygame.locals import *



pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Home")


def home():
    Login_Button = Button("Login",100,450,60,200,screen)
    running =  True
    while running:
        screen.fill(WHITE)
        Login_Button.DisplayButton()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exity()
        pygame.display.update()


if __name__ == "__main__":
    home()
