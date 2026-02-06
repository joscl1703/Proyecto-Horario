# Proyecto-Horario
Proyecto desarrollado en Python para la materia Lenguaje de Programación 1.

# 📅 Sistema de Gestión de Horarios Académicos (CLI)
**Cátedra:** Lenguajes de Programación I  
**Institución:** Universidad Nacional Experimental Politécnica de la Fuerza Armada (UNEFA)  
**Tecnología:** Python 3.x | Gestión de dependencias con Poetry

## 📌 Contexto del Proyecto
Este sistema fue desarrollado como parte de la formación académica en ingeniería. Es una aplicación de **Interfaz de Línea de Comandos (CLI)** que automatiza la organización y consulta de horarios, utilizando una arquitectura basada en módulos y persistencia de datos en formato JSON.

## 👥 Créditos y Colaboración
Este proyecto es el resultado del trabajo en equipo. He subido esta versión a mi perfil personal para documentar mis aportes técnicos y el crecimiento de mi portafolio como desarrollador.

* **Equipo de Desarrollo:**
    * Endy Espinoza.
    * Yeiderson Sequera.
    * Gregory Orozco.
    * Lenin Iguaran. 
* **Repositorio Original:** (https://github.com/pongf456)

## 👤 Mi Contribución Técnica 
En este desarrollo, fui el responsable de diseñar e implementar el **Módulo de Gestión de Estudiantes**, asegurando un flujo de datos eficiente y seguro. Mis aportes principales incluyen:

1. **Gestión de Inscripciones:** Programé la lógica que permite a los estudiantes inscribir materias, validando que la información se guarde correctamente en la base de datos JSON.
2. **Sistema de Eliminación de Materias:** Implementé la funcionalidad para dar de baja asignaturas, asegurando la integridad del archivo de datos tras cada modificación.
3. **Visualización de Horario Personalizado:** Desarrollé el algoritmo de consulta que filtra y muestra exclusivamente las materias vinculadas al perfil del estudiante en un formato legible por terminal.
4. **Validación de Datos:** Aseguré que el sistema gestione correctamente las entradas del usuario para evitar duplicidad de inscripciones o errores al intentar eliminar registros inexistentes.

## 🛠️ Requisitos e Instalación
El proyecto utiliza **Poetry** para garantizar que el entorno de ejecución sea idéntico en cualquier máquina.

```bash
# 1. Instalar dependencias
poetry install

# 2. Ejecutar el sistema
poetry run python main.py
