import tkinter as tk
from tkinter import messagebox


# ALGORITMA ZIG-ZAG CIPHER

def encrypt(text, rails):

    if rails == 1:
        return text

    fence = ['' for _ in range(rails)]

    row = 0
    direction = 1

    for char in text:
        fence[row] += char

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return ''.join(fence)



def decrypt(cipher, rails):

    if rails == 1:
        return cipher

    pattern = list(range(rails)) + list(range(rails-2, 0, -1))

    index = []

    for i in range(len(cipher)):
        index.append(pattern[i % len(pattern)])


    rail_count = []

    for i in range(rails):
        rail_count.append(index.count(i))


    rails_text = []

    posisi = 0

    for jumlah in rail_count:
        rails_text.append(
            list(cipher[posisi:posisi+jumlah])
        )
        posisi += jumlah


    hasil = ""

    posisi_rail = [0] * rails


    for r in index:

        hasil += rails_text[r][posisi_rail[r]]

        posisi_rail[r] += 1


    return hasil



# BUTTON FUNCTION


def proses_enkripsi():

    try:

        pesan = input_pesan.get()

        rail = int(input_rail.get())


        hasil = encrypt(pesan, rail)

        output.delete(0, tk.END)
        output.insert(0, hasil)


    except:

        messagebox.showerror(
            "Error",
            "Jumlah rail harus berupa angka"
        )



def proses_dekripsi():

    try:

        pesan = input_pesan.get()

        rail = int(input_rail.get())


        hasil = decrypt(pesan, rail)

        output.delete(0, tk.END)
        output.insert(0, hasil)


    except:

        messagebox.showerror(
            "Error",
            "Jumlah rail harus berupa angka"
        )



def reset():

    input_pesan.delete(0, tk.END)
    input_rail.delete(0, tk.END)
    output.delete(0, tk.END)



# GUI DESIGN


window = tk.Tk()

window.title(
    "Aplikasi Zig-Zag Cipher"
)

window.geometry(
    "650x600"
)

window.configure(
    bg="#D9EEFF"
)



# Judul

judul = tk.Label(
    window,
    text="🔐 ZIG-ZAG CIPHER",
    font=("Segoe UI", 26, "bold"),
    bg="#D9EEFF",
    fg="#0B3D91"
)

judul.pack(pady=25)



subjudul = tk.Label(
    window,
    text="Classical Cryptography - Rail Fence Cipher",
    font=("Segoe UI", 12),
    bg="#D9EEFF",
    fg="#444"
)

subjudul.pack()



# CARD UTAMA

card = tk.Frame(
    window,
    bg="white",
    padx=35,
    pady=30
)

card.pack(
    pady=30
)



# INPUT PESAN

tk.Label(
    card,
    text="Masukkan Pesan",
    font=("Segoe UI", 12, "bold"),
    bg="white"
).pack()


input_pesan = tk.Entry(
    card,
    width=45,
    font=("Segoe UI", 12)
)

input_pesan.pack(pady=10)



# RAIL

tk.Label(
    card,
    text="Jumlah Rail / Key",
    font=("Segoe UI", 12, "bold"),
    bg="white"
).pack()


input_rail = tk.Entry(
    card,
    width=15,
    justify="center",
    font=("Segoe UI", 12)
)

input_rail.pack(pady=10)



# BUTTON

button_frame = tk.Frame(
    card,
    bg="white"
)

button_frame.pack(pady=20)



btn_encrypt = tk.Button(
    button_frame,
    text="🔒 ENKRIPSI",
    width=14,
    height=2,
    bg="#1976D2",
    fg="white",
    font=("Segoe UI",10,"bold"),
    command=proses_enkripsi
)

btn_encrypt.grid(
    row=0,
    column=0,
    padx=8
)



btn_decrypt = tk.Button(
    button_frame,
    text="🔓 DEKRIPSI",
    width=14,
    height=2,
    bg="#2E7D32",
    fg="white",
    font=("Segoe UI",10,"bold"),
    command=proses_dekripsi
)

btn_decrypt.grid(
    row=0,
    column=1,
    padx=8
)



btn_reset = tk.Button(
    button_frame,
    text="↻ RESET",
    width=14,
    height=2,
    bg="#C62828",
    fg="white",
    font=("Segoe UI",10,"bold"),
    command=reset
)

btn_reset.grid(
    row=0,
    column=2,
    padx=8
)



# HASIL

tk.Label(
    card,
    text="Hasil",
    font=("Segoe UI",12,"bold"),
    bg="white"
).pack()



output = tk.Entry(
    card,
    width=45,
    font=("Segoe UI",12)
)

output.pack(pady=10)



# INFO

info = tk.Label(
    window,
    text="Plaintext → Enkripsi → Ciphertext\nCiphertext → Dekripsi → Plaintext",
    font=("Segoe UI",11),
    bg="#D9EEFF",
    fg="#555"
)

info.pack()



window.mainloop()