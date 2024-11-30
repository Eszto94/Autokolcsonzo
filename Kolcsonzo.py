from Autokolcsonzo import Autokolcsonzo
from Teherauto import Teherauto
from Szemelyauto import Szemelyauto
from Berles import Berles
from datetime import date

class Kolcsonzo:
    def __init__(self):
        self._kolcsonzo = Autokolcsonzo ("Cars")
        self._berlesek = Berles(0,0,0)
        self._init_auto()
        self._init_berles()

    def _init_auto(self):
        self._kolcsonzo.autok = Szemelyauto("ABC123", "kombi", 10000)
        self._kolcsonzo.autok = Szemelyauto("ABGH456", "SUV", 15000)
        self._kolcsonzo.autok = Teherauto("GRE456", "könnyű", 30000)

    def _init_berles(self):
        self._berlesek.berlesek = Berles(date.fromisoformat("2024-12-03"), "GRE456","546154TA")
        self._berlesek.berlesek = Berles(date.fromisoformat("2024-12-05"), "ABGH456", "457856JK")
        self._berlesek.berlesek = Berles(date.fromisoformat("2024-12-06"), "ABGH456", "457856JK")
        self._berlesek.berlesek = Berles(date.fromisoformat("2024-12-03"), "ABC123", "457856JK")

    def user_interact(self):
        while True:
            print("1. Autó foglalása")
            print("2, Bérlés lemondása")
            print("3. Bérlések listázása")
            print("4. Kilépés")

            choice = input("Válasz a fenti menüpontok közül: ")

            if choice == "1":

                rendszam = 0
                vizsgalo = True
                while (vizsgalo):
                    rendszam = input("Add meg a rendszámot: ")
                    for ellenorzes in self._kolcsonzo._autok:
                        if (rendszam == ellenorzes.rendszam):
                            vizsgalo = False

                    if (vizsgalo):
                        print("Nem létező rendszám, kérjük, adjon meg létezőt!")
                        self._kolcsonzo.autok

                datum = 0
                vizsgalo = True
                kolcsonozve = False
                while (vizsgalo):
                    try:
                        datum = date.fromisoformat(input("Add meg az évet, hónapot, napot kötőjellel elválasztva: "))

                        today = date.today()
                        if(today > datum):
                            print("A dátum múltbeli")

                        else:
                            if(vizsgalo):
                                for ellenorzes in self._berlesek._berlesek:
                                    if (rendszam == ellenorzes.rendszam) and (datum == ellenorzes.datum):
                                        kolcsonozve = True
                                        break

                                if (kolcsonozve):
                                    print("Ezen a napon az autó már kölcsönözve van, kérjük válasszon másik napot!")
                                    kolcsonozve = False

                                else:
                                    vizsgalo = False

                    except ValueError:
                        print("Hibás formátum")


                igszam = input("Add meg a igazolvány számodat: ")
                self._berlesek.berlesek = Berles(datum, rendszam, igszam)

                self._kolcsonzo.berleti_kiiras(rendszam)

            elif choice == "2":

                if(self._berlesek._berlesek.__len__() == 0):
                    print("Nincs már lemondható bérlés")


                else:

                    rendszam = 0
                    vizsgalo = True
                    while (vizsgalo):
                        rendszam = input("Add meg a rendszámot: ")
                        for ellenorzes in self._berlesek._berlesek:
                            if (rendszam == ellenorzes.rendszam):
                                vizsgalo = False

                        if (vizsgalo):
                            print("Nem létező rendszám, kérjük, adjon meg létezőt!")
                            self._berlesek.berlesek

                    datum = 0
                    vizsgalo = True
                    kolcsonozve = True

                    while (vizsgalo):
                        try:
                            datum = date.fromisoformat(input("Add meg az évet, hónapot, napot kötőjellel elválasztva: "))
                            sor_szam = -1
                            if (vizsgalo):
                                for ellenorzes in self._berlesek._berlesek:
                                    sor_szam = sor_szam + 1
                                    if (rendszam == ellenorzes.rendszam) and (datum == ellenorzes.datum):
                                        kolcsonozve = False
                                        self._berlesek._berlesek.pop(sor_szam)
                                        break

                                if (kolcsonozve):
                                    print("Ezen a napon nincs kölcsönözve az autó!")
                                    kolcsonozve = True

                                else:
                                    vizsgalo = False

                        except ValueError:
                            print("Hibás formátum")


            elif choice == "3":
                self._berlesek.berlesek


            elif choice == "4":
                break

            else:
                print("NEM VÁLASZTOTT MENÜPONTOT!")