import pygame
from juego import juego
from Punto import BolaMovil
from Config import ANCHO_VENTANA

class smooth(juego):
    def __init__(self, screen):
        super().__init__(screen)

        ancho = self.screen.get_width()
        alto = self.screen.get_height()
        
        # Instanciamos la bola que se mueve por física, sin esperar a un temporizador
        # ya va a empezar con una velocidad media
        self.punto = BolaMovil(ancho, alto, velocidad=6) 
         
        self.tiempo_inicio = pygame.time.get_ticks()
        print("--- MODO SMOOTH PURSUIT INICIADO ---")

    def actualizar(self):
        super().actualizar()

    def dibujar(self):
        super().dibujar()
        
        # Mostrar tiempo restante
        tiempo_actual = pygame.time.get_ticks() - self.tiempo_inicio
        segundos = tiempo_actual // 1000
        
        self.dibujar_texto(f"TIEMPO: {segundos}s", ANCHO_VENTANA - 180, 10)
        self.dibujar_texto("MODO SEGUIMIENTO SUAVE", 10, 50)