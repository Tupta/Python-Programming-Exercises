# import tkinter as tk

# def pole_klikniete(num):
#     print("Kliknięto pole nr:", num)

# root = tk.Tk()
# root.title("Plansza 10x10")

# # Tworzenie siatki planszy
# for i in range(10):
#     for j in range(10):
#         num = i * 10 + j + 1
#         button = tk.Button(root, text=str(num), width=4, command=lambda num=num: pole_klikniete(num))
#         button.grid(row=i, column=j)

# root.mainloop()


import tkinter as tk
import random

def pole_klikniete(num):
    print("Kliknięto pole nr:", num)

def rzut_kostka():
    ruch = random.randint(1, 6)  # Symulacja rzutu kością
    print("Rzut kostką:", ruch)
    przemiesc_pionek(ruch)

def przemiesc_pionek(ruch):
    global pozycja_pionka
    pozycja_pionka += ruch
    if pozycja_pionka > 100:
        pozycja_pionka = 100
    print("Przesunięcie pionka na pole nr:", pozycja_pionka)
    # Tutaj możesz dodać dodatkową logikę dla przemieszczenia pionka na planszy

root = tk.Tk()
root.title("Plansza 10x10")

pozycja_pionka = 1  # Początkowa pozycja pionka

# Tworzenie siatki planszy
for i in range(10):
    for j in range(10):
        num = i * 10 + j + 1
        button = tk.Button(root, text=str(num), height = 2, width=4, command=lambda num=num: pole_klikniete(num))
        button.grid(row=i, column=j)

rzut_kostka_button = tk.Button(root, text="Rzuć kostką", command=rzut_kostka)
rzut_kostka_button.grid(row=10, columnspan=10)

root.mainloop()
