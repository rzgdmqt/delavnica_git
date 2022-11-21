import os
import re
import tkinter as tk

from Uporabnik import Uporabnik


class Main:
    def __init__(self, okno):
        self.uporabniki = {}
        self.aktivni_uporabnik = None

        self.okno = okno
        self.okno.title("papiga")
        self.okno.configure(bg="white")
        self.okno.minsize(900, 500)
        
        self.glavno_okno = tk.Frame(bg="white")
        self.glavno_okno.pack()

        self.naslovno_besedilo = tk.Frame(self.glavno_okno)
        self.besedilo = tk.Label(self.naslovno_besedilo, text="aplikacija za shranjevanje gesl", bg="white")
        self.naslovno_besedilo.pack()
        self.besedilo.pack()


        self.vstopna_stran = tk.Frame(self.glavno_okno, bg="white")
        self.vpis_ime = tk.Entry(self.vstopna_stran)
        self.vpis_geslo = tk.Entry(self.vstopna_stran, show="*")
        self.vpis_ime_besedilo = tk.Label(self.vstopna_stran, text="Uporabniško ime: ", bg="white", justify=tk.LEFT)
        self.vpis_geslo_besedilo = tk.Label(self.vstopna_stran, text="Geslo: ", bg="white", justify=tk.LEFT)
        self.gumb_prijava = tk.Button(self.vstopna_stran, text="Prijava", bg="white", command=self.prijava)
        self.gumb_registracija = tk.Button(self.vstopna_stran, text="Registracija", bg="white")
        self.neveljavna_prijava = tk.Label(self.vstopna_stran, text="", bg="white")
        self.vstopna_stran.pack(pady=10)
        self.vpis_ime.grid(row=0, column=1, columnspan=2)
        self.vpis_geslo.grid(row=1, column=1, columnspan=2)
        self.vpis_ime_besedilo.grid(row=0, column=0, sticky="e")
        self.vpis_geslo_besedilo.grid(row=1, column=0, sticky="e")
        self.gumb_prijava.grid(row=3, column=1, padx=2, pady=2)
        self.gumb_registracija.grid(row=3, column=2, padx=2, pady=2)
        self.neveljavna_prijava.grid(row=4, column=0, columnspan=30)

        self.prijavljen_uporabnik = tk.Frame(self.okno, bg="white")

        for oseba_dat in os.listdir("uporabniki"):
            if not re.match(r".*?.oseba", oseba_dat):
                continue
            pot = os.path.join("uporabniki", oseba_dat)
            with open(pot) as f:
                for vr in f:
                    if vr.startswith("!"):
                        _, ime_u, geslo_u = vr.split()
                        uporabnik = Uporabnik(ime_u, geslo_u)
                        self.uporabniki[(ime_u, geslo_u)] = uporabnik
                        continue
                    if " " not in vr:
                        continue
                    stran, ime, geslo = vr.split()
                    self.uporabniki[(ime_u, geslo_u)].stran_ime_geslo.append((stran, ime, geslo))
        
    def prijava(self):
        ime_geslo = (self.vpis_ime.get(), self.vpis_geslo.get())
        if ime_geslo not in self.uporabniki:
            self.neveljavna_prijava.config(text="Neveljavna prijava, napačno uporabniško ime ali geslo. Ste se registrirali?")
            return
        self.aktivni_uporabnik = self.uporabniki[ime_geslo]
        self.prikazi_prijavo(self.uporabniki[ime_geslo])

    def prikazi_prijavo(self, uporabnik):
        self.neveljavna_prijava.config(text="")
        self.vstopna_stran.destroy()
        prijavljeni = tk.Label(self.prijavljen_uporabnik, text=f"Prijavljeni ste kot: {uporabnik.ime}\n", bg="white", justify=tk.LEFT)
        prijavljeni.pack(anchor="w")
        for stran, ime, geslo in self.uporabniki[uporabnik.ime, uporabnik.geslo].stran_ime_geslo:
            label = tk.Label(self.prijavljen_uporabnik, text=f"stran: {stran}\nuporabniško ime: {ime}\ngeslo: {geslo}\n", bg="white", justify=tk.LEFT)
            label.pack(anchor="w")
        dodaj_stran = tk.Entry(self.prijavljen_uporabnik)
        dodaj_ime = tk.Entry(self.prijavljen_uporabnik)
        dodaj_geslo = tk.Entry(self.prijavljen_uporabnik)
        dodaj_gumb = tk.Button(self.prijavljen_uporabnik, text="Shrani", bg="white")
        odjavi_gumb = tk.Button(self.prijavljen_uporabnik, text="Odjava", bg="white")
        dodaj_stran.pack()
        dodaj_ime.pack()
        dodaj_geslo.pack()
        dodaj_gumb.pack()
        odjavi_gumb.pack()
        self.prijavljen_uporabnik.pack()
        
    def dodaj_geslo(self, uporabnik, stran, ime, geslo):
        ...

    def registracija(self):
        ...

    def prikazi_registracijo(self):
        ...

    def odjava(self):
        ...



okno = tk.Tk()
Main(okno)
okno.mainloop()