import pygame
from juego import juego
from Punto import bola
from Config import DIFICULTADES

class juego_fijo(juego):
    def __init__(self, screen, dificultad):
        #es el constructor del modo de juego fijo

        #aqui llama al constrcutor de la clase juego
        super().__init__(screen)

        ancho = self.screen.get_width()
        alto = self.screen.get_height()

        #Aqui obtenemos la duración segun las dificultades que eligamos
        duracion = DIFICULTADES[dificultad]

        #crea el punto con la duracion fija
        self.punto = bola(duracion, ancho, alto)

        #aqui guarda la info de la dificultad para mostrarla
        self.dificultad = dificultad
        self.duracion_Segundos = duracion/1000

    def dibujar(self):
        #aqui usamos la def de clase juego para extender lo que hace en juego fijo
        super().dibujar()

        #aqui agregamos la info especifica del modo fijo, como segundos, dificultad y eso.

        texto_dificultad = f"Modo: {self.dificultad.upper()} - {self.duracion_Segundos}-s"
        self.dibujar_texto(texto_dificultad, 10, 50, (200,200,200))

        