import pygame
import Colors
from invader import Invader
from Player import Player
from Balas import Bala
from  filasInvaders import FilaInvaders
from TropaInvaders import TropasInvaders
from  ListaBalas import ListaBalas
from Suelo import Suelo
from Events import NroInvader


def choque(invader_x,bala_x):
    if bala_x.get_xb() >= invader_x.get_xi()-4 and bala_x.get_xb() <= (invader_x.get_xi()+20):
        if bala_x.get_yb() >= invader_x.get_yi()-4 and bala_x.get_yb() <= (invader_x.get_yi()+20):
            invader_x.eliminar()

pygame.init() #inicia pygame
window_width = 320 #tamaño de pantalla
window_height = 600
window_size = (window_width, window_height) #ensierra en una tupla los valores de tamaño
main_window = pygame.display.set_mode(window_size) #crea la pantalla
aux = 0
pygame.display.set_caption("Project") #nombre de la pantalla

x = 160 #x player
y = 560 #y player

width = 20 #player
height = 20 #player

vel_player = 1 #velocidad
vel_invader = 0.2
running_game = True #si va a correr o no el juego
nro_invader = NroInvader(16)



sw=True
suelo1 = Suelo()
#inv_1 = Invader(20, 30, vel_invader) #crea al invader[(,)posicion inicial]
#fila_inv = FilaInvaders(20,30,vel_invader)
tropa_inv = TropasInvaders(20,30,vel_invader)
player_1 = Player(x,y,vel_player)
#Lista_balas = ListaBalas(-20,-20)
bala = Bala(-10,player_1.get_yp())
while running_game:
    pygame.time.delay(10) #refresca los pixeles (1000 = 1 sg)
    main_window.fill(Colors.black)  # fill = llenar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
            break
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
       player_1.movIzq()

    if keys[pygame.K_RIGHT] and x < 500 - width:
        player_1.movDer()

    #if keys[pygame.K_UP] and y > 0:
     #   y -= vel

    #if keys[pygame.K_DOWN] and y < 500 - height:
     #   y += vel
    if keys[pygame.K_SPACE] :
        #Lista_balas.set_bala(player_1.get_xp(),player_1.get_yp())
        #Lista_balas.draw(main_window)

        #Lista_balas.lista_Balas[Lista_balas.get_nro_bala()%5].set_x(player_1.get_xp())
        #Lista_balas.lista_Balas[Lista_balas.get_nro_bala()%5].set_y(player_1.get_yp())
        #Lista_balas.sig_bala()
        bala.set_x(player_1.get_xp())
        bala.set_y(player_1.get_yp())
        bala.draw(main_window)
    if aux<400:
        aux +=1
    else:
        aux=0


    suelo1.draw(main_window)
    #inv_1.draw(main_window) #dibujar invader 1
    #fila_inv.draw(main_window)
    tropa_inv.draw(main_window)
    #inv_1.move_in_y(main_window) #mover el invader
    #inv_1.movimiento(main_window,aux)
    #fila_inv.movimiento(main_window,aux)
    tropa_inv.movimiento(main_window,aux)
    player_1.draw(main_window)
    bala.move_in_y(main_window)
    #Lista_balas.move_in_y(main_window)
    #choque(inv_1,bala)
    #fila_inv.choque_bala(bala)
    tropa_inv.choque_bala(bala,nro_invader)

    if nro_invader.get_xnro() == 0:
        running_game = False

    if tropa_inv.choque_suelo():
        running_game = False




    #pygame.draw.rect(main_window, Colors.red, (x, y, width, height)) #dibuja al player


    pygame.display.update() #borrar la imagen

pygame.quit() #termina el juego
#devci la paz
#facebook developers circus la paz
