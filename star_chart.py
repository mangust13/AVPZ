import math
import tkinter as tk
from tkinter import ttk

def draw_circle(canvas, x0, y0, x1, y1, outline="black", fill="white", width=2):
    canvas.create_oval(x0, y0, x1, y1, outline=outline, fill=fill, width=width)

    Cx = (x0 + x1) / 2
    Cy = (y0 + y1) / 2
    radius = (x1 - x0) / 2

    angle_step = 30

    for i in range(12):
        angle_rad = math.radians(i * angle_step)

        x_end = Cx + radius * math.cos(angle_rad)
        y_end = Cy + radius * math.sin(angle_rad)
        canvas.create_line(Cx, Cy, x_end, y_end, fill="black", width=1)

def create_star_chart_tab(notebook):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Зоряна карта")

    tab.columnconfigure(0, weight=1)
    tab.rowconfigure(0, weight=1)

    canvas = tk.Canvas(tab, width=500, height=500)
    canvas.grid(row=0, column=0, sticky="")

    draw_circle(canvas, 100, 100, 400, 400)
