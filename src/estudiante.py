from typing import cast
import src.database as db
from src.modelos import Estudiante
from src.constantes import HORARIO_BASE, DIAS, HORAS
import copy

print("\n" + "=" * 40)
print("   BIENVENIDO AL MÓDULO DE ESTUDIANTES")
print("=" * 40)
print("1. Iniciar Sesión")
print("2. Registrarse")
print("3. Volver")

opcion_entrada = input("Seleccione: ")

if opcion_entrada == "2":
    nom = input("Nombre: ")
    ape = input("Apellido: ")
    ced = input("Cedula: ")
    cor = input("Correo: ")
    cla = input("Contraseña: ")

    nuevo_estudiante: Estudiante = {
        "nombre": nom,
        "apellido": ape,
        "correo": cor,
        "contraseña": cla,
        "cedula": ced,
        "horario": copy.deepcopy(HORARIO_BASE),
    }
    db.estudiantes.append(nuevo_estudiante)
    print(f"\n Estudiante {nom} registrado con éxito.")

elif opcion_entrada == "1":
    correo_buscado = input("Correo: ")
    clave_buscada = input("Contraseña: ")

    estudiante_actual = None
    for est in db.estudiantes:
        if est["correo"] == correo_buscado and est["contraseña"] == clave_buscada:
            estudiante_actual = est
            break

    if estudiante_actual:
        mantener_sesion = True

        while mantener_sesion:
            print(f"\n--- SESIÓN: {estudiante_actual['nombre'].upper()} ---")
            print("1. Ver mi Horario")
            print("2. Inscribir Materia ")
            print("3. Retirar Materia")
            print("4. Descargar Comprobante Actualizado ")
            print("5. Cerrar Sesión")

            accion = input("Seleccione: ")

            if accion == "1":
                print("\n" + "=" * 80)
                print(
                    f"       HORARIO DE CLASES: {estudiante_actual['nombre'].upper()}"
                )
                print("=" * 80)

                cabecera = "HORA".ljust(15)
                for dia in DIAS:
                    cabecera += dia.ljust(12)
                print(cabecera)
                print("-" * 80)

                matriz = estudiante_actual["horario"]["matriz"]

                for i_hora in range(len(HORAS)):
                    fila = HORAS[i_hora].ljust(15)

                    for i_dia in range(len(DIAS)):
                        contenido = matriz[i_dia][i_hora]

                        if contenido is None:
                            fila += "---------".ljust(12)
                        else:
                            fila += contenido.ljust(12)

                    print(fila)

                print("-" * 80)
                input("\nPresiona Enter para volver al menú...")

            elif accion == "2":
                print("\n--- MATERIAS OFERTADAS POR COORDINACIÓN ---")
                if not db.materias:
                    print("[!] No hay materias registradas.")
                else:
                    for m in db.materias:
                        bloques_encontrados = []
                        matriz_admin = m.get("horario", [])

                        for i_d, dia_col in enumerate(matriz_admin):
                            for i_h, bloque in enumerate(dia_col):
                                if bloque == m["codigo"]:
                                    bloques_encontrados.append((i_d, i_h))

                        if bloques_encontrados:
                            d_primero, h_primero = bloques_encontrados[0]
                            print(
                                f"[{m['codigo']}] {m['nombre']} | {DIAS[d_primero]} | {len(bloques_encontrados)} bloque(s)"
                            )

                    cod = input("\nIngrese el código de la materia: ").strip()
                    mat_obj = next((m for m in db.materias if m["codigo"] == cod), None)

                    if mat_obj:
                        bloques_a_inscribir = []
                        for i_d, dia_col in enumerate(mat_obj["horario"]):
                            for i_h, bloque in enumerate(dia_col):
                                if bloque == mat_obj["codigo"]:
                                    bloques_a_inscribir.append((i_d, i_h))

                        hay_choque = False
                        for d, h in bloques_a_inscribir:
                            if estudiante_actual["horario"]["matriz"][d][h] is not None:
                                print(
                                    f"\n[!] ERROR: Choque en {DIAS[d]} {HORAS[h]} con {estudiante_actual['horario']['matriz'][d][h]}"
                                )
                                hay_choque = True
                                break

                        if not hay_choque:
                            for d, h in bloques_a_inscribir:
                                estudiante_actual["horario"]["matriz"][d][h] = mat_obj[
                                    "codigo"
                                ]
                            estudiante_actual["horario"][
                                "asignaturas_inscritas"
                            ].append(mat_obj["codigo"])
                            print(
                                f" {mat_obj['nombre']} - {mat_obj['codigo']} inscrita en todos sus bloques con éxito."
                            )
                    else:
                        print("[!] Código no válido.")

            elif accion == "3":
                print("\n--- RETIRAR MATERIA ---")
                materia_a_retirar = input(
                    "Escriba el código exacto de la materia a retirar: "
                ).strip()
                encontrada = False
                if (
                    materia_a_retirar
                    in estudiante_actual["horario"]["asignaturas_inscritas"]
                ):
                    encontrada = True
                    matriz = estudiante_actual["horario"]["matriz"]

                    for d in range(len(matriz)):
                        for h in range(len(matriz[d])):
                            if matriz[d][h] == materia_a_retirar:
                                matriz[d][h] = None
                    estudiante_actual["horario"]["asignaturas_inscritas"].remove(
                        materia_a_retirar
                    )

                if encontrada:
                    print(
                        f" La materia '{materia_a_retirar}' ha sido retirada de tu horario."
                    )
                else:
                    print("[!] No se encontró esa materia en tu horario actual.")

            elif accion == "4":
                nombre_archivo = f"Comprobante_{estudiante_actual['nombre']}.txt"

                with open(nombre_archivo, "w", encoding="utf-8") as f:
                    f.write(
                        "==========================================================\n"
                    )
                    f.write("              UNEFA - COMPROBANTE DE INSCRIPCIÓN\n")
                    f.write(
                        "==========================================================\n\n"
                    )
                    f.write(
                        f"ESTUDIANTE: {estudiante_actual['nombre'].upper()} {estudiante_actual['apellido'].upper()}\n"
                    )
                    f.write(f"CÉDULA: {estudiante_actual.get('cedula', 'N/A')}\n")
                    f.write("-" * 60 + "\n")

                    materias_inscritas = estudiante_actual["horario"][
                        "asignaturas_inscritas"
                    ]
                    matriz_p = estudiante_actual["horario"]["matriz"]

                    for mat_nom in materias_inscritas:
                        profe_asignado = "POR ASIGNAR" 
    
                        nm = next(
                        (x for x in db.materias if x["codigo"] == mat_nom), 
                         None
                        )
                        
                        if nm is not None and nm.get("profesor_asignado") is not None:
                            profe_asignado = nm["profesor_asignado"]
                        
                        print(f"Materia: {mat_nom} | Profesor: {profe_asignado}")
                        

                        for p in db.profesores:
                            if mat_nom in p["horario"]["asignaturas_inscritas"]:
                                profe_asignado = p["nombre"] + " " + p["apellido"]
                                break

                        f.write(
                        f"{mat_nom:<10} | {nm['nombre'] if nm else ''} | {profe_asignado:<10}\n"
                    )

                    f.write("-" * 60 + "\n\n")

                    f.write("RESUMEN DE HORARIO SEMANAL:\n")
                    cabecera = "HORA".ljust(12)
                    for d in DIAS:
                        cabecera += d.ljust(12)
                    f.write(cabecera + "\n" + "-" * 85 + "\n")

                    for i in range(len(HORAS)):
                        linea = HORAS[i].ljust(12)
                        for j in range(len(DIAS)):
                            contenido = (
                                cast(str, matriz_p[j][i])
                                if matriz_p[j][i]
                                else "---------"
                            )
                            linea += contenido.ljust(12)
                        f.write(linea + "\n")

                print(f"\n Comprobante generado: {nombre_archivo}")
                print("Se incluyó la relación Materia | Profesor en el encabezado.")

            elif accion == "5":
                mantener_sesion = False
    else:
        print("\n[!] Error: Credenciales incorrectas.")
