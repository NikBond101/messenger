import socket
import logging
import time
import os
import sys
import queue

from utils import create_socket, create_logger


def sending_job(
    input_queue: queue.Queue,
    udp_addr: str = "127.0.0.5",
    udp_port: int = 5001,
) -> None:
    logger = create_logger("send")
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    destination = (udp_addr, udp_port)

    while True:
        message = input_queue.get()
        udp_socket.sendto(message.encode(), destination)

        # time.sleep(5)


if __name__ == "__main__":
    pass
