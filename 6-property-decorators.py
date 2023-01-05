class Personel:

    zam_orani = 1.05

    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim.title()
        self.maas = maas
        # self.eposta = f'{isim.lower()}.{soyisim.lower()}@firmaadi.com'.replace(' ', '-')
        # print(f"Yeni personel tanımlamdı {self.isim} {self.soyisim}")

    @property
    def eposta(self):
        return f'{self.isim.lower()}.{self.soyisim.lower()}@firmaadi.com'.replace(' ', '-')

    @property
    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'

    @tam_isim.setter
    def tam_isim(self, ad):
        tamAd = ad.split(' ')
        self.isim=""
        i=1
        for Ad in tamAd:
            if i==1:
                self.isim += Ad
                i += 1
            elif i!=len(tamAd):
                self.isim += " "+Ad
                i += 1
            else:
                self.soyisim = Ad

    @tam_isim.deleter
    def tam_isim(self):
        print("Değişkenler Silindi")
        self.isim = None
        self.soyisim = None




per_1 = Personel('fohn albert', 'smith', 28000)

per_1.isim="john albert"

per_1.tam_isim = "hans bremen olive lotus"

print(per_1.isim)

print(per_1.tam_isim)

print(per_1.eposta)

del per_1.tam_isim

print(per_1.isim)

