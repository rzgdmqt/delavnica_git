import tkinter as tk

class VstopnaStran:

  def __init__(self, master):
        self.vstopna_stran = tk.Frame(master)
        self.vpis_ime = tk.Entry(self.vstopna_stran)
        self.vpis_geslo = tk.Entry(self.vstopna_stran)
        self.vstopna_stran.pack()
        self.vpis_ime.pack()
        self.vpis_geslo.pack()
