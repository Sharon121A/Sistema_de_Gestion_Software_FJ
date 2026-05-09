"""
Clases relacionadas con los servicios del sistema.
"""

from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError

class Servicio(ABC):
    """
    Clase abstracta Servicio.
    """

    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base
        self.validar()

    def validar(self):
        """
        Valida los datos del servicio.
        """
        if self.costo_base <= 0:
            raise DatosInvalidosError("El costo del servicio debe ser positivo")

    @abstractmethod
    def calcular_costo(self, horas):
        pass


class ReservaSala(Servicio):
    """
    Servicio de reserva de salas.
    """

    def calcular_costo(self, horas):
        return self.costo_base * horas


class AlquilerEquipo(Servicio):
    """
    Servicio de alquiler de equipos.
    """

    def calcular_costo(self, horas, seguro=False):
        total = self.costo_base * horas
        if seguro:
            total += 50000
        return total


class AsesoriaEspecializada(Servicio):
    """
    Servicio de asesoría especializada.
    """

    def calcular_costo(self, horas, descuento=0):
        total = self.costo_base * horas
        return total - (total * descuento)
