## Focus Combat - Entrenador Visual Proactivo

Focus Combat es una herramienta de entrenamiento visual de alto rendimiento diseñada para mejorar el enfoque, la visión periférica y los tiempos de reacción. Inspirada en métodos de entrenamiento de élite, esta aplicación soluciona el problema de la predictibilidad en los ejercicios visuales convencionales.

# ¿Por qué hice esto? La historia detrás del proyecto

Todo comenzó analizando la metodología de entrenamiento de Vasily Lomachenko (vía IQFight). Como practicante de Boxeo y MMA, me fascinó cómo los atletas de élite integran el entrenamiento cognitivo y visual para anticipar movimientos y mejorar la toma de decisiones en el ring.

Al investigar herramientas de "Eye Training", encontré dos problemas:

Las herramientas profesionales requieren hardware costoso.

Los entrenamientos gratuitos en YouTube son videos estáticos.

El problema de los videos: Con la práctica constante, el cerebro memoriza los patrones del video. El entrenamiento deja de ser reactivo para volverse mecánico.

Para solucionar esto, desarrollé Focus Combat: una aplicación que genera estímulos 100% aleatorios y procedimentales, asegurando que el usuario nunca pueda predecir el siguiente movimiento y forzando al sistema nervioso a mantenerse en un estado de alerta real.

#  Características Principales

# 4 Modos de Entrenamiento:

 Progresivo: La dificultad y velocidad escalan automáticamente cada 15 segundos para llevar tus reflejos al límite.

Fijo: Entrenamiento de consistencia con niveles de dificultad seleccionables.

 Periférico: Entrenamiento de campo visual amplio; mantén la vista en el centro mientras reaccionas a estímulos en los bordes.

 Smooth Pursuit: Seguimiento fluido de objetivos con física de rebote para mejorar la coordinación ocular.

# Ingeniería y Adaptabilidad:

Diseño Adaptativo: La interfaz utiliza cálculos matemáticos dinámicos para ajustarse a cualquier resolución de pantalla.

Arquitectura POO: Código modular basado en clases, herencia y polimorfismo para facilitar la expansión.

# Tecnologías Utilizadas

Lenguaje: Python 3.12

Motor Gráfico: Pygame CE (Community Edition)

DevOps & Compilación:

Docker: Para asegurar un entorno de compilación reproducible.

Wine: Utilizado dentro de Docker para generar binarios de Windows desde Linux.

PyInstaller: Para empaquetar la aplicación en un ejecutable standalone.

##  Instalación y Uso

Usuarios (Windows)

Ve a la sección de Releases.

Descarga el archivo .zip.

Descomprime y ejecuta FocusCombat.exe. No requiere instalación previa.

### Desarrolladores (Linux/Windows)

# Clonar y configurar entorno
git clone [https://github.com/TU_USUARIO/FocusCombat.git](https://github.com/TU_USUARIO/FocusCombat.git)
cd FocusCombat
python -m venv venv
source venv/bin/activate  # Linux
pip install -r requirements.txt

# Ejecutar
python FCgame/main.py


# Arquitectura del Software

El proyecto fue construido bajo principios de ingeniería de software para ser mantenible:

Clase Base Juego: Gestiona el ciclo de vida del juego (Game Loop) y eventos globales.

Herencia: Cada modo de juego es una clase que extiende la funcionalidad base.

Configuración Dinámica: Uso de sys._MEIPASS para garantizar que los Assets se carguen correctamente tanto en desarrollo como en producción.

Desarrollado con ❤️ por [Charly Xol]
