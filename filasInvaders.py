from invader import Invader
from  Balas import Bala
from Suelo import Suelo

class FilaInvaders:
    def __init__(self,x, y,vel):
        self.lista_invaders = [Invader(x,y,vel),Invader(x+60,y,vel),Invader(x+120,y,vel),Invader(x+180,y,vel)]

    def draw(self, pygame_window):
        for i in range(0, len(self.lista_invaders)):
            self.lista_invaders[i].draw(pygame_window)
    def movimiento(self,main_window, aux):
        for i in range(0, len(self.lista_invaders)):
            self.lista_invaders[i].movimiento(main_window,aux)
    def choque_bala(self,bala_x,nroInvaders):
        for i in range(0, len(self.lista_invaders)):
            if bala_x.get_xb() >= self.lista_invaders[i].get_xi() - 4 and bala_x.get_xb() <= (self.lista_invaders[i].get_xi() + 20):
                if bala_x.get_yb() >= self.lista_invaders[i].get_yi() - 4 and bala_x.get_yb() <= (self.lista_invaders[i].get_yi() + 20):
                    self.lista_invaders[i].eliminar()
                    bala_x.bala_eliminar()
                    nroInvaders.InvDead()


    def choque_suelo(self):
        for i in range(0, len(self.lista_invaders)):
            return self.lista_invaders[i].get_yi()