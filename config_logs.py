"""
Configuración del sistema de logs.
Registra errores y eventos importantes.
"""

import logging

logger = logging.getLogger("softwarefj")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.FileHandler("sistema.log", encoding="utf-8")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
