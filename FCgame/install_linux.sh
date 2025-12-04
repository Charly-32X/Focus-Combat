#!/bin/bash

# 1. Obtener la ruta actual absoluta (donde está main.py)
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ICONO="$DIR/Assets/icono.png" 

echo "📂 Directorio del juego: $DIR"

# 2. BÚSQUEDA INTELIGENTE DEL PYTHON
POSIBLES_RUTAS=(
    "$DIR/venv/bin/python3"       
    "$DIR/.venv/bin/python3"      
    "$DIR/../venv/bin/python3"    
    "$DIR/../.venv/bin/python3"   
    "$DIR/../env/bin/python3"
)

PYTHON_EXEC=""

for ruta in "${POSIBLES_RUTAS[@]}"; do
    if [ -f "$ruta" ] && [ -x "$ruta" ]; then
        DIR_PADRE=$(dirname "$ruta")
        NOMBRE_EJECUTABLE=$(basename "$ruta")
        RUTA_ABSOLUTA_DIR=$(cd "$DIR_PADRE" && pwd)
        PYTHON_EXEC="$RUTA_ABSOLUTA_DIR/$NOMBRE_EJECUTABLE"
        echo "✅ ¡Eureka! Usando Python del venv: $PYTHON_EXEC"
        break
    fi
done

if [ -z "$PYTHON_EXEC" ]; then
    echo "❌ ERROR: No encontré el entorno virtual."
    PYTHON_EXEC="/usr/bin/python3"
fi

DESKTOP_FILE="$HOME/.local/share/applications/focuscombat.desktop"

echo "📝 Escribiendo lanzador en: $DESKTOP_FILE"

# --- CAMBIO CLAVE AQUÍ ---
# 1. Terminal=true para ver errores.
# 2. En Exec, usamos 'bash -c' para ejecutar el juego y luego 'read' para pausar
#    y que puedas leer el error antes de que se cierre.
cat > "$DESKTOP_FILE" <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Focus Combat
Comment=Entrenador Visual
Exec=bash -c '"$PYTHON_EXEC" "$DIR/main.py"; echo "Presiona Enter para cerrar..."; read line'
Icon=utilities-terminal
Path=$DIR
Terminal=true
StartupNotify=true
Categories=Game;
EOF

chmod +x "$DESKTOP_FILE"

echo "✅ ¡Listo! Busca 'Focus Combat' en tu menú."
echo "   (Se abrirá una terminal para mostrarte errores si los hay)"