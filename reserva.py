"""
Clase Reserva que integra cliente y servicio.
"""

from excepciones import ReservaError

class Reserva:
    """
    Representa una reserva del sistema.
    """

    def __init__(self, cliente, servicio, horas):
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "PENDIENTE"
        self.validar()

    def validar(self):
        """
        Valida los datos de la reserva.
        """
        if self.horas <= 0:
            raise ReservaError("Las horas de la reserva deben ser mayores a cero")

    def confirmar(self):
        """
        Confirma la reserva.
        """
        self.estado = "CONFIRMADA"

    def cancelar(self):
        """
        Cancela la reserva.
        """
        self.estado = "CANCELADA"
