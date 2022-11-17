import tkinter as tk


class Main:
    def __init__(self, okno):
        self.uporabniki = []
        self.okno = okno
        self.okno.title("papiga")
        self.okno.configure(bg="white")
        self.okno.minsize(900, 500)
        self.glavno_okno = tk.Frame()
        self.vstopna_stran = tk.Frame()
        self.vpis_ime = tk.Entry(self.vstopna_stran)
        self.vpis_geslo = tk.Entry(self.vstopna_stran)
        self.glavno_okno.pack()
        self.vstopna_stran.pack()
        self.vpis_ime.pack()
        self.vpis_geslo.pack()



okno = tk.Tk()
Main(okno)
okno.mainloop()