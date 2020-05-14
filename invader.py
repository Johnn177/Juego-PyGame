import pygame
import Colors


class Invader:
    def __init__(self, x, y, vel):
        self.x = x #posicion
        self.y = y #posiciom
        self.vel = vel
        self.width = 20 #ancho
        self.height = 20 #alto

    def draw(self, pygame_window): #pygame window es pantalla
        pygame.draw.rect(pygame_window, Colors.white, (self.x, self.y, self.width, self.height)) #draw = dibujar

    def move_in_y(self, pygame_window): #mover en y
        self.y += self.vel
        self.draw(pygame_window) #dibuja
    def eliminar(self):
        self.x = -100
    def get_xi(self):
        return self.x
    def get_yi(self):
        return self.y
    def movimiento(self, pygame_window,valor):
        if valor >=0 and valor <100:
            self.y += self.vel
            self.draw(pygame_window)  # dibuja
        if valor >= 100 and valor < 200:
            self.x += self.vel
            self.draw(pygame_window)  # dibuja
        if valor >=200 and valor <300:
            self.y += self.vel
            self.draw(pygame_window)  # dibuja
        if valor >=300 and valor <400:
            self.x -= self.vel
            self.draw(pygame_window)  # dibuja
    def choque_suelo(self):
        if self.y >0:
            return True
    # def update(self):