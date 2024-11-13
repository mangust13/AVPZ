import tkinter as tk
from tkinter import ttk


def create_criteria_tab(notebook):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Критерії оцінювання")

    headers = [
        "№ з/п", "Критерії оцінювання якості ПЗ",
        "Експерти:", "", "", "",
        "Середнє значення вагових коефіцієнтів"
    ]

    sub_headers = [
        "", "", "галузі застосування", "зручності використання",
        "з програмування", "узагальнені користувачі", ""
    ]

    criteria_labels = [
        ["1", "Точність управління та обчислень"],
        ["2", "Ступінь стандартності інтерфейсів"],
        ["3", "Функціональна повнота можливостей ПЗ"],
        ["4", "Стійкість до помилок користувача"],
        ["5", "Можливість розширення функцій"],
        ["6", "Зручність виконання завдань"],
        ["7", "Простота в обслуговуванні ПЗ"],
        ["8", "Відповідність чинним стандартам"],
        ["9", "Переносність між програмно-апаратного забезпечення"],
        ["10", "Зручність навчання користувачу"],
        ["", "Загальна/середня кількість балів"]
    ]

    weights = [
        ["8", "5", "9", "7"],
        ["5", "9", "6", "5"],
        ["10", "6", "9", "6"],
        ["6", "5", "10", "7"],
        ["5", "5", "10", "4"],
        ["9", "7", "7", "7"],
        ["8", "7", "10", "7"],
        ["6", "5", "10", "5"],
        ["8", "6", "7", "7"],
        ["7", "8", "10", "10"],
    ]

    score = [
        ["10", "9", "10", "8.05"],
        ["9", "8", "8", "7.50"],
        ["9", "7", "9", "6.10"],
        ["6", "5", "8", "7.70"],
        ["7", "5", "8", "6.05"],
        ["9", "9", "10", "7.85"],
        ["10", "9", "7", "6.75"],
        ["6", "8", "7", "5.55"],
        ["9", "7", "6", "7.85"],
        ["6", "9", "4", "4.30"],
    ]

    entry_fields = []
    result_labels = []
    average_labels = []

    def update_totals():
        totals = []
        averages = []

        for col in range(4):
            column_values_before = [int(entry_fields[row][col][0].get()) for row in range(10)]
            column_values_after = [float(entry_fields[row][col][1].get()) for row in range(10)]

            total_before = sum(column_values_before)
            average_after = round(sum(column_values_after) / len(column_values_after), 2)

            totals.append(total_before)
            averages.append(average_after)

            result_labels[col][0].config(text=str(total_before))
            result_labels[col][1].config(text=str(average_after))

        for row in range(10):
            row_values_before = [int(entry_fields[row][col][0].get()) for col in range(4)]
            row_average_before = round(sum(row_values_before) / len(row_values_before), 2)
            average_labels[row].config(text=str(row_average_before))

    for col, header in enumerate(headers):
        if col == 2:
            label = ttk.Label(tab, text=headers[2], font=("Arial", 10, "bold"), anchor="center", borderwidth=1,
                              relief="solid")
            label.grid(row=0, column=2, columnspan=4, padx=1, pady=1, sticky="nsew")
        elif col == 0:
            label = ttk.Label(tab, text=headers[0], font=("Arial", 10, "bold"), anchor="center", borderwidth=1,
                              relief="solid")
            label.grid(row=0, column=0, rowspan=2, padx=1, pady=1, sticky="nsew")
        elif col == 1:
            label = ttk.Label(tab, text=headers[1], font=("Arial", 10, "bold"), anchor="center", borderwidth=1,
                              relief="solid")
            label.grid(row=0, column=1, rowspan=2, padx=1, pady=1, sticky="nsew")
        elif col == 6:
            label = ttk.Label(tab, text=headers[6], font=("Arial", 10, "bold"), anchor="center", borderwidth=1,
                              relief="solid")
            label.grid(row=0, column=6, rowspan=2, padx=1, pady=1, sticky="nsew")

    for col, sub_header in enumerate(sub_headers):
        if 2 <= col <= 5:
            label = ttk.Label(tab, text=sub_headers[col], font=("Arial", 10), anchor="center", borderwidth=1,
                              relief="solid")
            label.grid(row=1, column=col, padx=1, pady=1, sticky="nsew")

    label = ttk.Label(tab, text="Вагові коефіцієнти / оцінки експертів, бали", font=("Arial", 10), anchor="center",
                      borderwidth=1, relief="solid")
    label.grid(row=2, column=2, columnspan=4, padx=1, pady=1, sticky="nsew")

    for row, (label_data, before_data, after_data) in enumerate(
            zip(criteria_labels, weights, score), start=3):
        ttk.Label(tab, text=label_data[0], anchor="center", borderwidth=1, relief="solid").grid(row=row, column=0, padx=1, pady=1, sticky="nsew")
        ttk.Label(tab, text=label_data[1], anchor="center", borderwidth=1, relief="solid").grid(row=row, column=1, padx=1, pady=1, sticky="nsew")

        row_entries = []
        for col, (before, after) in enumerate(zip(before_data, after_data), start=2):
            frame = ttk.Frame(tab, borderwidth=1, relief="solid")
            frame.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")

            entry_before = tk.Entry(frame, justify="center", width=7, font=("Arial", 10))
            entry_before.insert(0, before)
            entry_before.grid(row=0, column=0)
            entry_before.bind("<KeyRelease>", lambda event: update_totals())

            separator = ttk.Label(frame, text="/", anchor="center", font=("Arial", 10))
            separator.grid(row=0, column=1)

            entry_after = tk.Entry(frame, justify="center", width=7, font=("Arial", 10))
            entry_after.insert(0, after)
            entry_after.grid(row=0, column=2)
            entry_after.bind("<KeyRelease>", lambda event: update_totals())

            row_entries.append((entry_before, entry_after))
        entry_fields.append(row_entries)

        average_label = ttk.Label(tab, text="0.00", anchor="center", borderwidth=1, relief="solid", font=("Arial", 10, "bold"))
        average_label.grid(row=row, column=6, padx=1, pady=1, sticky="nsew")
        average_labels.append(average_label)

    ttk.Label(tab, text="Загальна/середня кількість балів", anchor="center", font=("Arial", 10, "bold"), borderwidth=1, relief="solid").grid(row=13, column=1, padx=1, pady=1, sticky="nsew")

    for col in range(2, 6):
        frame = ttk.Frame(tab, borderwidth=1, relief="solid")
        frame.grid(row=13, column=col, padx=1, pady=1, sticky="nsew")

        label_before = ttk.Label(frame, text="0", anchor="center", font=("Arial", 10, "bold"))
        label_before.grid(row=0, column=0)

        separator = ttk.Label(frame, text="/", anchor="center", font=("Arial", 10))
        separator.grid(row=0, column=1)

        label_after = ttk.Label(frame, text="0.00", anchor="center", font=("Arial", 10, "bold"))
        label_after.grid(row=0, column=2)

        result_labels.append((label_before, label_after))

    for col in range(len(headers)):
        tab.grid_columnconfigure(col, weight=1)
    for row in range(len(criteria_labels) + 3):
        tab.grid_rowconfigure(row, weight=1)

    update_totals()
    return weights,score
