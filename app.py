import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from _collections import deque
from frames import Timer

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Good luck!")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.pomodoro = tk.StringVar(value=25)
        self.short_break = tk.StringVar(value=5)
        self.long_break = tk.StringVar(value=15)
        self.timer_order = ["Pomodoro", "Short break", "Pomodoro", "Short break", "Pomodoro", "Long break"]
        self.timer_schedule = deque(self.timer_order)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        timer_frame = Timer(container, self)
        timer_frame.grid(row=0, column=0, sticky="NSEW")

if __name__ == '__main__':

    root = PomodoroTimer()
    root.mainloop()