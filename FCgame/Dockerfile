# Usamos la imagen de tobix/pywine (porque soy de linux)
FROM tobix/pywine:3.12

# 1. Instalamos dependencias usando 'wine python'
# El comando 'wine' es el puente para usar el Python de Windows instalado dentro
RUN wine python -m pip install --upgrade pip
RUN wine python -m pip install pygame-ce pyinstaller

# 2. Copiamos los archivos
COPY . /src/
WORKDIR /src/

# 3. El comando para compilar
# Cambiamos "pyinstaller" por "wine python -m PyInstaller" para invocarlo como módulo
# Esto es más seguro y evita errores de "comando no encontrado"
ENTRYPOINT ["wine", "python", "-m", "PyInstaller", "--clean", "-y", "--onefile", "--windowed", "--name", "FocusCombat", "--distpath", "/src/dist/windows", "--add-data", "Assets;Assets", "main.py"]