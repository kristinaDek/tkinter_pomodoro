import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from _collections import deque

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Pomodoro timer!")
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




class Timer(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.controller = controller
        pomodoro_time = int(controller.pomodoro.get())
        self.current_time = tk.StringVar(value=f"{pomodoro_time:02d}:00")

        self.timer_running = False
        self._timer_decrement_job = None
        self.current_timer_label = tk.StringVar(value=controller.timer_schedule[0])

        timer_lab = ttk.Frame(self, height="50")
        timer_lab.grid(row=0, column=0, pady=(10, 0), sticky="NSEW")
        timer_description = ttk.Label(timer_lab, textvariable=self.current_timer_label)

        timer_description.place(relx=0.5, rely=0.5, anchor="center")

        timer_fr = ttk.Frame(self, height="100")
        timer_fr.grid(row= 1, column= 0, pady=(10,0), sticky="NSEW")

        timer_counter = ttk.Label(
            timer_fr,
            textvariable=self.current_time
        )

        timer_counter.place(relx=0.5, rely=0.5, anchor="center")

        button_container = ttk.Frame(self, padding=10)
        button_container.grid(row=2, column=0)
        button_container.columnconfigure((0, 1, 2), weight=1)

        self.start_button = ttk.Button(
            button_container,
            text="Start",
            command=self.start_timer,
            cursor="hand2"
        )
        self.start_button.grid(row=0,column=0, sticky="EW")

        self.stop_button = ttk.Button(
            button_container,
            text="Stop",
            state="disabled",
            command=self.stop_timer,
            cursor="hand2"
        )
        self.stop_button.grid(row=0, column=1, sticky="EW", padx=5)

        self.reset_button = ttk.Button(
            button_container,
            text="Reset",
            state="disabled",
            command=self.reset_timer,
            cursor="hand2"
        )
        self.reset_button.grid(row=0, column=2, sticky="EW")


    def start_timer(self):
        self.timer_running = True
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "enabled"
        self.reset_button["state"] = "enabled"
        self.decrement_time()

    def reset_timer(self):
        self.stop_timer()
        pomodoro_time = int(self.controller.pomodoro.get())
        self.controller.timer_schedule = deque(self.controller.timer_order)
        self.current_time.set(f"{pomodoro_time:02d}:00")
        self.current_timer_label.set(self.controller.timer_schedule[0])



    def stop_timer(self):
        self.timer_running = False
        self.stop_button["state"] = "disabled"
        self.start_button["state"] = "enabled"
        self.reset_button["state"] = "enabled"

        if  self._timer_decrement_job:
            self.after_cancel(self._timer_decrement_job)
            self._timer_decrement_job = None


    def decrement_time(self):
        current_time = self.current_time.get()

        if self.timer_running and current_time != "00:00":
            min, sec= current_time.split(":")

            if int(sec) > 0:
                sec = int(sec) - 1
                min = int(min)
            else:
                sec = 59
                min = int(min) - 1

            self.current_time.set(f"{min:02d}:{sec:02d}")
            self._timer_decrement_job = self.after(1000, self.decrement_time)

        elif self.timer_running and current_time == "00:00":
            self.controller.timer_schedule.rotate(-1)
            next_up = self.controller.timer_schedule[0]
            self.current_timer_label.set(next_up)

            if next_up == "Pomodoro":
                pomodoro_time = int(self.controller.pomodoro.get())
                self.current_time.set(f"{pomodoro_time:02d}:00")
            elif next_up == "Short break":
                short_break_time = int(self.controller.short_break.get())
                self.current_time.set(f"{short_break_time:02d}:00")
            elif next_up == "Long break":
                long_break_time = int(self.controller.long_break.get())
                self.current_time.set(f"{long_break_time:02d}:00")
            self._timer_decrement_job = self.after(1000, self.decrement_time)



if __name__ == '__main__':

    root = PomodoroTimer()
    root.mainloop()