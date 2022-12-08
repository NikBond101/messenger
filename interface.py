import tkinter
import queue


def set_message(event, entry: tkinter.Entry, input_queue: queue.Queue):
    input_queue.put(entry.get())


def interface_job(input_queue: queue.Queue) -> None:
    app = tkinter.Tk()
    app.title("Messanger")
    app.minsize(600, 400)
    app.resizable(False, False)

    input_var = tkinter.StringVar(app, "")

    input_entry = tkinter.Entry(app, textvariable=input_var)
    input_button = tkinter.Button(app, text="input")

    input_entry.pack()
    input_button.pack()

    input_button.bind(
        "<Button-1>", lambda event: set_message(event, input_entry, input_queue)
    )

    app.mainloop()
