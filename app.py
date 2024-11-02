from tkinter import *
from datetime import datetime
import os
from PIL import Image
import customtkinter as ctk
from tkinter import messagebox
import csv 
from csv import writer
import random
import string

# VARIJABLE 
nazivDatoteke = 'Lozinke.csv'  # Naziv CSV datoteke u kojoj ćemo čuvati lozinke
duzinaPAss = 12  # Početna dužina lozinke

# FUNKCIJE

# Funkcija za resetiranje unosa
def reset():
    # Prikazujemo upozorenje korisniku prije resetiranja
    msg_box = messagebox.askquestion('Brisanje podataka', 'Jeste li sigurni?', icon='warning')
    if msg_box == 'yes':
        lozinka_adress_Entry.delete(0, END)
        web_adress_Entry.delete(0, END)
        web_adress_Entry.focus_set()
    else:
        web_adress_Entry.focus_set()

# Funkcija za spremanje lozinke u CSV datoteku
def spremi():
    if len(web_adress_Entry.get()) == 0 or len(lozinka_adress_Entry.get()) == 0:
        # Provjeravamo je li korisnik unio sve potrebne podatke
        messagebox.showinfo('Upozorenje', 'Navedite potrebene informacije...')
        lozinka_adress_Entry.delete(0, END)
        web_adress_Entry.delete(0, END)
        web_adress_Entry.focus_set()
    else:
        adresa = web_adress_Entry.get()
        password = lozinka_adress_Entry.get()

        # Brojimo redove u CSV datoteci kako bismo dodali redni broj za novu lozinku
        with open(nazivDatoteke, 'r') as f:
            redovi = list(csv.reader(f))
        br = len(redovi) + 1  # Redni broj novog unosa

        # Kreiramo red s podacima koje ćemo dodati
        rows = [br, adresa, password]
        with open(nazivDatoteke, 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(rows)  # Dodajemo novi red u CSV datoteku

        # Resetiramo unose nakon spremanja
        lozinka_adress_Entry.delete(0, END)
        web_adress_Entry.delete(0, END)
        web_adress_Entry.focus_set()
        messagebox.showinfo('Podaci spremljeni', 'Nastavite rad s aplikacijom')

# Funkcija za generiranje lozinke
def generiraj_Lozinku():
    global duzinaPAss  # Definiranje globalne varijable
    lozinka_adress_Entry.delete(0, END)  # Brišemo prethodni unos lozinke

    # Kreiramo listu slova i brojeva za slučajni odabir karaktera
    mojaLista = list(string.ascii_letters) + [str(br) for br in range(10)]
    lozinka_trenutna = ''

    try:
        # Uzimamo dužinu lozinke iz unosa
        noviDuljina = int(duljina_lozinke_Entry.get())
        if noviDuljina >= 12:
            duzinaPAss = noviDuljina  # Ako je dužina veća ili jednaka 12, ažuriramo globalnu varijablu
        else:
            messagebox.showwarning("Upozorenje", "Lozinka treba biti barem 12 znakova.")
            return
    except ValueError:
        # Ako korisnik unese slovo umjesto broja, prikazujemo poruku
        messagebox.showwarning("Upozorenje", "Molimo unesite ispravnu brojčanu dužinu lozinke.")
        return

    # Generiramo lozinku odgovarajuće dužine
    for _ in range(duzinaPAss):
        slucajni = random.choice(mojaLista)
        lozinka_trenutna += slucajni

    print("Generirana lozinka je: ", lozinka_trenutna)
    lozinka_adress_Entry.insert(0, lozinka_trenutna)  # Unosimo generiranu lozinku u polje

# Funkcija za prikaz glavnog okvira aplikacije
def aplikacija():
    novi_okvir.pack_forget()  # Sakrijemo okvir za postavke
    okvir_aplikacije.pack()

# Funkcija za prikaz postavki aplikacije
def postavke():
    nazivDatoteke_variabla.set(nazivDatoteke)  # Postavljamo naziv datoteke u varijablu
    okvir_aplikacije.pack_forget()
    novi_okvir.pack(side='top', expand=False, fill='y', pady=2, padx=40)

# Funkcija za primjenu novih postavki
def odaberi_postavke():
    try:
        # Pretvaramo unos za dužinu lozinke u cijeli broj
        string_u_int = int(duljina_lozinke_Entry.get())
        aplikacija()  # Vraćamo korisnika na glavnu aplikaciju

        # Ažuriramo globalnu varijablu za naziv datoteke
        global nazivDatoteke
        nazivDatoteke = naziv_datoteke_Entry.get()

    except ValueError:
        # Prikazujemo upozorenje ako korisnik unese nevažeću vrijednost
        messagebox.showwarning('Upozorenje','Unesite brojeve, a ne slova. Hvala!')
        duljina_lozinke_Entry.delete(0, END)
        duljina_lozinke_Entry.insert(0, duzinaPAss)
        duljina_lozinke_Entry.focus_set()

# KREIRANJE GLAVNOG PROZORA
root = ctk.CTk()

# Postavljamo osnovne postavke za izgled aplikacije
ctk.set_default_color_theme("dark-blue")  # Mogućnosti: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode('light')

root.resizable(False, False)
root.title('PassWord Organizator')

# Centriramo prozor na ekranu
duljina, visina = 600, 500
x = (root.winfo_screenwidth() // 2) - (duljina // 2)
y = (root.winfo_screenheight() // 2) - (visina // 2)
root.geometry(f"{duljina}x{visina}+{x}+{y}")
root.config(bg='white')
root.iconbitmap('PassLogo.ico')

# VARIJABLE
web_lokacija = StringVar()
password_variabla = StringVar()
duzinaLozinke = StringVar()
nazivDatoteke_variabla = StringVar()

# DODAVANJE SLIKE
Logo = ctk.CTkImage(Image.open("Organizator.png"), size=(250, 250))

# Prikaz logotipa aplikacije
slika_Label = ctk.CTkLabel(root, image=Logo, text="")
slika_Label.pack(pady=10)

# OKVIR APLIKACIJE
okvir_aplikacije = ctk.CTkFrame(root, fg_color='white')
okvir_aplikacije.pack(side='top', expand=False, fill='y', pady=2, padx=40)

# Labele i Entry polja u okviru aplikacije
web_adress_Labela = ctk.CTkLabel(okvir_aplikacije, text='Web lokacija:')
web_adress_Labela.grid(row=0, column=0, padx=5, pady=20)

web_adress_Entry = ctk.CTkEntry(okvir_aplikacije, textvariable=web_lokacija)
web_adress_Entry.grid(row=0, column=1, padx=30)

lozinka_adress_Labela = ctk.CTkLabel(okvir_aplikacije, text='Unesite lozinku:')
lozinka_adress_Labela.grid(row=1, column=0, padx=5)

lozinka_adress_Entry = ctk.CTkEntry(okvir_aplikacije, textvariable=password_variabla)
lozinka_adress_Entry.grid(row=1, column=1, padx=30)

generiraj_Lozinku_Tipka = ctk.CTkButton(okvir_aplikacije, text='Generiraj lozinku', fg_color='#051D40', command=generiraj_Lozinku)
generiraj_Lozinku_Tipka.grid(row=1, column=2, padx=5)

# Tipke u okviru aplikacije
spremi_Tipka = ctk.CTkButton(okvir_aplikacije, text='Spremi podatke', fg_color='#051D40', command=spremi)
spremi_Tipka.grid(row=2, column=0, padx=10, pady=50)

reset_Tipka = ctk.CTkButton(okvir_aplikacije, text='Reset', fg_color='#051D40', command=reset)
reset_Tipka.grid(row=2, column=1, padx=10)

postavke_Tipka = ctk.CTkButton(okvir_aplikacije, text='Postavke', fg_color='#051D40', command=postavke)
postavke_Tipka.grid(row=2, column=2, padx=10)

# OKVIR POSTAVKI
novi_okvir = ctk.CTkFrame(root, fg_color='white')

duljina_lozinke_Label = ctk.CTkLabel(novi_okvir, text="Duljina lozinke:")
duljina_lozinke_Label.grid(row=0, column=0, pady=10)

duljina_lozinke_Entry = ctk.CTkEntry(novi_okvir, textvariable=duzinaLozinke)
duljina_lozinke_Entry.insert(0, duzinaPAss)
duljina_lozinke_Entry.grid(row=0, column=1, padx=30)

naziv_datoteke_Label = ctk.CTkLabel(novi_okvir, text="Naziv datoteke:")
naziv_datoteke_Label.grid(row=1, column=0, pady=10)

naziv_datoteke_Entry = ctk.CTkEntry(novi_okvir, textvariable=nazivDatoteke_variabla)
naziv_datoteke_Entry.grid(row=1, column=1)

potvrdi_Tipka = ctk.CTkButton(novi_okvir, text='Potvrdi postavke', fg_color='#051D40', command=odaberi_postavke)
potvrdi_Tipka.grid(row=2, column=1, pady=20)

# Pokrećemo glavni prozor aplikacije
root.mainloop()
