"""
Archivo principal del sistema.
Ejecuta de forma secuencial todas las pruebas.
"""

import logging
import logger

from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva

def ejecutar_pruebas():
    print("=== INICIO DE PRUEBAS DEL SISTEMA ===")

    # PRUEBA 1: Cliente válido
    try:
        cliente1 = Cliente(1, "Ana Pérez", "ana@email.com")
        print("Cliente válido creado")
    except Exception as e:
        logging.error(e)

    # PRUEBA 2: Cliente inválido
    try:
        Cliente(2, "", "correo_invalido")
    except Exception as e:
        logging.error(e)
        print("Error controlado en cliente inválido")

    # PRUEBA 3: Creación de servicios
    try:
        sala = ReservaSala("Sala de Juntas", 100000)
        equipo = AlquilerEquipo("Portátil", 50000)
        asesor = AsesoriaEspecializada("Asesoría TI", 120000)
        print("Servicios creados correctamente")
    except Exception as e:
        logging.error(e)

    # PRUEBA 4: Reserva válida
    try:
        reserva1 = Reserva(cliente1, sala, 2)
        reserva1.confirmar()
        print("Reserva confirmada")
    except Exception as e:
        logging.error(e)

    # PRUEBA 5: Reserva inválida
    try:
        Reserva(cliente1, asesor, -5)
    except Exception as e:
        logging.error(e)
        print("Error controlado en reserva inválida")

    print("=== FIN DE PRUEBAS – SISTEMA ESTABLE ===")

if __name__ == "__main__":
    ejecutar_pruebas()
