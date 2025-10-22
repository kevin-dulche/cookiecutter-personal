import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Casi listo!")
print(f"Creando el repositorio...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}Ya está todo listo! Crea y diviértete!{RESET_ALL}")

# Colores aqui: https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html