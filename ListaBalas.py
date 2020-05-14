import pygame
import Colors
from Balas import Bala
class ListaBalas:
    def __init__(self,x, y):
        self.lista_Balas = [Bala(x,y),Bala(x,y),Bala(x,y),Bala(x,y),Bala(x,y)]
        self.nro_Bala = 0

    def draw(self, pygame_window):  # pygame window es pantalla
        for i in range(0,len(self.lista_Balas)):
            self.lista_Balas[i].draw(pygame_window)
    def reset(self):
        for i in range(0,len(self.lista_Balas)):
            self.lista_Balas[i].set_x(-20)
    def set_bala(self, x, y):
        if self.nro_Bala<5:
            self.nro_Bala=0
            self.reset()
        self.lista_Balas[self.nro_Bala].set_x(x)
        self.lista_Balas[self.nro_Bala].set_x(y)
        self.nro_Bala +=1
    def move_in_y(self,main_window):
        for i in range(0,len(self.lista_Balas)):
            self.lista_Balas[i].move_in_y(main_window)
    def get_nro_bala(self):
        return  self.nro_Bala
    def sig_bala(self):
        if(self.nro_Bala<5):
            self.nro_Bala += 1
        else:
            self.nro_Bala =0

