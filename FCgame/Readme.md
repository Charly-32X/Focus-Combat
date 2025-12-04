# Focus Combat - Entrenador Visual 
**Focus Combat** es una herramienta de entrenamiento visual diseñada para todo aquel que quiera mejorar el enfoque de su vista, notar pequeños cambios o hasta predecir posibles movimientos. **Su objetivo** es mejorar los tiempos de reacción, la visión periférica y el seguimiento ocular mediante ejercicios.

# ¿Por qué hice esto? La historia detras del proyecto
Todo comenzó cuando un día me topé con un video de IQFight. Para entender esto, yo entreno boxeo, aunque este año últimamente me he inclinado bastante por las artes marciales mixtas.

Viendo el video, era una narración de la vida de mi boxeador favorito, Vasily Lomachenko. En el video, en un punto se habló de sus entrenamientos; uno de ellos eran entrenamientos visuales, de análisis. Básicamente entrenaba el cerebro, pero fue uno de esos entrenamientos el que me llamó la atención: entrenaba sus reflejos utilizando únicamente la vista y tocando algún botón.

Al interesarme en eso, busqué más información, pero todos los métodos necesitaban algún botón o algo que hubiera que tocar. Así que, como estamos en la era de la IA, acudí a ella y me habló sobre el Eye training. Lo busqué, lo puse a prueba durante una semana y noté cambios: fue efectivo, podía predecir mejor los golpes y mis reflejos mejoraron ligeramente. Sin embargo, me encontré con el problema: todo estaba en formato de video de YouTube, y tarde o temprano iba a aprender los patrones. Por eso decidí crear una app que realizara todo lo del Eye training de manera aleatoria.


## Caracteristicas Principales
### 4 modos de entrenamiento:
#### - Progresivo: 
Aumenta la velocidad automaticamente cada 15s
#### - Fijo:
Puedes elegir el nivel de dificultad.
#### - Periférico:
Mantendras la vista fijada en un punto mientras analizas estimulos externos.
#### Smooth Pursuit: 
Seguimiento suave de un objetivo

### Arquitectura escalable:
Es un diseñado modular basado en POO.
### Diseño adaptativo:
Se adapta a tu resolución de pantalla.

### Cross-Platform:
Lo desarrollé en Linux, compilado para Windows mediante Docker y Wine.

## Tecnologías Utilizadas

### Lenguaje: Python 3.12

### Motor Gráfico: Pygame CE (Community Edition)

### Compilación & DevOps:

##### Docker: Para la compilación cruzada (Linux -> Windows).

##### PyInstaller: Para la generación de binarios standalone (.exe).

##### Wine: Entorno de compatibilidad.

## Instalación y Uso

### Opción A: Ejecutable (Windows)

Descarga el archivo .zip desde la sección de Releases.

Descomprime la carpeta.

Ejecuta FocusCombat.exe.

Nota: No requiere instalación de Python.

### Opción B: Ejecutar desde Código (Devs)

Requisitos: Python 3.10+

#### 1. Clonar el repositorio
git clone [https://github.com/Charly-32X/Focus-Combat.git](https://github.com/Charly-32X/Focus-Combat.git)

#### 2. Entrar a la carpeta
cd FocusCombat

#### 3. Crear entorno virtual (Opcional pero recomendado)
python -m venv venv
##### source venv/bin/activate   En Linux/Mac
##### venv\Scripts\activate    En Windows

#### 4. Instalar dependencias
pip install -r requirements.txt

#### 5. Ejecutar
python main.py

## Arquitectura del Código

### El proyecto sigue principios DRY (Don't Repeat Yourself) y patrones de diseño:

#### Clase Padre Juego: Maneja el bucle principal, eventos de ventana y renderizado base.

#### Herencia: Los modos (JuegoFijo, PerifericGame) heredan y extienden la lógica base.

#### Polimorfismo: Los objetos (Bola, BolaMovil, BolaQuieta) comparten métodos pero se comportan distinto.

#### Configuración Centralizada: Config.py maneja rutas dinámicas compatibles con sys._MEIPASS para ejecutables congelados.

