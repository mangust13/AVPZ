import tkinter as tk
from tkinter import ttk
from star_chart import create_star_chart_tab
from criteria_table import create_criteria_tab

root = tk.Tk()
root.title("Аналіз специфікації вимог та управління ризиками")
root.state("zoomed")

def create_notebook():
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)
    return notebook

notebook = create_notebook()

create_criteria_tab(notebook)
create_star_chart_tab(notebook)

root.mainloop()
