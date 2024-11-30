class Autokolcsonzo:
    def __init__(self, nev):
        self._nev = nev
        self._autok = []

    @property
    def nev(self):
        return self._nev

    @property
    def autok(self):
        for auto in self._autok:
            print(f" Rendszám: {auto.rendszam}, Ára: {auto.berleti_dij} huf")

    @autok.setter
    def autok(self, uj_auto):
        self._autok.append(uj_auto)

    def berleti_kiiras(self, rendszam):
        for auto in self._autok:
            if (auto.rendszam == rendszam):
                print(f"A bérleti díj: {auto.berleti_dij} huf")