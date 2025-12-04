import pygame
from juego import juego
from Punto import bola
from Config import ANCHO_VENTANA

class JuegoProgresivo(juego):
    def __init__(self, screen):
        #  Llamamos al constructor padre
        super().__init__(screen)
        
        ancho = self.screen.get_width()
        alto = self.screen.get_height()

        #  Configuración Inicial
        self.duracion_actual = 2500
        self.punto = bola(self.duracion_actual, ancho, alto)
        
        #  Temporizadores
        # Marca de tiempo de cuándo empezó el juego (para el tiempo total)
        self.tiempo_inicio_total = pygame.time.get_ticks()
        
        # Marca de tiempo de la última vez que subimos la dificultad
        self.ultimo_aumento_dificultad = pygame.time.get_ticks()

    def actualizar(self):
        # Mover la bola 
        super().actualizar()
        
        # Obtener el tiempo actual
        ahora = pygame.time.get_ticks()
        
        # Calcular cuánto tiempo ha pasado desde el último aumento
        tiempo_desde_ultimo_cambio = ahora - self.ultimo_aumento_dificultad
        
        # Si han pasado 15 segundos
        if tiempo_desde_ultimo_cambio >= 15000:
            self._aumentar_dificultad()
            # Reiniciamos el contador del intervalo
            self.ultimo_aumento_dificultad = ahora

    def _aumentar_dificultad(self):
        """Metodo privado para manejar la lógica de subir nivel"""
        
        # Verificamos que no bajemos del límite de 0.5s (500ms)
        if self.duracion_actual > 500:
            # Reducimos 500ms (0.5 segundos)
            self.duracion_actual -= 500
            
            # Actualizamos la propiedad de la bola
            self.punto.duracion = self.duracion_actual
            
            print(f"¡NIVEL SUBIDO! Nueva velocidad: {self.duracion_actual}ms")
        else:
            print("¡Velocidad Máxima alcanzada!")

    def dibujar(self):
        super().dibujar()
        
        # Calcular tiempo total jugado en segundos
        tiempo_total_ms = pygame.time.get_ticks() - self.tiempo_inicio_total
        segundos_totales = tiempo_total_ms // 1000
        
        # --- EL HUD ---
        
        #  Mostrar Tiempo Total (Arriba a la derecha)
        texto_tiempo = f"Tiempo: {segundos_totales}s"
        # Calculamos la X para que quede alineado a la derecha
        self.dibujar_texto(texto_tiempo, ANCHO_VENTANA - 180, 10)
        
        # Mostrar Velocidad Actual (Arriba a la izquierda, debajo del salir)
        # Convertimos ms a segundos
        velocidad_seg = self.duracion_actual / 1000
        texto_velocidad = f"Velocidad: {velocidad_seg}s"
        
        # Cambiamos el color según la dificultad (Visual feedback)
        color_info = (255, 255, 255)
        if self.duracion_actual <= 1000:
            color_info = (255, 50, 50) # Rojo si es muy rápido
        elif self.duracion_actual <= 2000:
            color_info = (255, 255, 0) # Amarillo si es medio
            
        self.dibujar_texto(texto_velocidad, 10, 50, color_info)
        
        # 3. Barra de progreso para el próximo nivel
        # Esto le muestra al usuario cuánto falta para los próximos 15s
        self._dibujar_barra_progreso()

    def _dibujar_barra_progreso(self):
        """Dibuja una pequeña barra abajo que se llena cada 15s"""
        ahora = pygame.time.get_ticks()
        tiempo_pasado = ahora - self.ultimo_aumento_dificultad
        porcentaje = tiempo_pasado / 15000 # 0.0 a 1.0
        
        ancho_barra = 200
        alto_barra = 5
        x = (ANCHO_VENTANA // 2) - (ancho_barra // 2)
        y = 50
        
        # Fondo de la barra
        pygame.draw.rect(self.screen, (100, 100, 100), (x, y, ancho_barra, alto_barra))
        # Barra de llenado
        pygame.draw.rect(self.screen, (0, 255, 0), (x, y, ancho_barra * porcentaje, alto_barra))