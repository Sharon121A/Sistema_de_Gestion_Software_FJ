"""
Clase Cliente con encapsulación y validaciones estrictas.
"""

from entidad_base import EntidadBase
from excepciones import DatosInvalidosError

class Cliente(EntidadBase):
    """
    Representa un cliente del sistema.
    """

    def __init__(self, id_cliente, nombre, email):
        # Identificador del cliente
        self.__id_cliente = id_cliente
        
        # Nombre del cliente
        self.__nombre = nombre
        
        # Correo electrónico
        self.__email = email
        
        # Validación inicial
        self.validar()

    def validar(self):
        """
        Valida los datos del cliente.
        """
        if not self.__nombre:
            raise DatosInvalidosError("El nombre del cliente no puede estar vacío")

        if "@" not in self.__email:
            raise DatosInvalidosError("Correo electrónico inválido")

    def __str__(self):
        return f"{self.__nombre} - {self.__email}"
