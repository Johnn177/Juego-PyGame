from invader import Invader

class NroInvader:
    def __init__(self, x):
        self.x = x
    def InvDead(self):
        self.x -=1
    def get_xnro(self):
        return self.x