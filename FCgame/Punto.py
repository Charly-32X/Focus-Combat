import pygame
import random
from Config import COLOR_PUNTO, RADIO_PUNTO, COLOR_BOLA_QUIETA

class bola:  #la bola va a representar el objeto que vamos a ver y esta clase tendra varias funciones
    def __init__(self, duracion, screen_width, screen_heigth):
        #esta funcion construye a la bolita o la inicializa mejor dicho

        #la posición de la bola, sus atributos.
        self.x = screen_width // 2
        self.y = screen_heigth // 2

        #lo visual, atributos visuales
        self.radio = RADIO_PUNTO
        self.color = COLOR_PUNTO

        #atributos del tiempo

        self.duracion = duracion
        self.ultima_aparicion = pygame.time.get_ticks() #guarda el tiempo con el que se inicia

    def actualizar(self, screen_width, screen_heigth):
       #Esto verifica si el punto se debe mover de nuevo

       tiempo_Actual = pygame.time.get_ticks()
       tiempo_transcurrido = tiempo_Actual-self.ultima_aparicion

       #una condicion para que se mueva cuando ya paso el tiempo

       if tiempo_transcurrido>=self.duracion:
           self.mover_random(screen_width, screen_heigth)
           self.ultima_aparicion = tiempo_Actual #esto resetea el tiempo
    
    def mover_random(self, screen_width, screen_heigth):
        #para mover la bola dentro de la ventana
        self.x = random.randint(self.radio, screen_width  - self.radio)
        self.y = random.randint(self.radio, screen_heigth - self.radio)

    def dibujar(self, screen):
        #esto es para que la bola exista, se dibuje sola.

        pygame.draw.circle(screen ,self.color, (self.x, self.y), self.radio)

class bola_quieta:
    #esta bolita, como su nombre lo dice esta quieta, no voy darle herencia pq no me sirve tanto

    def __init__(self, screen_width, screen_heigth) :
        #la constructora
        #es la posicon de la bola
        self.x = screen_width//2
        self.y = screen_heigth//2

        #atributos visuales
        self.radio = RADIO_PUNTO - 5
        self.color = COLOR_BOLA_QUIETA

    def dibujar(self, screen):
        #aqui se dibujara en el centro.

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radio)


class BolaMovil(bola):
    def __init__(self,screen_width, screen_heigth, velocidad=5):
        # el constrcutor pero en la duracion le damos 0 para que no se mantenga quieta x tiempo
        super().__init__(duracion=0, screen_width=screen_width, screen_heigth=screen_heigth)
        
        # Velocidad en X y Y (Dirección)
        # tambien se elige una dirección al azar.
        self.dx = random.choice([-1, 1]) * velocidad
        self.dy = random.choice([-1, 1]) * velocidad
        
        # Empezamos en una posición aleatoria segura
        self.mover_random(screen_width, screen_heigth)

    def actualizar(self, screen_width, screen_heigth):
        # el movimiento ese
        # En lugar de esperar un tiempo, nos movemos un poquito en cada frame
        self.x += self.dx
        self.y += self.dy

        # Lógica para el rebote
        # Si choca a la derecha o izquierda, invierte la dirección X
        if self.x >= screen_width - self.radio or self.x <= self.radio:
            self.dx *= -1
            
        # Si choca arriba o abajo, invierte la dirección Y
        if self.y >= screen_heigth - self.radio or self.y <= self.radio:
            self.dy *= -1