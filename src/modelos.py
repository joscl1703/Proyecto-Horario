from typing import Annotated, List, Tuple, TypeAlias, TypedDict

BloqueHora: TypeAlias = str | None
Dia: TypeAlias = Annotated[List[BloqueHora], 13]


class Horario(TypedDict):
    asignaturas_inscritas: list[str]
    matriz: Tuple[Dia, Dia, Dia, Dia, Dia, Dia]


class Estudiante(TypedDict):
    nombre: str
    cedula:str
    apellido: str
    correo: str
    contraseña: str
    horario: Horario


class Profesor(TypedDict):
    nombre: str
    apellido: str
    horario: Horario


class Materia(TypedDict):
    codigo: str
    nombre: str
    profesor_asignado: str | None
    horario: Tuple[Dia, Dia, Dia, Dia, Dia, Dia]
