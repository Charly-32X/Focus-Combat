import pygame
from Config import ANCHO_VENTANA, ALTO_VENTANA, COLOR_FONDO, FPS

class juego:
     #esta clase sera para los gamee loops y todo eso

    def __init__(self, screen):
        """
        Constructor de la clase base.
        
        Args:
            screen: Superficie de pygame donde se dibuja
        """
        self.screen = screen
        self.reloj = pygame.time.Clock()
        self.ejecutando = True
        self.punto = None  # Se inicializará en las clases hijas
        
        # Fuente para texto
        self.fuente = pygame.font.Font(None, 36)
    
    def manejar_eventos(self):
        
        #Maneja los eventos comunes (cerrar ventana, ESC para salir).
        #Las clases hijas pueden extender este método.
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.ejecutando = False

    def actualizar(self):
        
        #Actualiza la lógica del juego.
        #Este método será sobrescrito por las clases hijas.
        
        if self.punto:
            self.punto.actualizar()
    
    def dibujar(self):
        
        #Dibuja los elementos comunes en pantalla.
        #Las clases hijas pueden extender este método para agregar más elementos.
        
        # Limpiar pantalla
        self.screen.fill(COLOR_FONDO)
        
        # Dibujar el punto
        if self.punto:
            self.punto.dibujar(self.screen)
        
        # Instrucción de salida
        texto_salir = self.fuente.render("ESC para salir", True, (150, 150, 150))
        self.screen.blit(texto_salir, (10, 10))

    def dibujar_texto(self, texto, x, y, color=(255, 255, 255)):
        """
        Método auxiliar para dibujar texto en pantalla.
        
        Args:
            texto (str): Texto a mostrar
            x (int): Posición X
            y (int): Posición Y
            color (tuple): Color RGB del texto
        """
        superficie_texto = self.fuente.render(texto, True, color)
        self.screen.blit(superficie_texto, (x, y))
    
    def ejecutar(self):
        
        #Game loop principal.
        
        while self.ejecutando:
            # 1. Manejar eventos (input del usuario)
            self.manejar_eventos()
            
            # 2. Actualizar lógica del juego
            self.actualizar()
            
            # 3. Dibujar todo en pantalla
            self.dibujar()
            
            # 4. Actualizar la pantalla
            pygame.display.flip()
            
            # 5. Controlar FPS
            self.reloj.tick(FPS)