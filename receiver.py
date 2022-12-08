import socket
import logging
import time
import os
import sys
import json

from utils import create_socket, create_logger


def receiving_job(
    udp_addr: str = "127.0.0.5",
    udp_port: int = 5001,
    buffer_size: int = 4096,
) -> None:
    destination = (udp_addr, udp_port)
    logger = create_logger("recv")
    udp_socket = create_socket(destination, logger)
    buffer = bytearray(buffer_size)

    while True:
        received = udp_socket.recv_into(buffer, buffer_size)
        print(str(buffer[:received], 'utf-8'))


if __name__ == "__main__":
    pass
