import sys

selected_module: str | None = None
while True:
    if selected_module and selected_module in sys.modules:
        del sys.modules[selected_module]

    result = input("""¿A qué modulo quieres acceder?
    1. Administrador
    2. Estudiante
    3. Profesor
    4. Salir
    :  """)
    if result == "1":
        selected_module = "src.administrador"
        __import__("src.administrador")
    if result == "2":
        selected_module = "src.estudiante"
        __import__("src.estudiante")
    if result == "3":
        selected_module = "src.profesor"
        __import__("src.profesor")
    if result == "4":
        break
