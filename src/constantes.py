from src.modelos import Dia, Horario


DIA_BASE: Dia = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
]
MATRIZ_BASE = (
    list(DIA_BASE),
    list(DIA_BASE),
    list(DIA_BASE),
    list(DIA_BASE),
    list(DIA_BASE),
    list(DIA_BASE),
)
HORARIO_BASE: Horario = {
    "asignaturas_inscritas": [],
    "matriz": (
        list(DIA_BASE),
        list(DIA_BASE),
        list(DIA_BASE),
        list(DIA_BASE),
        list(DIA_BASE),
        list(DIA_BASE),
    ),
}

DIAS = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO"]
HORAS = [
    "07:00-07:45",
    "07:45-08:30",
    "08:30-09:15",
    "09:15-10:00",
    "10:00-10:45",
    "10:45-11:30",
    "11:30-12:15",
    "01:00-01:45",
    "01:45-02:30",
    "02:30-03:15",
    "03:15-04:00",
    "04:00-04:45",
    "04:45-05:30",
]
