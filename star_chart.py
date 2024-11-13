import math
import tkinter as tk
from tkinter import ttk

def draw_circle(expert,canvas, x0, y0, x1, y1, outline="black", fill="white", width=2):
    canvas.create_oval(x0, y0, x1, y1, outline=outline, fill=fill, width=width)

    Cx = (x0 + x1) / 2
    Cy = (y0 + y1) / 2
    radius = (x1 - x0) / 2
    print(len(expert))

    angle=0
    for i in range(len(expert)):
        angle+=expert[i]
        # print("Angle:",math.degrees(angle))
        x_end = Cx + radius * math.cos(angle)
        y_end = Cy + radius * math.sin(angle)
        canvas.create_line(Cx, Cy, x_end, y_end, fill="black", width=1)
def calculate_betas(weights, k):
    betas = [0] * len(weights)
    total_sum = 0
    for i in range(len(weights)):
        total_sum += float(weights[i][k])

    for j in range(len(betas)):
        betas[j] = (2 * math.pi * float(weights[j][k])) / total_sum
    return betas

def create_star_chart_tab(notebook,weights,score):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Зоряна карта")

    tab.columnconfigure(0, weight=1)
    tab.rowconfigure(0, weight=1)

    canvas = tk.Canvas(tab, width=500, height=500)
    canvas.grid(row=0, column=0, sticky="")
    avg_experts=[[0 for _ in range(len(weights))] for _ in range(len(weights[0]))]
    for i in range(len(weights)):
        print("\n")
        for j in range(len(weights[0])):
            print(weights[i][j])
    for i in range(len(avg_experts)):
        avg_experts[i]=calculate_betas(weights,i)
    draw_circle(avg_experts[0],canvas, 100, 100, 400, 400)


