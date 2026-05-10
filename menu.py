"""
Archivo principal del sistema.
Ejecuta de forma secuencial todas las pruebas.
"""

from config_logs import logger
from manejo_excepciones import *
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva

def separador(titulo):
    print(f"\n{'='*60}")
    print(f"  {titulo}")
    print(f"{'='*60}")

def ejecutar_pruebas():
    print("=== INICIO DE PRUEBAS DEL SISTEMA ===")
    logger.info("Inicio de pruebas del sistema")

    cliente1 = None
    sala = None
    equipo = None
    asesor = None

    # ═══════════════════════════════════════════════════════
    # PRUEBA 1: Cliente válido
    # ═══════════════════════════════════════════════════════
    separador("PRUEBA 1: Cliente válido")
    try:
        cliente1 = Cliente(1, "Ana Pérez", "ana@email.com")
    except Exception as e:
        logger.error(f"Prueba 1 fallida: {e}")
        print(f"❌ Error: {e}")
    else:
        print(f"✅ Cliente válido creado: {cliente1}")
    finally:
        print("→ Finalizada validación de cliente")

    # ═══════════════════════════════════════════════════════
    # PRUEBA 2: Cliente inválido (nombre vacío)
    # ═══════════════════════════════════════════════════════
    separador("PRUEBA 2: Cliente inválido - nombre vacío")
    try:
        Cliente(2, "", "correo_invalido")
    except DatosInvalidosError as e:
        logger.error(f"Prueba 2: {e}")
        print(f"❌ Error controlado (DatosInvalidosError): {e}")
    else:
        print("→ Esto no debería aparecer")
    finally:
        print("→ Bloque finally ejecutado")

    # ═══════════════════════════════════════════════════════
    # PRUEBA 3: Cliente inválido (email mal formado)
    # ═══════════════════════════════════════════════════════
    separador("PRUEBA 3: Cliente inválido - email incorrecto")
    try:
        Cliente(3, "Luis Gómez", "sin_arroba")
    except DatosInvalidosError as e:
        logger.error(f"Prueba 3: {e}")
        print(f"❌ Error controlado: {e}")

    # ═══════════════════════════════════════════════════════
    # PRUEBA 4: Cliente inválido (ID negativo)
    # ═══════════════════════════════════════════════════════
    separador("PRUEBA 4: Cliente inválido - ID negativo")
    try:
        Cliente(-5, "María Ruiz", "maria@mail.com")
    except DatosInvalidosError as e:
        logger.error(f"Prueba 4: {e}")
        print(f"❌ Error controlado: {e}")

    # ═══════════════════════════════════════════════════════
    # PRUEBA 5: Creación de servicios válidos
    # ═══════════════════════════════════════════════════════
    separador("PRUEBA 5: Servicios válidos")
    try:
        sala = ReservaSala("Sala de Juntas", 100000, capacidad=12)
        equipo = AlquilerEquipo("Portátil", 50000, tipo_equipo="Computación")
        asesor = AsesoriaEspecializada("Asesoría TI", 120000, area="Cloud")
        print(f"✅ {sala}")
        print(f"✅ {equipo}")
        print(f"✅ {asesor}")
    except Exception as e:
        logger.error(f"Prueba 5: {e}")
        print(f"❌ Error: {e}")

    # ═══════════════════════════════════════════════════════
    # PRUEBA 6: Servicio inválido (costo negativo)
    # ═══════════════════════════════════════════════════════
    separador("PRUEBA 6: Servicio inválido - costo negativo")
    try:
        ReservaSala("Sala X", -5000)
    except DatosInvalidosError as e:
        logger.error(f"Prueba 6: {e}")
        print(f"❌ Error controlado: {e}")

    # ═══════════════════════════════════════════════════════
    # PRUEBA 7: Reserva válida y confirmación
    # ═══════════════════════════════════════════════════════
    separador("PRUEBA 7: Reserva válida y confirmada")
    try:
        if cliente1 and sala:
            r1 = Reserva(cliente1, sala, 2)
            print(f"📋 {r1}")
            costo = r1.confirmar()
            print(f"✅ Reserva confirmada. Costo total: ${costo:,.0f}")
            r1.procesar()
            print(f"✅ Reserva procesada. Estado: {r1.get_estado()}")
    except Exception as e:
        logger.error(f"Prueba 7: {e}")
        print(f"❌ Error: {e}")

    # ═══════════════════════════════════════════════════════
    # PRUEBA 8: Reserva inválida (horas negativas)
    # ═══════════════════════════════════════════════════════
    separador("PRUEBA 8: Reserva inválida - horas negativas")
    try:
        if cliente1 and equipo:
            Reserva(cliente1, equipo, -5)
    except ReservaError as e:
        logger.error(f"Prueba 8: {e}")
        print(f"❌ Error controlado: {e}")

    # ═══════════════════════════════════════════════════════
    # PRUEBA 9: Servicio no disponible (encadenamiento)
    # ═══════════════════════════════════════════════════════
    separador("PRUEBA 9: Servicio NO disponible")
    try:
        sala_no_disp = ReservaSala("Sala VIP", 200000, disponible=False)
        if cliente1:
            r2 = Reserva(cliente1, sala_no_disp, 1)
            r2.confirmar()
    except ReservaError as e:
        logger.error(f"Prueba 9 - Error encadenado: {e}")
        print(f"❌ Error encadenado (ReservaError ← ServicioNoDisponibleError): {e}")

    # ═══════════════════════════════════════════════════════
    # PRUEBA 10: Cálculo inconsistente (descuento inválido)
    # ═══════════════════════════════════════════════════════
    separador("PRUEBA 10: Cálculo inconsistente")
    try:
        if asesor:
            asesor.calcular_costo(5, descuento=1.5)
    except CalculoError as e:
        logger.error(f"Prueba 10: {e}")
        print(f"❌ Error controlado (CalculoError): {e}")

    # ═══════════════════════════════════════════════════════
    # PRUEBA 11: Cancelación de reserva
    # ═══════════════════════════════════════════════════════
    separador("PRUEBA 11: Cancelación de reserva")
    try:
        if cliente1 and equipo:
            r3 = Reserva(cliente1, equipo, 1)
            r3.confirmar()
            print(f"Estado antes: {r3.get_estado()}")
            r3.cancelar()
            print(f"✅ Reserva cancelada. Estado: {r3.get_estado()}")
    except Exception as e:
        logger.error(f"Prueba 11: {e}")
        print(f"❌ Error: {e}")

    # ═══════════════════════════════════════════════════════
    # PRUEBA 12: Cancelar reserva ya cancelada
    # ═══════════════════════════════════════════════════════
    separador("PRUEBA 12: Cancelar reserva ya cancelada")
    try:
        if 'r3' in dir() and r3.get_estado() == "CANCELADA":
            r3.cancelar()
    except ReservaError as e:
        logger.error(f"Prueba 12: {e}")
        print(f"❌ Error controlado: {e}")

    # ═══════════════════════════════════════════════════════
    # PRUEBA 13: Cliente adicional válido
    # ═══════════════════════════════════════════════════════
    separador("PRUEBA 13: Cliente adicional válido")
    try:
        c5 = Cliente(5, "Carlos Mendoza", "carlos.m@softwarefj.com")
        print(f"✅ {c5}")
    except Exception as e:
        logger.error(f"Prueba 13: {e}")
        print(f"❌ Error: {e}")

    print("\n=== FIN DE PRUEBAS – SISTEMA ESTABLE ===")
    logger.info("Fin de pruebas - Sistema estable")

if __name__ == "__main__":
    ejecutar_pruebas()
