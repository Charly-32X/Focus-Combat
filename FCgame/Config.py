#EN este archivo iran todas las configuraciones, pantalla, fps, dificultad, etc
import pygame
import os
import sys

# --- FUNCIÓN  PARA RUTAS  --
def obtener_ruta_recurso(ruta_relativa):
    # 1. Si estamos en un .exe (PyInstaller crea _MEIPASS)
    if hasattr(sys, '_MEIPASS'):
        # Buscamos DENTRO del archivo temporal del .exe
        base_path = sys._MEIPASS
    else:
        # 2. Si estamos en modo normal (.py)
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, ruta_relativa)


#vamos a inicializar pygame para obtener informacion del monitor
pygame.init()
monitor = pygame.display.Info()

#configuración de la pantalla 
ANCHO_VENTANA = int(monitor.current_w*0.7) #esto es para que este al 70% del ancho del monitor
ALTO_VENTANA = int(monitor.current_h*0.7) #lo mismo de arriba pero con lo alto
TITULO_VENTANA = "Focus Combat - Entrenador Visual"
FPS= 60
#------------------------------------------------------

#Los colores( en formato rgb)
COLOR_FONDO = (0, 0, 0) #GRIS
COLOR_PUNTO = (255, 0, 0) #ROJO
COLOR_TEXTO = (255, 255, 255) #BLANCO
COLOR_BOLA_QUIETA = (153,50,204) #MOrado DarkOrchid
#------------------------------------------------------

#Configuración del punto
RADIO_PUNTO = 25
#_--------------------------------------

#Los niveles de dificultad
DIFICULTADES = {
    "Facil": 2000,
    "Medio": 1000,
    "Dificil": 300
}
#------------------------------------

#Configuración del menu
OPCIONES_MENU = {
    1:"Facil",
    2:"Medio",
    3:"Dificil"
}
#---------------------------------------

#esta es la configuración de la fuente
Archivo_fuente_name_titulo = "Assets/Fonts/ScienceGothic-VariableFont_CTRS,slnt,wdth,wght.ttf"
Archivo_fuente_name_subtitulo = "Assets/Fonts/TiroTamil-Italic.ttf"
titulo_size = 80
botones_size = 30