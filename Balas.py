import pygame
import Colors


class Bala:
    def __init__(self, x, y):
        self.x = x #posicion
        self.y = y #posiciom
        self.width = 5 #ancho
        self.height = 5 #alto
    def draw(self, pygame_window): #pygame window es pantalla
        pygame.draw.rect(pygame_window, Colors.white, (self.x, self.y, self.width, self.height)) #draw = dibujar
    def move_in_y(self, pygame_window): #mover en y
        self.y -= 5
        self.draw(pygame_window) #dibuja
    def set_x(self, x):
        self.x = x+8
    def set_y(self,y):
        self.y=y
    def get_xb(self):
        return self.x
    def get_yb(self):
        return  self.y
    def bala_eliminar(self):
        self.x = -32