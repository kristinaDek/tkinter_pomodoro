import tkinter as tk
from tkinter import ttk

CHOCO_TEXT = "#8B7A80"


class Settings(ttk.Frame):
    def __init__(self, container, controller, show_timer, **kwargs):
        super().__init__(container, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        self["style"] = "Background.TFrame"

        settings_container = ttk.Frame(self, padding="30 15 30 15", style="Background.TFrame")
        settings_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)
        settings_container.columnconfigure(0, weight=1)
        settings_container.rowconfigure(1, weight=1)

        pomodoro_label = ttk.Label(settings_container, text="Pomodoro:", style="LightText.TLabel")
        pomodoro_label.grid(row=0, column=0, sticky="W")
        pomodoro_spin = tk.Spinbox(settings_container, from_=0, to=120, increment=1, justify= "center", textvariable=controller.pomodoro, width=10, font="Courier 10", foreground=CHOCO_TEXT)
        pomodoro_spin.grid(row=0, column=1, sticky="EW")
        pomodoro_spin.focus()

        long_break_label = ttk.Label(settings_container, text="Long break:", style="LightText.TLabel")
        long_break_label.grid(row=1, column=0, sticky="W")
        long_break_spin = tk.Spinbox(settings_container, from_=0, to=60, increment=1, justify= "center", textvariable=controller.long_break, width=10, font="Courier 10", foreground=CHOCO_TEXT)
        long_break_spin.grid(row=1, column=1, sticky="EW")
        long_break_spin.focus()

        short_break_label = ttk.Label(settings_container, text="Short break:", style="LightText.TLabel")
        short_break_label.grid(row=2, column=0, sticky="W")
        short_break_spin = tk.Spinbox(settings_container, from_=0, to=30, increment=1, justify="center", textvariable=controller.short_break, width=10, font="Courier 10", foreground=CHOCO_TEXT)
        short_break_spin.grid(row=2, column=1, sticky="EW")
        short_break_spin.focus()

        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        button_container = ttk.Frame(self, style="Timer.TFrame")
        button_container.grid(sticky="EW", padx=10)
        button_container.columnconfigure(0, weight=1)
        self.timer_button = ttk.Button(
            button_container,
            text="Back",
            command=show_timer,
            style = "PomodoroButton.TButton",
            cursor="hand2"
        )
        self.timer_button.grid(row=0, column=0, sticky="EW", padx=2)