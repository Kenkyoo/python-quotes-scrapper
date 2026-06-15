import tkinter as tk
from tkinter import messagebox
import re
import pandas as pd
from scrapper import quotes_scrapper

def run_scrapper():
    url = entry.get().strip()
    if not url:
        messagebox.showwarning("Falta URL", "Ingresá un link para buscar.")
        return

    output.config(state='normal')
    output.delete('1.0', tk.END)
    status_var.set("Buscando citas...")
    root.update()

    try:
        quotes = quotes_scrapper(url)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo acceder al link:\n{e}")
        status_var.set("")
        output.config(state='disabled')
        return

    if quotes:
        output.insert(tk.END, f"✅ {len(quotes)} citas encontradas:\n\n")
        for i, q in enumerate(quotes, 1):
            output.insert(tk.END, f"{i}. {q}\n\n")

        df = pd.DataFrame(quotes, columns=['Quote'])
        df.to_csv('quotes.csv', index=False, encoding='utf-8')
        status_var.set(f"{len(quotes)} citas encontradas · Guardado en quotes.csv")
    else:
        output.insert(tk.END, "❌ No se encontraron citas entre comillas.")
        status_var.set("Sin resultados.")

    output.config(state='disabled')


# --- UI ---
root = tk.Tk()
root.title("Quotes Scrapper")
root.geometry("720x600")
root.resizable(True, True)

frame = tk.Frame(root, padx=16, pady=12, bg='#2e3440')
frame.pack(fill='both', expand=True)

tk.Label(frame, text="URL", bg="#a3be8c", fg="#eceff4", padx=(2), font=('Helvetica', 10, 'bold')).pack(anchor='w')

input_row = tk.Frame(frame)
input_row.pack(fill='x', pady=(4, 10))

entry = tk.Entry(input_row, font=('Helvetica', 11), bg="#eceff4", fg="#2e3440")
entry.pack(side='left', fill='x', expand=True, ipady=5)

btn = tk.Button(input_row, text="Buscar", command=run_scrapper,
                font=('Helvetica', 10, 'bold'), padx=12, fg='#eceff4', bg="#bf616a")
btn.pack(side='left', padx=(2))

output = tk.Text(frame, font=('Helvetica', 13), wrap='word',
                 state='disabled', relief='flat', bg='#3b4252', fg="#d8dee9")
output.pack(fill='both', expand=True)

scrollbar = tk.Scrollbar(frame, command=output.yview)
output.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')

status_var = tk.StringVar()
tk.Label(root, textvariable=status_var, anchor='w',
         font=('Helvetica', 12), bg='#b48ead', fg="white").pack(fill='x', pady=2)

entry.bind('<Return>', lambda e: run_scrapper())
root.mainloop()
