import pygame
import Colors

class Suelo:
    def __init__(self):
        self.x = 0 #posicion
        self.y = 580 #posiciom
        self.width = 600 #ancho
        self.height = 20 #alto
    def draw(self, pygame_window): #pygame window es pantalla
        pygame.draw.rect(pygame_window, Colors.white, (self.x, self.y, self.width, self.height)) #draw = dibujar
    def get_ys(self):
        return self.y