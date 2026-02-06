from src import database
from src.constantes import DIAS, HORARIO_BASE, HORAS, MATRIZ_BASE
from src.modelos import Materia, Profesor
import copy
import readchar

loggued = False
while True:
    if not loggued:
        usuario = input("Ingresa el usuario: ")
        contraseña = input("ingresa la contraseña: ")
        if usuario != "admin" or contraseña != "admin":
            print("Datos de acceso inválidos.")
            break
        loggued = True
    opcion = input("""Bienvenido coordinador ¿Qué desea realizar? 
    1. Administrar los profesores
    2. Administrar las materias
    3. Salir
    :   """)
    if opcion == "3":
        break
    if opcion == "1":
        opcion = input("""¿Qué desea hacer?
        1. Obtener profesores
        2. Agregar profesor
        3. Eliminar profesor
        :   """)
        if opcion == "1":
            if len(database.profesores) == 0:
                print("No hay profesores disponibles.")
            else:
                for i, profesor in enumerate(database.profesores):
                    print(f"ID:{i} {profesor['nombre']} {profesor['apellido']}")
        if opcion == "2":
            nombre = input("Ingrese el nombre del profesor: ")
            apellido = input("ingrese el apellido del profesor: ")
            nuevo_profesor: Profesor = {
                "nombre": nombre,
                "apellido": apellido,
                "horario": copy.deepcopy(HORARIO_BASE),
            }
            database.profesores.append(nuevo_profesor)
            print("Profesor agregado.")
        if opcion == "3":
            id = input("Indique la ID del profesor a eliminar: ")
            try:
                id = int(id)
                database.profesores.pop(id)
                print("Profesor eliminado.")
            except ValueError:
                print("Valor inválido.")
            except IndexError:
                print("ID no existente.")
        opcion = None
    if opcion == "2":
        opcion = input("""¿Qué desea hacer?
        1. Obtener materias
        2. Agregar materia
        3. Eliminar materia
        4. Mostrar horario de la materia
        5. Asignar profesor a la materia
        :   """)
        if opcion == "1":
            if len(database.materias) == 0:
                print("No hay materias disponibles.")
            else:
                for i, materia in enumerate(database.materias):
                    print(f"ID: {i} {materia['codigo']} {materia['nombre']}")
        if opcion == "2":
            try:
                nombre = input("Ingresa el nombre de la materia: ")
                codigo = input("Ingresa el código de la materia: ")
                nuevo_horario = copy.deepcopy(MATRIZ_BASE)
                print("""A continuación se presentará el formulario para el horario de la materia. Presione:
                (s) para saltar el dia o el bloque de hora
                (Enter) para editar el día o agregar el bloque de hora""")
                for index_dia, dia in enumerate(nuevo_horario):
                    print(f"Día {DIAS[index_dia]}: ", end="", flush=True)
                    key = readchar.readkey()
                    if key == "s":
                        print("Saltado")
                    elif key == readchar.key.ENTER:
                        print("")
                        for index_bloque in range(len(dia)):
                            print(f"Bloque {HORAS[index_bloque]}: ", end="", flush=True)
                            key = readchar.readkey()
                            if key == "s":
                                print("Saltado")
                            elif key == readchar.key.ENTER:
                                nuevo_horario[index_dia][index_bloque] = codigo
                                print("agregado")

                            else:
                                raise Exception("Tecla inválida.")
                    else:
                        raise Exception("Tecla inválida.")
                nueva_materia: Materia = {
                    "nombre": nombre,
                    "codigo": codigo,
                    "horario": nuevo_horario,
                    "profesor_asignado": None,
                }
                database.materias.append(nueva_materia)
                print("Materia agregada con exito.")
            except Exception:
                print("Proceso abortado.")
        if opcion == "3":
            id = input("Ingrese el ID de la materia a eliminar: ")
            try:
                id = int(id)
                materia = database.materias.pop(id)
                profesor_asignado = next(
                    (
                        x
                        for x in database.profesores
                        if x["nombre"] == materia["profesor_asignado"]
                    ),
                    None,
                )
                if profesor_asignado:
                    for dia in profesor_asignado["horario"]["matriz"]:
                        for i_bloque, bloque_valor in enumerate(dia):
                            if bloque_valor == materia["codigo"]:
                                dia[i_bloque] = None
                    profesor_asignado["horario"]["asignaturas_inscritas"].remove(
                        materia["codigo"]
                    )
                print("Materia eliminada con exito.")
            except ValueError:
                print("Valor inválido.")
            except IndexError:
                print("ID no existente.")
        if opcion == "4":
            id = input("Ingrese el ID de la materia: ")
            try:
                id = int(id)
                horario = database.materias[id]
                matriz = zip(*horario["horario"])
                print("BLOQUE".ljust(15), end="")
                for dia in DIAS:
                    print(dia.ljust(15), end="")
                print("")
                for i, item in enumerate(matriz):
                    print(HORAS[i].ljust(15), end="")
                    for bloque in item:
                        print((bloque or "").ljust(15), end="")
                    print("")
            except ValueError:
                print("Valor de ID inválido.")
            except IndexError:
                print("El valor de ID no existe.")
        if opcion == "5":
            id = input("ingrese el ID de la materia: ")
            try:
                id = int(id)
                materia = database.materias[id]
                if materia["profesor_asignado"]:
                    print(
                        f"La materia ya tiene un profesor asignado: {materia['profesor_asignado']}"
                    )
                    break
                id_profesor = input("Ingrese el ID del profesor: ")
                id_profesor = int(id_profesor)
                profesor = database.profesores[id_profesor]
                for i_dia_materia, dia_materia in enumerate(materia["horario"]):
                    for i_bloque_materia, bloque_materia in enumerate(dia_materia):
                        if (
                            bloque_materia
                            and profesor["horario"]["matriz"][i_dia_materia][
                                i_bloque_materia
                            ]
                        ):
                            raise Exception(
                                "El horario actual del profesor choca con la materia a asignar."
                            )
                for i_dia_materia, dia_materia in enumerate(materia["horario"]):
                    for i_bloque_materia, bloque_materia in enumerate(dia_materia):
                        profesor["horario"]["matriz"][i_dia_materia][
                            i_bloque_materia
                        ] = bloque_materia
                profesor["horario"]["asignaturas_inscritas"].append(materia["codigo"])
                materia["profesor_asignado"] = (
                    profesor["nombre"] + " " + profesor["apellido"]
                )
                print("Materia asignada exitosamente.")
            except ValueError:
                print("Valor de ID inválido.")
            except IndexError:
                print("Materia o profesor inexistente.")
            except Exception as e:
                print(*e.args)
