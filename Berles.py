from Autokolcsonzo import Autokolcsonzo

class Berles:
    def __init__(self, datum, rendszam, igszam):
        self.datum = datum
        self.rendszam = rendszam
        self.igszam = igszam
        self._berlesek = []

    @property
    def berlesek(self):
        for berles in self._berlesek:
            print(f" Dátum: {berles.datum}, Rendszám: {berles.rendszam}, Igazolványszám: {berles.igszam}")

    @berlesek.setter
    def berlesek(self, uj_berles):
        self._berlesek.append(uj_berles)