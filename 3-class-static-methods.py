class Personel:

    personel_sayisi = 0
    zam_orani = 1.05

    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f'{isim.lower()}.{soyisim.lower()}@firmaadi.com'.replace(' ','-')
        Personel.personel_sayisi += 1

    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'

    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)

    @classmethod
    def zam_oranini_belirle(cls, zam_orani):
        cls.zam_orani = zam_orani

    @classmethod
    def from_string(cls, per_str):
        isim, soyisim, maas = per_str.split('-')
        return cls(isim, soyisim, maas)

    @staticmethod
    def mesai_gunu(gun):
        if gun.weekday() == 5 or gun.weekday() == 6:
            return 'Hafta Sonu'
        else:
            return 'Hafta İçi'

from datetime import datetime

tarih = datetime(2023,1,3)
print(tarih.day)
print(Personel.mesai_gunu(tarih))

per_str_4 = 'sam-winchester-40000'
per_str_5 = 'amy-winchester-42000'

per_4 = Personel.from_string(per_str_4)
per_5 = Personel.from_string(per_str_5)

# print(per_4.isim)


per_1 = Personel(isim='john albert', soyisim='smith', maas=28000)
per_2 = Personel('martha', 'smith', 27000)
per_3 = Personel('test', 'user', 1000)

print(per_1.eposta)

# print(Personel.zam_orani)
# print(per_1.zam_orani)

# Personel.zam_oranini_belirle(1.10)

# print(Personel.zam_orani)
# print(per_1.zam_orani)


