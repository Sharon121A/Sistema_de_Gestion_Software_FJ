"""
Configuración del sistema de logs.
Registra errores y eventos importantes.
"""

import logging

logging.basicConfig(
    filename="sistema.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
