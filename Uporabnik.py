class Uporabnik:
    def __init__(self, ime, geslo, mail="example@mail.com") -> None:
        self.ime = ime
        self.mail = mail
        self.geslo = geslo
        self.stran_ime_geslo = []
        self.hash = -1

    def spremeni_geslo(self, geslo):
        return

    def spremeni_ime(self, ime):
        return

    def __hash__(self):
        return self.hash

