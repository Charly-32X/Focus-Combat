import pygame
import sys

#las configuracion
from Config import ALTO_VENTANA, ANCHO_VENTANA, TITULO_VENTANA

#el menu
from menu import Menu

#los modos de juego
from juego_progesivo import JuegoProgresivo
from juego_fijo import juego_fijo
from perifericGame import periferic_Game
from smooth import smooth

def main ():
    #es la inicializacion del juego
    pygame.init()

    #la screen o ventana
    screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), pygame.RESIZABLE)
    pygame.display.set_caption(TITULO_VENTANA)

    #este bucle permite poder seleccionar el modo que quieras.
    while True:

        #ya aqui se ejecuta el menu
        menu_iniciar =  Menu(screen)

        #aqui se guarda lo que elige el usuario en el menu.
        modo_Elegido, dificultad_elegida = menu_iniciar.ejecutar()

        if modo_Elegido == "salir" or modo_Elegido is None:
            print("Saliendo del juego")
            break


        if modo_Elegido == "progresivo":
            print("Iniciando modo de juego Progesivo.")
            juego_Actual = JuegoProgresivo(screen)

        elif modo_Elegido == "periferica":
            print("Iniciando modo vista periferica")
            juego_Actual = periferic_Game(screen)

        elif modo_Elegido == "smooth":
            print("iniciando modo smooth visual")
            juego_Actual = smooth(screen)

        elif modo_Elegido == "fijo":
            print("Iniciando modo de juego Fijo.")
            juego_Actual = juego_fijo(screen, dificultad_elegida)

        
        #aqui se ejecuta el juego seleccionado
        if juego_Actual:
            juego_Actual.ejecutar()

    pygame.quit()
    sys.exit()

if __name__=="__main__":
    main()