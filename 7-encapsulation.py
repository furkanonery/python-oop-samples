class Personel:

    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title() # GLOBAL
        self.soyisim = soyisim.title()
        self.maas = maas
        self.__zam_orani = 1.05 # PRIVATE

    def zam_uygula(self):
        self.maas = int(self.maas * self.__zam_orani)

    def __getZamOrani(self): # PRIVATE
        return self.__zam_orani 


per_1 = Personel('john albert', 'smith', 28000)