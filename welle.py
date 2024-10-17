import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog

class RataRataApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Penghitung Rata-rata")
        self.master.geometry("600x500")
        self.master.configure(bg="#f0f0f0")

        # Title label
        self.title_label = tk.Label(master, text="Penghitung Rata-rata", font=("Arial", 24, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # Instructions label
        self.label = tk.Label(master, text="Masukkan tiga nilai untuk menghitung rata-rata:", bg="#f0f0f0", font=("Arial", 12))
        self.label.pack(pady=10)

        # Input button
        self.button_input = tk.Button(master, text="Input Nilai", command=self.input_nilai, font=("Arial", 14), bg="#4CAF50", fg="white")
        self.button_input.pack(pady=5, padx=20)

        # Reset button
        self.button_reset = tk.Button(master, text="Reset", command=self.reset, font=("Arial", 14), bg="#f44336", fg="white")
        self.button_reset.pack(pady=5, padx=20)

        # History button
        self.button_history = tk.Button(master, text="Lihat Riwayat", command=self.show_history, font=("Arial", 14), bg="#2196F3", fg="white")
        self.button_history.pack(pady=5, padx=20)

        # Clear history button
        self.button_clear_history = tk.Button(master, text="Hapus Riwayat", command=self.clear_history, font=("Arial", 14), bg="#FFC107", fg="black")
        self.button_clear_history.pack(pady=5, padx=20)

        # Save history button
        self.button_save_history = tk.Button(master, text="Simpan Riwayat", command=self.save_history, font=("Arial", 14), bg="#9C27B0", fg="white")
        self.button_save_history.pack(pady=5, padx=20)

        # Load history button
        self.button_load_history = tk.Button(master, text="Muat Riwayat", command=self.load_history, font=("Arial", 14), bg="#2196F3", fg="white")
        self.button_load_history.pack(pady=5, padx=20)

        # Result area
        self.result_area = tk.Text(master, height=10, width=50, font=("Arial", 12), bg="#ffffff")
        self.result_area.pack(pady=10, padx=20)

        self.history = []  # To store previous results

    def input_nilai(self):
        try:
            nilai1 = simpledialog.askinteger("Input", "Masukkan Nilai 1:", minvalue=0, maxvalue=100)
            nilai2 = simpledialog.askinteger("Input", "Masukkan Nilai 2:", minvalue=0, maxvalue=100)
            nilai3 = simpledialog.askinteger("Input", "Masukkan Nilai 3:", minvalue=0, maxvalue=100)
            if None in (nilai1, nilai2, nilai3):
                raise ValueError("Input tidak boleh kosong!")
            rata = (nilai1 + nilai2 + nilai3) / 3
            hasil = "LULUS" if rata >= 60 else "GAGAL"
            result_message = (
                f"Nilai 1: {nilai1}\n"
                f"Nilai 2: {nilai2}\n"
                f"Nilai 3: {nilai3}\n"
                f"Rata-rata: {rata:.2f}\n"
                f"Hasil: {hasil}\n"
            )
            self.result_area.delete(1.0, tk.END)
            self.result_area.insert(tk.END, result_message)
            self.history.append((nilai1, nilai2, nilai3, rata, hasil))  # Store values in a tuple
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def reset(self):
        self.result_area.delete(1.0, tk.END)
        self.history.clear()

    def show_history(self):
        if not self.history:
            messagebox.showinfo("Riwayat", "Tidak ada riwayat.")
            return
        history_message = "\n".join(f"Nilai: {h[0]}, {h[1]}, {h[2]} - Rata-rata: {h[3]:.2f}, Hasil: {h[4]}" for h in self.history)
        messagebox.showinfo("Riwayat Hasil", history_message)

    def clear_history(self):
        self.history.clear()
        messagebox.showinfo("Riwayat", "Riwayat telah dihapus.")

    def save_history(self):
        if not self.history:
            messagebox.showinfo("Riwayat", "Tidak ada riwayat untuk disimpan.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as f:
                for h in self.history:
                    f.write(f"Nilai: {h[0]}, {h[1]}, {h[2]} - Rata-rata: {h[3]:.2f}, Hasil: {h[4]}\n")
            messagebox.showinfo("Riwayat", "Riwayat berhasil disimpan.")

    def load_history(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as f:
                for line in f:
                    parts = line.strip().split(' - ')
                    nilai1, nilai2, nilai3 = map(int, parts[0].split(': ')[1].split(', '))
                    rata = float(parts[1].split(': ')[1])
                    hasil = parts[2].split(': ')[1]
                    self.history.append((nilai1, nilai2, nilai3, rata, hasil))
            messagebox.showinfo("Riwayat", "Riwayat berhasil dimuat.")

def toggle_fullscreen(event=None):
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)

def end_fullscreen(event=None):
    window.attributes('-fullscreen', False)

# Creating the root window
window = tk.Tk()
app = RataRataApp(window)

# Bind keys for fullscreen toggle
window.bind('<F11>', toggle_fullscreen)
window.bind('<Escape>', end_fullscreen)

# Start the Tkinter event loop
window.mainloop()