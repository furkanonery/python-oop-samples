class Personel:

    zam_orani = 1.05

    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f'{isim.lower()}.{soyisim.lower()}@firmaadi.com'.replace(' ', '-')
        # print(f"Yeni personel tanımlamdı {self.isim} {self.soyisim}")

    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'

    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)

    def __repr__(self):
        return f"Personel('{self.isim}','{self.soyisim}',{self.maas})"

    def __str__(self):
        return f"{self.tam_isim()} - {self.eposta}"

    def __add__(self,other):
        return self.maas + other.maas

    def __len__(self):
        return len(self.tam_isim())



per_1 = Personel('john albert','smith',28000)
per_2 = Personel('martha', 'smith', 27000)

print(len(per_1))
