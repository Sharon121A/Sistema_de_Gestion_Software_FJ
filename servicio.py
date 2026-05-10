"""
Clases relacionadas con los servicios del sistema.
"""

from abc import ABC, abstractmethod
from manejo_excepciones import DatosInvalidosError, ServicioNoDisponibleError, CalculoError
from config_logs import logger

class Servicio(ABC):
    """
    Clase abstracta Servicio.
    """

    def __init__(self, nombre, costo_base, disponible=True):
        self.__nombre = nombre
        self.__costo_base = costo_base
        self.__disponible = disponible
        self.validar()

    def get_nombre(self):
        return self.__nombre

    def get_costo_base(self):
        return self.__costo_base

    def is_disponible(self):
        return self.__disponible

    def set_disponible(self, valor):
        self.__disponible = valor

    def validar(self):
        """
        Valida los datos del servicio.
        """
        if not self.__nombre or not isinstance(self.__nombre, str):
            raise DatosInvalidosError("El nombre del servicio no puede estar vacío")
        if not isinstance(self.__costo_base, (int, float)) or self.__costo_base <= 0:
            raise DatosInvalidosError(f"El costo del servicio debe ser numérico y positivo. Recibido: {self.__costo_base}")

    def verificar_disponibilidad(self):
        """Verifica si el servicio está disponible."""
        if not self.__disponible:
            raise ServicioNoDisponibleError(f"El servicio '{self.__nombre}' no está disponible actualmente")

    @abstractmethod
    def calcular_costo(self, horas, **kwargs):
        pass

    @abstractmethod
    def describir(self):
        pass

    def __str__(self):
        estado = "DISPONIBLE" if self.__disponible else "NO DISPONIBLE"
        return f"{self.__nombre} (${self.__costo_base}) - {estado}"


class ReservaSala(Servicio):
    """
    Servicio de reserva de salas.
    """

    def __init__(self, nombre, costo_base, capacidad=10, disponible=True):
        self.__capacidad = capacidad
        super().__init__(nombre, costo_base, disponible)

    def calcular_costo(self, horas, impuesto=0.19, descuento=0, **kwargs):
        if horas <= 0:
            raise CalculoError("Las horas deben ser mayores a cero")
        subtotal = self.get_costo_base() * horas
        total = subtotal + (subtotal * impuesto) - (subtotal * descuento)
        return total

    def describir(self):
        return f"Sala de reuniones: {self.get_nombre()}, capacidad {self.__capacidad} personas"


class AlquilerEquipo(Servicio):
    """
    Servicio de alquiler de equipos.
    """

    def __init__(self, nombre, costo_base, tipo_equipo="General", disponible=True):
        self.__tipo_equipo = tipo_equipo
        super().__init__(nombre, costo_base, disponible)

    def calcular_costo(self, horas, seguro=False, mantenimiento=False, impuesto=0.19, **kwargs):
        if horas <= 0:
            raise CalculoError("Las horas deben ser mayores a cero")
        total = self.get_costo_base() * horas
        if seguro:
            total += 50000
        if mantenimiento:
            total += 25000
        return total + (total * impuesto)

    def describir(self):
        return f"Equipo: {self.get_nombre()}, tipo {self.__tipo_equipo}"


class AsesoriaEspecializada(Servicio):
    """
    Servicio de asesoría especializada.
    """

    def __init__(self, nombre, costo_base, area="General", disponible=True):
        self.__area = area
        super().__init__(nombre, costo_base, disponible)

    def calcular_costo(self, horas, descuento=0, recargo_urgencia=0, impuesto=0.19, **kwargs):
        if horas <= 0:
            raise CalculoError("Las horas deben ser mayores a cero")
        if not (0 <= descuento <= 1):
            raise CalculoError("El descuento debe estar entre 0 y 1")
        if not (0 <= recargo_urgencia <= 1):
            raise CalculoError("El recargo de urgencia debe estar entre 0 y 1")
        total = self.get_costo_base() * horas
        total -= total * descuento
        total += total * recargo_urgencia
        return total + (total * impuesto)

    def describir(self):
        return f"Asesoría especializada en {self.__area}: {self.get_nombre()}"
