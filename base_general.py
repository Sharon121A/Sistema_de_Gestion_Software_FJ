"""
Clase abstracta base para las entidades del sistema.
"""

from abc import ABC, abstractmethod

class EntidadBase(ABC):
    """
    Clase abstracta que obliga a implementar validaciones y representación.
    """

    @abstractmethod
    def validar(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
