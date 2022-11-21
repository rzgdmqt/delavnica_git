import tkinter as tk
import os


class Main:
    def __init__(self, okno):
        self.uporabniki = []

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
        self.vpis_geslo = tk.Entry(self.vstopna_stran)
        self.vpis_ime_besedilo = tk.Label(self.vstopna_stran, text="Uporabniško ime: ", bg="white")
        self.vpis_geslo_besedilo = tk.Label(self.vstopna_stran, text="Geslo: ", bg="white")
        self.gumb_prijava = tk.Button(self.vstopna_stran, text="Prijava", bg="white")
        self.gumb_registracija = tk.Button(self.vstopna_stran, text="Registracija", bg="white")
        self.vstopna_stran.pack(pady=10)
        self.vpis_ime.grid(row=0, column=1, columnspan=2)
        self.vpis_geslo.grid(row=1, column=1, columnspan=2)
        self.vpis_ime_besedilo.grid(row=0, column=0)
        self.vpis_geslo_besedilo.grid(row=1, column=0)
        self.gumb_prijava.grid(row=3, column=1, padx=2, pady=2)
        self.gumb_registracija.grid(row=3, column=2, padx=2, pady=2)

        for oseba in os.listdir("uporabbniki"):
            

    def prijava(self):
        if self.vpis_ime 
        self.okno.destroy()
        self.okno = tk.Button(self.glavno_okno, text="Prijava", bg="white")
        self.okno.grid(row=0, column=0)




okno = tk.Tk()
Main(okno)
okno.mainloop()