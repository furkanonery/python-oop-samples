class Personel:

    personel_sayisi = 0
    zam_orani = 1.05

    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f'{isim.lower()}.{soyisim.lower()}@firmaadi.com'
        Personel.personel_sayisi += 1

    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'

    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)


per_1 = Personel(isim='john', soyisim='smith', maas=28000)
per_2 = Personel('martha','smith',27000)
per_3 = Personel('test','user',1000)

print(Personel.personel_sayisi)

print(per_1.maas)
per_1.zam_uygula()
print(per_1.maas)

# from pprint import pprint

# pprint(per_1.__dict__)
# per_1.zam_orani=1.10
# pprint(per_1.__dict__)

