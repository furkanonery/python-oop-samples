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


class Yazilimci(Personel):
    zam_orani = 1.15

    def __init__(self, isim, soyisim, maas, prog_dili):
        super().__init__(isim, soyisim, maas)
        self.prog_dili = prog_dili
        # print(f"Yeni yazılımcı personel tanımlamdı {self.isim} {self.soyisim}")


class Mudur(Personel):
    def __init__(self, isim, soyisim, maas, persons=None):
        super().__init__(isim, soyisim, maas)
        if persons == None:
            self.persons = []
        else:
            self.persons = persons
        # print(f"Yeni müdür personel tanımlamdı {self.isim} {self.soyisim}")

    def personel_ekle(self, per):
        if per not in self.persons:
            self.persons.append(per)

    def personel_cikar(self, per):
        if per in self.persons:
            self.persons.remove(per)

    def personel_listele(self):
        for e, per in enumerate(self.persons):
            e+=1
            print(e, per.eposta)


yaz_1 = Yazilimci('john albert', 'smith', 28000, 'Python')
yaz_2 = Yazilimci('martha', 'smith', 27000, 'Java')
yaz_3 = Yazilimci('daniel', 'edge', 27000, 'C#')

mudur_1 = Mudur('John', 'Wick', 50000, [yaz_1, yaz_2])
mudur_2 = Mudur('jenny', 'larson', 50000)

# print(yaz_1.maas)
# yaz_1.zam_uygula()
# print(yaz_1.maas)


# print(yaz_1.eposta)
# print(yaz_1.prog_dili)

mudur_2.personel_ekle(yaz_3)

mudur_1.personel_listele()
# mudur_2.personelListele()
mudur_1.personel_cikar(yaz_1)
mudur_1.personel_listele()

print(isinstance(yaz_1,Personel))
print(isinstance(yaz_1,Yazilimci))
print(isinstance(yaz_1,Mudur))

print(issubclass(Mudur,Personel))
print(issubclass(Mudur,Yazilimci))
print(issubclass(Yazilimci,Personel))


