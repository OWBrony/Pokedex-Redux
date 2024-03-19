from Constants import *
import pygame
class director():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.run = True

    def main_loop(self):
        while self.run:
             self._handle_input()
            #  self._draw()

    def _handle_input(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
    
    def _draw(self):
        #  self.screen.blit((0, 0))
        pass