import pygame
import Colors

class Player:
    def __init__(self, x, y, vel):
        self.x = x #posicion
        self.y = y #posiciom
        self.vel = vel
        self.width = 20 #ancho
        self.height = 20 #alto

    def draw(self, pygame_window): #pygame window es pantalla
        pygame.draw.rect(pygame_window, Colors.white, (self.x, self.y, self.width, self.height)) #draw = dibujar
    def movIzq(self):
        if self.x>0:
            self.x -= self.vel
    def movDer(self):
        if self.x < 500:
            self.x += self.vel
    def get_xp(self):
        return self.x
    def get_yp(self):
        return self.y