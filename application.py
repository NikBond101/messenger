import tkinter
import socket
import logging
from threading import Thread
import queue

from sender import sending_job
from receiver import receiving_job
from interface import interface_job

if __name__ == "__main__":
    input_queue = queue.Queue()
    send_th = Thread(target=lambda: sending_job(input_queue), daemon=True)
    recv_th = Thread(target=receiving_job, daemon=True)
    interface_th = Thread(target=lambda: interface_job(input_queue))

    send_th.start()
    recv_th.start()
    interface_th.start()
