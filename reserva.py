"""
Clase Reserva que integra cliente y servicio.
"""

from manejo_excepciones import ReservaError, ServicioNoDisponibleError
from config_logs import logger

class Reserva:
    """
    Representa una reserva del sistema.
    """

    _contador = 0

    def __init__(self, cliente, servicio, horas):
        self.__cliente = cliente
        self.__servicio = servicio
        self.__horas = horas
        self.__estado = "PENDIENTE"
        Reserva._contador += 1
        self.__id = Reserva._contador
        self.validar()
        logger.info(f"Reserva {self.__id} creada para {cliente.get_nombre()}")

    def get_id(self):
        return self.__id

    def get_cliente(self):
        return self.__cliente

    def get_servicio(self):
        return self.__servicio

    def get_estado(self):
        return self.__estado

    def validar(self):
        """
        Valida los datos de la reserva.
        """
        if self.__cliente is None:
            raise ReservaError("La reserva requiere un cliente")
        if self.__servicio is None:
            raise ReservaError("La reserva requiere un servicio")
        if not isinstance(self.__horas, (int, float)) or self.__horas <= 0:
            raise ReservaError(f"Las horas de la reserva deben ser mayores a cero. Recibido: {self.__horas}")

    def confirmar(self):
        """
        Confirma la reserva verificando disponibilidad del servicio.
        """
        try:
            self.__servicio.verificar_disponibilidad()
            costo = self.__servicio.calcular_costo(self.__horas)
            self.__estado = "CONFIRMADA"
            logger.info(f"Reserva {self.__id} confirmada. Costo: ${costo:,.0f}")
            return costo
        except ServicioNoDisponibleError as e:
            raise ReservaError(f"No se puede confirmar la reserva: {e}") from e

    def cancelar(self):
        """
        Cancela la reserva.
        """
        if self.__estado == "CANCELADA":
            raise ReservaError("La reserva ya fue cancelada anteriormente")
        if self.__estado == "COMPLETADA":
            raise ReservaError("No se puede cancelar una reserva ya completada")
        self.__estado = "CANCELADA"
        logger.info(f"Reserva {self.__id} cancelada")

    def procesar(self):
        """
        Procesa la reserva confirmada y la marca como completada.
        """
        if self.__estado != "CONFIRMADA":
            raise ReservaError("Solo se pueden procesar reservas confirmadas")
        self.__estado = "COMPLETADA"
        logger.info(f"Reserva {self.__id} completada")

    def __str__(self):
        return (f"Reserva(ID={self.__id}, Cliente={self.__cliente.get_nombre()}, "
                f"Servicio={self.__servicio.get_nombre()}, Horas={self.__horas}, Estado={self.__estado})")
