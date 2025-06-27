
def procesar_personas(personas: list[Persona]):
    print("\n--- Información de Personas ---")
    for p in personas:
        if isinstance(p, Pagable):
            print(f"{p} → Pago: ${safe_calcular_pago(p):.2f}")
        if isinstance(p, Calificable):
            print(f"{p} → Promedio: {safe_calcular_promedio(p):.2f}")

def mostrar_detalles_cursos(cursos: list[Curso]):
    print("\n--- Detalles de Cursos ---")
    for c in cursos:
        print(c)
        print(f"  Pago profesor: ${safe_calcular_pago(c.profesor):.2f}")
        for e in c.estudiantes:
            print(f"    • {e.nombre}: Promedio = {safe_calcular_promedio(e):.2f}")
        print()
