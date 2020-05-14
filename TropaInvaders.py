from filasInvaders import FilaInvaders

class TropasInvaders:
    def __init__(self, x, y, vel):
        self.tropa_invader = [FilaInvaders(x,y,vel),FilaInvaders(x+30,y+30,vel),FilaInvaders(x,y+60,vel),FilaInvaders(x+30,y+90,vel)]
    def draw(self, pygame_window):
        for i in range(0, len(self.tropa_invader)):
            self.tropa_invader[i].draw(pygame_window)
    def movimiento(self,main_window, aux):
        for i in range(0, len(self.tropa_invader)):
            self.tropa_invader[i].movimiento(main_window,aux)

    def choque_bala(self, bala_x,nroInvaders):
        for i in range(0, len(self.tropa_invader)):
            self.tropa_invader[i].choque_bala(bala_x,nroInvaders)


    def choque_suelo(self):
        for i in range(0, len(self.tropa_invader)):
            if self.tropa_invader[i].choque_suelo()+90 > 560:
                return True
            else:
                return False
