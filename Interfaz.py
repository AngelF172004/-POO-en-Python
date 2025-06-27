
from abc import ABC, abstractmethod

class Pagable(ABC):
    @abstractmethod
    def calcular_pago(self) -> float:
        pass

class Calificable(ABC):
    @abstractmethod
    def calcular_promedio(self) -> float:
        pass

class PagoInvalidoException(Exception):
    pass

class PromedioInvalidoException(Exception):
    pass
