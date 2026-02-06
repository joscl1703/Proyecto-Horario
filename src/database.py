from src.modelos import Estudiante, Materia, Profesor
import json
import atexit

DATA_BASE_NAME = "./database.json"
estudiantes: list[Estudiante] = []
profesores: list[Profesor] = []
materias: list[Materia] = []
try:
    with open(DATA_BASE_NAME, "rb") as file:
        data = json.load(file)
        profesores = data["profesores"]
        estudiantes = data["estudiantes"]
        materias = data["materias"]
except FileNotFoundError:
    pass

atexit.register(
    lambda: json.dump(
        {"profesores": profesores, "estudiantes": estudiantes, "materias": materias},
        open(DATA_BASE_NAME, "w"),
        indent=4,
    )
)
