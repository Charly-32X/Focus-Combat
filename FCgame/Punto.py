import pygame
import random
from Config import ANCHO_VENTANA, ALTO_VENTANA, COLOR_PUNTO, RADIO_PUNTO

class bola:  #la bola va a representar el objeto que vamos a ver y esta clase tendra varias funciones
    def __init__(self, duracion):
        #esta funcion construye a la bolita o la inicializa mejor dicho

        #la posición de la bola, sus atributos.
        self.x = ANCHO_VENTANA // 2
        self.y = ALTO_VENTANA // 2

        #lo visual, atributos visuales
        self.radio = RADIO_PUNTO
        self.color = COLOR_PUNTO

        #atributos del tiempo

        self.duracion = duracion
        self.ultima_aparicion = pygame.time.get_ticks() #guarda el tiempo con el que se inicia

    def actualizar(self):
       #Esto verifica si el punto se debe mover de nuevo

       tiempo_Actual = pygame.time.get_ticks()
       tiempo_transcurrido = tiempo_Actual-self.ultima_aparicion

       #una condicion para que se mueva cuando ya paso el tiempo

       if tiempo_transcurrido>=self.duracion:
           self.mover_random()
           self.ultima_aparicion = tiempo_Actual #esto resetea el tiempo
    
    def mover_random(self):
        #para mover la bola dentro de la ventana
        self.x = random.randint(self.radio, ANCHO_VENTANA - self.radio)
        self.y = random.randint(self.radio, ALTO_VENTANA - self.radio)

    def dibujar(self, screen):
        #esto es para que la bola exista, se dibuje sola.

        pygame.draw.circle(screen ,self.color, (self.x, self.y), self.radio)
