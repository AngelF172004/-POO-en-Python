# Fragmento 3: Funciones de Creación de Objetos

def crear_profesores() -> list[Pagable]:
    return [
        ProfesorTiempoCompleto("Ana Gómez", 101, 25000),
        ProfesorPorHoras("Luis Pérez", 102, 80, 200)
    ]

def crear_estudiantes() -> list[Estudiante]:
    return [
        Estudiante("Juan Martínez", 201, [8.5, 7.0, 9.0]),
        Estudiante("María Ruiz",   202, [9.5, 8.0]),
        Estudiante("Carlos López", 203, [])  # probar excepción en promedio
    ]

def crear_cursos(profesores: list[Pagable],
                 estudiantes: list[Estudiante]) -> list[Curso]:
    prof1, prof2 = profesores
    est1, est2, est3 = estudiantes

    curso_java = Curso("Programación en Java", prof1)
    curso_java.add_estudiante(est1)
    curso_java.add_estudiante(est2)

    curso_bd = Curso("Bases de Datos", prof2)
    curso_bd.add_estudiante(est2)
    curso_bd.add_estudiante(est3)

    return [curso_java, curso_bd]
