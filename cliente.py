"""
Clase Cliente con encapsulación y validaciones estrictas.
"""

import re
from base_general import EntidadBase
from manejo_excepciones import DatosInvalidosError
from config_logs import logger

class Cliente(EntidadBase):
    """
    Representa un cliente del sistema.
    """

    def __init__(self, id_cliente, nombre, email):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__email = email
        self.validar()
        logger.info(f"Cliente creado: {nombre} (ID: {id_cliente})")

    def validar(self):
        """
        Valida los datos del cliente.
        """
        if not isinstance(self.__id_cliente, int) or self.__id_cliente <= 0:
            raise DatosInvalidosError(f"El ID debe ser un entero positivo. Recibido: {self.__id_cliente}")

        if not self.__nombre or not isinstance(self.__nombre, str) or len(self.__nombre.strip()) < 2:
            raise DatosInvalidosError("El nombre del cliente no puede estar vacío y debe tener al menos 2 caracteres")

        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(patron, self.__email):
            raise DatosInvalidosError(f"Correo electrónico inválido: '{self.__email}'")

    def get_id(self):
        return self.__id_cliente

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def __str__(self):
        return f"Cliente(ID={self.__id_cliente}, Nombre={self.__nombre}, Email={self.__email})"

    def __repr__(self):
        return self.__str__()
