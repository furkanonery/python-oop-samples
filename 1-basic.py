class Personel:
    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas
        self.eposta = f'{isim.lower()}.{soyisim.lower()}@firmaadi.com'

    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'

per_1 = Personel(isim='john', soyisim='smith', maas=28000)
per_2 = Personel('martha','smith',27000)

print(per_1.tam_isim())
# Aynı işlevi görüyorlar
print(Personel.tam_isim(per_1))


# print(per_1.isim)
# print(per_1.soyisim)
# print(per_1.maas)
# print(per_1.eposta)

# print(per_2.isim)
# print(per_2.soyisim)
# print(per_2.maas)
# print(per_2.eposta)
