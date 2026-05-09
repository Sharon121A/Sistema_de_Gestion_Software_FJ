"""
Clase abstracta base para las entidades del sistema.
"""

from abc import ABC, abstractmethod

class EntidadBase(ABC):
    """
    Clase abstracta que obliga a implementar validaciones.
    """

    @abstractmethod
    def validar(self):
        pass
