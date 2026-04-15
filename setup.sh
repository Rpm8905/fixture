#!/bin/bash

# 1. Crear el entorno virtual
python3 -m venv venv

# 2. Activar el entorno virtual
source venv/bin/activate

# 3. Instalar Flask
pip install flask

echo "¡Listo! Flask instalado en el venv."