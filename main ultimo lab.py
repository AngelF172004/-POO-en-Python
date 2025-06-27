

if __name__ == "__main__":
    profesores  = crear_profesores()
    estudiantes = crear_estudiantes()
    personas    = profesores + estudiantes
    cursos      = crear_cursos(profesores, estudiantes)

    procesar_personas(personas)
    mostrar_detalles_cursos(cursos)
