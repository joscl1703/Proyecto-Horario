from src import database
from src.constantes import DIAS, HORAS
from src.modelos import Profesor

loggued_profesor = False
profesor_actual: None | Profesor = None

while True:
    if not loggued_profesor:
        usuario = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")

        profesor = next(
            (
                p
                for p in database.profesores
                if p["nombre"] == usuario and p["apellido"] == apellido
            ),
            None,
        )

        if not profesor:
            print("Profesor no encontrado. Verifique sus datos.")
            break

        loggued_profesor = True
        profesor_actual = profesor
        print(
            f"Bienvenido profesor {profesor_actual['nombre']} {profesor_actual['apellido']}"
        )

    opcion = input(
        """¿Qué desea realizar?
    1. Perfil Academico
    2. Cerrar sesión
    :   """
    )

    if opcion == "2":
        print("Sesión cerrada.")
        break

    if opcion == "1" and profesor_actual:
        print("HORARIO DEL PROFESOR")
        matriz = zip(*profesor_actual["horario"]["matriz"])
        print("BLOQUE".ljust(15), end="")
        for dia in DIAS:
            print(dia.ljust(15), end="")
        print("")
        for i, item in enumerate(matriz):
            print(HORAS[i].ljust(15), end="")
            for bloque in item:
                print((bloque or "").ljust(15), end="")
            print("")

        asignaturas = profesor_actual["horario"]["asignaturas_inscritas"]
        if len(asignaturas) == 0:
            print("No tiene materias asignadas.")
        else:
            print("Materias asignadas:")
            for codigo in asignaturas:
                materia = next(
                    (m for m in database.materias if m["codigo"] == codigo), None
                )
                if materia:
                    print(f"{materia['codigo']} - {materia['nombre']}")
