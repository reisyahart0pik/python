import tkinter as tk
from tkinter import messagebox

def hitung():
    try:
        angka1 = float(entry1.get())
        angka2 = float(entry2.get())
        operasi = operasi_var.get()
        
        if operasi == "+":
            hasil = angka1 + angka2
        elif operasi == "-":
            hasil = angka1 - angka2
        elif operasi == "*":
            hasil = angka1 * angka2
        elif operasi == "/":
            if angka2 != 0:
                hasil = angka1 / angka2
            else:
                messagebox.showerror("Error", "Tidak bisa dibagi 0!")
                return
        else:
            messagebox.showerror("Error", "Operasi tidak valid!")
            return
        
        label_hasil.config(text=f"Hasil: {hasil}")
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")

# === GUI ===
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("900x600")
root.configure(bg="#1e3d59")  # biru tua

judul_font = ("Arial", 26, "bold")
label_font = ("Arial", 18)
entry_font = ("Arial", 18)
button_font = ("Arial", 18, "bold")

# Pakai grid biar responsif
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(0, weight=1)

# Judul
judul = tk.Label(root, text="Kalkulator Sederhana", font=judul_font, bg="#1e3d59", fg="white")
judul.grid(row=0, column=0, pady=10, sticky="n")

# Angka pertama
label1 = tk.Label(root, text="Angka Pertama:", font=label_font, bg="#1e3d59", fg="white")
label1.grid(row=1, column=0, sticky="n")
entry1 = tk.Entry(root, font=entry_font, justify="center", bd=3, relief="solid")
entry1.grid(row=2, column=0, ipadx=50, ipady=10)

# Angka kedua
label2 = tk.Label(root, text="Angka Kedua:", font=label_font, bg="#1e3d59", fg="white")
label2.grid(row=3, column=0, sticky="n")
entry2 = tk.Entry(root, font=entry_font, justify="center", bd=3, relief="solid")
entry2.grid(row=4, column=0, ipadx=50, ipady=10)

# Operasi
label3 = tk.Label(root, text="Pilih Operasi:", font=label_font, bg="#1e3d59", fg="white")
label3.grid(row=5, column=0, sticky="n")
operasi_var = tk.StringVar()
operasi_var.set("+")
opsi = ["+", "-", "*", "/"]
menu = tk.OptionMenu(root, operasi_var, *opsi)
menu.config(font=button_font, width=6, bg="#145374", fg="white", relief="flat", activebackground="#0c2d48")
menu.grid(row=6, column=0, pady=10)

# Tombol Hitung
btn = tk.Button(root, text="Hitung", command=hitung, font=button_font, bg="#0c2d48", fg="white",
                width=12, height=2, relief="flat", activebackground="#3282b8")
btn.grid(row=7, column=0, pady=15)

# Label hasil
label_hasil = tk.Label(root, text="Hasil: ", font=("Arial", 22, "bold"), bg="#1e3d59", fg="#f8f9fa")
label_hasil.grid(row=8, column=0, pady=20)

# Footer
footer = tk.Label(root, text="Terima kasih telah menggunakan kalkulator ini!",
                  font=("Arial", 14), bg="#1e3d59", fg="#bbdefb", wraplength=700, justify="center")
footer.grid(row=9, column=0, pady=15)

root.mainloop()
