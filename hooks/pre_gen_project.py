import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith("."):
    print(f"{ERROR_COLOR}ERROR: {project_slug=} no es un nombre válido para esta plantilla.{RESET_ALL}")
    sys.exit(1)

print(f"{MESSAGE_COLOR}Esta listo, tu proyecto ha sido creado exitosamente!{RESET_ALL}")
print(f"Creando proyecto en { os.getcwd() }{RESET_ALL}")

# Colores aqui: https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html