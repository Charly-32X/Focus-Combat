import pygame
from Config import COLOR_FONDO, COLOR_TEXTO, Archivo_fuente_name_titulo, Archivo_fuente_name_subtitulo, titulo_size, botones_size

class boton:
    def __init__(self, x, y, ancho, alto, texto, accion):
        # Este es el constructor
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.accion = accion

        self.color_original = (125, 14, 14)
        self.color_hover = (255, 10, 10)
        self.color_actual = self.color_original

        self.texto_fuente = pygame.font.Font(Archivo_fuente_name_subtitulo, botones_size)

    def actualizar(self, mouse_pos):
        # Al pasar el mouse, el color cambia.
        if self.rect.collidepoint(mouse_pos):
            self.color_actual = self.color_hover
        else:
            self.color_actual = self.color_original
    
    def dibujar(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.rect.x + 4, self.rect.y + 4, self.rect.width, self.rect.height))

        pygame.draw.rect(screen, self.color_actual, self.rect)
        pygame.draw.rect(screen, COLOR_TEXTO, self.rect, 2)

        texto_superficie = self.texto_fuente.render(self.texto, True, COLOR_TEXTO)
        texto_rect = texto_superficie.get_rect(center=self.rect.center)
        screen.blit(texto_superficie, texto_rect)

    def click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.activo = True
        self.pantalla_actual = "principal" 

        try:
            self.fuente_titulo = pygame.font.Font(Archivo_fuente_name_titulo, titulo_size)
            self.fuente_subtitulo = pygame.font.Font(Archivo_fuente_name_subtitulo, botones_size)
        except:
            self.fuente_titulo = pygame.font.Font(None, titulo_size)
            self.fuente_subtitulo = pygame.font.Font(None, botones_size)
        
        self.modo_elegido = None
        self.dificultad_elegida = None

        # metodos para la seleccion de los modos de juego
        self.botones_principal = self.crear_botones_principal()
        self.botones_dificultades = self.crear_botones_dificultades()

    def crear_botones_principal(self):

        ancho = self.screen.get_width()
        alto = self.screen.get_height()

        #altura
        centro_x = ancho//2
        inicio_y = int(alto*0.4)

        #tamaño de los botones
        ancho = 300
        alto = 70 
        separacion = 30

        botones = []

        # FILA 1: TRES BOTONES ---
        
        # 1. Botón Central 
        x_centro = centro_x - (ancho // 2)
        botones.append(boton(x_centro, inicio_y, ancho, alto, "PERIFÉRICO", "periferica"))
        botones.append(boton(x_centro, inicio_y+120, ancho, alto, "SMOOTH PURSUIT", "smooth"))
        
        # 2. Botón Izquierdo 
        x_izq = x_centro - ancho - separacion
        botones.append(boton(x_izq, inicio_y, ancho, alto, "PROGRESIVO", "progresivo"))
        
        # 3. Botón Derecho
        x_der = x_centro + ancho + separacion
        botones.append(boton(x_der, inicio_y, ancho, alto, "MODO FIJO", "fijo"))
        
        # --- FILA 2: SALIR ---
        y_abajo = inicio_y + alto + 150
        botones.append(boton(x_centro, y_abajo, ancho, alto, "SALIR", "salir"))

        return botones

    def crear_botones_dificultades(self):

        ancho = self.screen.get_width()
        alto = self.screen.get_height()

        centro_x = ancho // 2
        inicio_y = int(alto * 0.35)

        ancho = 350
        alto = 70
        espacio = 90
        
        return [
            boton(centro_x - ancho//2, inicio_y, ancho, alto, "FÁCIL", "Facil"),
            boton(centro_x - ancho//2, inicio_y + espacio, ancho, alto, "MEDIO", "Medio"),
            boton(centro_x - ancho//2, inicio_y + espacio * 2, ancho, alto, "DIFÍCIL", "Dificil"),
            boton(centro_x - ancho//2, inicio_y + espacio * 3, ancho, alto, "VOLVER", "volver")
        ]

    def manejar_eventos(self):
        mouse_pos = pygame.mouse.get_pos()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.activo = False
                self.modo_elegido = "salir"
                return
            
            if evento.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((evento.w, evento.h), pygame.RESIZABLE)
                self.botones_principal = self.crear_botones_principal()
                self.botones_dificultades = self.crear_botones_dificultades()
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                self._manejar_click(mouse_pos)
        
        botones_activos = self.botones_principal if self.pantalla_actual == "principal" else self.botones_dificultades
        for b in botones_activos:
            b.actualizar(mouse_pos)

    def _manejar_click(self, mouse_pos):
        if self.pantalla_actual == "principal":
            for b in self.botones_principal:
                if b.click(mouse_pos):
                    if b.accion == "progresivo":
                        self.modo_elegido = "progresivo"
                        self.activo = False 
                    elif b.accion == "fijo":
                        self.pantalla_actual = "dificultades"
                    if b.accion == "periferica":
                        self.modo_elegido = "periferica"
                        self.activo = False
                    if b.accion == "smooth":
                        self.modo_elegido = "smooth"
                        self.activo = False
                    elif b.accion == "salir":
                        self.modo_elegido = "salir"
                        self.activo = False
                            
        elif self.pantalla_actual == "dificultades":
            for b in self.botones_dificultades:
                if b.click(mouse_pos):
                    if b.accion == "volver":
                        self.pantalla_actual = "principal"
                    else:
                        self.modo_elegido = "fijo"
                        self.dificultad_elegida = b.accion
                        self.activo = False

    def dibujar(self):
        self.screen.fill(COLOR_FONDO)

        ancho = self.screen.get_width()
        
        titulo_texto = "DIFICULTAD" if self.pantalla_actual == "dificultades" else "FOCUS COMBAT"
        titulo = self.fuente_titulo.render(titulo_texto, True, COLOR_TEXTO)
        self.screen.blit(titulo, titulo.get_rect(center=(ancho//2, 150)))

        botones = self.botones_principal if self.pantalla_actual == "principal" else self.botones_dificultades
        for b in botones:
            b.dibujar(self.screen)
            
        pygame.display.flip()

    def ejecutar(self):
        reloj = pygame.time.Clock()
        while self.activo:
            self.manejar_eventos()
            self.dibujar()
            reloj.tick(60)
        return self.modo_elegido, self.dificultad_elegida