import tkinter as tk
from tkinter import ttk

def create_tabs(root):
    notebook = ttk.Notebook(root)

    # 1. Zakładka Myjnie
    frame_myjnie = ttk.Frame(notebook)
    notebook.add(frame_myjnie, text="Myjnie")
    ttk.Label(frame_myjnie, text="Tu będzie panel zarządzania myjniami").pack(padx=20, pady=20)

    # 2. Zakładka Klienci
    frame_klienci = ttk.Frame(notebook)
    notebook.add(frame_klienci, text="Klienci")
    ttk.Label(frame_klienci, text="Tu będzie panel zarządzania klientami").pack(padx=20, pady=20)

    # 3. Zakładka Pracownicy
    frame_pracownicy = ttk.Frame(notebook)
    notebook.add(frame_pracownicy, text="Pracownicy")
    ttk.Label(frame_pracownicy, text="Tu będzie panel zarządzania pracownikami").pack(padx=20, pady=20)

    # 4. Zakładka Mapa
    frame_mapa = ttk.Frame(notebook)
    notebook.add(frame_mapa, text="Mapa")
    ttk.Label(frame_mapa, text="Tu będzie mapa interaktywna").pack(padx=20, pady=20)

    notebook.pack(expand=True, fill="both")

def main():
    root = tk.Tk()
    root.title("System zarządzania siecią myjni")
    root.geometry("1000x600")
    create_tabs(root)
    root.mainloop()

if __name__ == "__main__":
    main()
asd