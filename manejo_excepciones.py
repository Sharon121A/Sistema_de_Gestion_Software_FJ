"""
Archivo que contiene las excepciones personalizadas del sistema.
"""

class SistemaError(Exception):
    """Excepción base del sistema"""
    pass

class DatosInvalidosError(SistemaError):
    """Error por datos incorrectos"""
    pass

class ServicioNoDisponibleError(SistemaError):
    """Error cuando un servicio no está disponible"""
    pass

class ReservaError(SistemaError):
    """Error relacionado con reservas"""
    pass

class CalculoError(SistemaError):
    """Error en cálculos inconsistentes"""
    pass
