from Auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij):
        super().__init__(rendszam, tipus, berleti_dij)
        self.terfogat = int
        self.teher_biras = int