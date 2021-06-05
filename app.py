import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from _collections import deque
from frames import Timer, Settings
from windows import set_dpi_awarness

set_dpi_awarness()


COLOR_PRIMARY = "#e3baab"
COLOR_SECONDARY = "#B0BFDF"
BACKUP_COLOR = "#89A3D0"
CORAL_TEXT = "#FF6666"
GREEN_TEXT = "#3D6C7D"
CHOCO_TEXT = "#8B7A80"
YELLOW_TEXT = "#F6A400"

class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Timer.TFrame", background=BACKUP_COLOR)
        style.configure("Background.TFrame", background=COLOR_SECONDARY)
        style.configure("TimerText.TLabel", background=BACKUP_COLOR, foreground=GREEN_TEXT, font="Courier 38")
        #generic
        style.configure("LightText.TLabel", background=COLOR_SECONDARY, foreground=CHOCO_TEXT, font="Courier 12")
        style.configure("PomodoroButton.TButton", background=COLOR_SECONDARY, foreground=GREEN_TEXT, font="Courier 10")
        style.configure("SpinC.TSpinbox", background=COLOR_SECONDARY, foreground=GREEN_TEXT, font="Courier 10")
        style.map("PomodoroButton.TButton", background=[("active", CHOCO_TEXT), ("disabled", BACKUP_COLOR)], foreground=[("active", GREEN_TEXT), ("disabled", CHOCO_TEXT)])

        self["background"] = COLOR_SECONDARY


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


        self.frames = dict()

        timer_frame = Timer(container, self, lambda:self.show_frame(Settings))
        timer_frame.grid(row=0, column=0, sticky="NSEW")
        settings_frame = Settings(container, self, lambda:self.show_frame(Timer))
        settings_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[Timer] = timer_frame
        self.frames[Settings] = settings_frame

        self.show_frame(Timer)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()



if __name__ == '__main__':

    root = PomodoroTimer()
    root.mainloop()