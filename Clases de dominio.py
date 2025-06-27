
class Persona(ABC):
    def __init__(self, nombre: str, id: int):
        self._nombre = nombre
        self._id = id

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def id(self) -> int:
        return self._id

    def __str__(self) -> str:
        return f"[ID: {self._id}] {self._nombre}"

class ProfesorTiempoCompleto(Persona, Pagable):
    def __init__(self, nombre: str, id: int, salario_mensual: float):
        super().__init__(nombre, id)
        self.salario_mensual = salario_mensual

    def calcular_pago(self) -> float:
        if self.salario_mensual <= 0:
            raise PagoInvalidoException(f"Salario mensual debe ser mayor a 0 para {self.nombre}")
        return self.salario_mensual

class ProfesorPorHoras(Persona, Pagable):
    def __init__(self, nombre: str, id: int, horas_trabajadas: float, pago_por_hora: float):
        super().__init__(nombre, id)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_pago(self) -> float:
        pago = self.horas_trabajadas * self.pago_por_hora
        if pago <= 0:
            raise PagoInvalidoException(f"Pago por horas inválido para {self.nombre}")
        return pago

class Estudiante(Persona, Calificable):
    def __init__(self, nombre: str, id: int, calificaciones: list[float]):
        super().__init__(nombre, id)
        self.calificaciones = calificaciones

    def calcular_promedio(self) -> float:
        if not self.calificaciones:
            raise PromedioInvalidoException(f"No hay calificaciones para {self.nombre}")
        return sum(self.calificaciones) / len(self.calificaciones)

class Curso:
    def __init__(self, nombre_curso: str, profesor: Pagable):
        self.nombre_curso = nombre_curso
        self.profesor = profesor
        self.estudiantes: list[Estudiante] = []

    def add_estudiante(self, e: Estudiante):
        self.estudiantes.append(e)

    def __str__(self) -> str:
        return (f"Curso: {self.nombre_curso} | "
                f"Profesor: {self.profesor.nombre} | "
                f"Estudiantes: {len(self.estudiantes)}")
