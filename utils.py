import os
import sys
import logging
import socket

from typing import Tuple


def create_socket(sock_address: Tuple[str, int], logger: logging.Logger) -> socket.socket:
    if os.path.exists(sock_address[0]):
        try:
            logger.info("Unlink socket")
            os.unlink(sock_address[0])
        except Exception as err:
            logger.exception("unlink error", err)
            raise
    try:
        logger.info("create socket at %s", sock_address)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(sock_address)
    except Exception as err:
        logger.error("bind error", err)

    return sock


def create_logger(
    name: str,
    level: str = "DEBUG",
    format: str = "[%(levelname)s](%(name)s) %(message)s"
) -> logging.Logger:
    formatter = logging.Formatter(format)
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)
    logger = logging.Logger(name)
    logger.setLevel(level.upper())
    logger.addHandler(console)

    return logger