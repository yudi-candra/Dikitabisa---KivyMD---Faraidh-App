from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivymd.theming import ThemeManager
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (412, 767)

class ImageButton(ButtonBehavior, Image):
    pass

class HomeScreen(Screen):
    pass
class MenuScreen(Screen):
    pass
class DeskripsiScreen(Screen):
    pass
class CalculateScreen(Screen):
    def tampilkan(self):
        print(daftarhasil)
        hasil = '\n\n'.join(str(var) for var in daftarhasil)
        self.manager.screens[4].ids.hasil.text = hasil
           
class ResultScreen(Screen):
    def hapuslist(self):
        daftarhasil.clear()
        print(daftarhasil)

texthasil = None
#variabel penting
lk = 0
pr = 0
suami = 0
istri = 0
harta = 0

peninggalan1 = {
    "ayah": 1 / 3,
    "ibu": 1 / 3,
    "anakL": 1,
    "anakP": 1 / 3,
    "sLseibu": 1 / 6,
    "sPseibu" : 1/2,
    "spseayah": 1 / 2,
    "sLseayah": 1,
    "cucu": "sisa",
    "suami": 1 / 2,
    "istri": 1 / 4
}

peninggalan2 = {
    "ayah": 1 / 6,
    "ibu": 1 / 6,
    "anakL": 1,
    "anakP": 2 / 3,
    "sLseibu": 1 / 3,
    "sPseibu" : 1,
    "spseayah": 2 / 3,
    "sLseayah": 4 / 3,
    "cucu": 1,
    "suami": 1 / 4,
    "istri": 1 / 8
}

daftarhasil = []

def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

def hitung_harta(sum, who, harta):
    hasil = (int(harta)*who)/int(sum)
    print(hasil)
    return hasil

def hitung_harta2(sum, who, harta):
    hasil = (int(harta)*who)/int(sum)
    print(hasil)
    return hasil

def label_hasil(harta, who):
    global texthasil
    texthasil = f"Bagian {who} : Rp. {int(harta)} / Orang"
    daftarhasil.append(texthasil)

class MainApp(MDApp):
    
    def build(self):
        theme_cls = ThemeManager()
        
        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.accent_pallete = "LightGreen"
        self.theme_cls.theme_style = "Light"
        
        switch = ScreenManager()
        switch.add_widget(HomeScreen(name='home'))
        switch.add_widget(MenuScreen(name='menu'))
        switch.add_widget(MenuScreen(name='deskripsi'))
        switch.add_widget(MenuScreen(name='calculate'))
        switch.add_widget(MenuScreen(name='result'))
        return Builder.load_file('App.kv')

    
    def opsi(self, jumlahharta, anaklk, anakpr, varayah, varibu, varsuami, varistri, varcucu, varsla, varsli, varspa, varspi):
        harta = jumlahharta
        lk = anaklk
        pr = anakpr
        ayah = varayah
        ibu = varibu
        suami = varsuami
        istri = varistri
        cucu = varcucu
        sLa = varsla
        sLi = varsli
        spa = varspa
        spi = varspi

        if len(ayah)!=0 and len(ibu)!=0 and len(suami)!=0 and len(istri)!=0:
            if len(lk) == 0 and len(pr) == 0:
                if len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    if len(cucu) == 0:
                        bagian1 = peninggalan1.get("istri")
                        bagian2 = peninggalan1.get("suami")
                        bagian3 = peninggalan1.get("ayah")
                        bagian4 = peninggalan1.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = 1/3
                        hartaayah = 1/6

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaayah, "Ayah")
                        hasil = label_hasil(hartaibu, "ibu")

                    else:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")
                        bagian3 = peninggalan2.get("ayah")
                        bagian4 = peninggalan2.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = hitung_harta(ibu, bagian4, harta)
                        hartaayah = hitung_harta(ayah, bagian3, harta)
                        hartacucu = int(harta) - (
                                    (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                                        hartaayah * int(ayah)))

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaayah, "Ayah")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartacucu, "cucu")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaslki = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                                hartaayah * int(ayah))) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaslki = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                                hartaayah * int(ayah))) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaslki = int(harta) - (
                            (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                            hartaayah * int(ayah))) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                    hasil = label_hasil("terhalang", "Saudara perempuan seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaspr = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                                hartaayah * int(ayah))) / int(spi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaspr, "Saudara kandung Perempuan")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaspri = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                                hartaayah * int(ayah))) / int(spi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaspri = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                                hartaayah * int(ayah))) / int(spi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("Terhalang", "Saudara Perempuan seayah")


                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                                hartaayah * int(ayah)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                                hartaayah * int(ayah)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                                hartaayah * int(ayah)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    sisa = int(harta) - (
                            (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                            hartaayah * int(ayah)))

                    hartaspri = (sisa / 3) * int(spi)
                    hartaslki = ((sisa / 3) * 2) * int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaslka = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                                hartaayah * int(ayah))) / int(sLa)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaspra = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                                hartaayah * int(ayah))) / int(spa)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                                hartaayah * int(ayah)))

                    hartaspra = (sisa / 3) / int(spa)
                    hartaslka = ((sisa / 3) * 2) / int(sLa)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")

            elif len(lk) != 0 and len(pr) == 0:
                bagian1 = peninggalan2.get("istri")
                bagian2 = peninggalan2.get("suami")
                bagian3 = peninggalan2.get("ayah")
                bagian4 = peninggalan2.get("ibu")

                hartaistri = hitung_harta(istri, bagian1, harta)
                hartasuami = hitung_harta(suami, bagian2, harta)
                hartaibu = hitung_harta(ibu, bagian4, harta)
                hartaayah = hitung_harta(ayah, bagian3, harta)
                hartalk = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                            hartaayah * int(ayah))) / int(lk)

                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartaayah, "Ayah")
                hasil = label_hasil(hartaibu, "ibu")
                hasil = label_hasil(hartalk, "anak laki-laki")

            elif len(lk) == 0 and len(pr) != 0:
                bagian1 = peninggalan2.get("istri")
                bagian2 = peninggalan2.get("suami")
                bagian3 = peninggalan2.get("ayah")
                bagian4 = peninggalan2.get("ibu")

                hartaistri = hitung_harta(istri, bagian1, harta)
                hartasuami = hitung_harta(suami, bagian2, harta)
                hartaibu = hitung_harta(ibu, bagian4, harta)
                hartaayah = hitung_harta(ayah, bagian3, harta)
                sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                            hartaayah * int(ayah)))

                hartasuami = sisa / 3 * 2
                hartapr = (sisa / 3) / int(pr)

                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartaayah, "Ayah")
                hasil = label_hasil(hartaibu, "ibu")
                hasil = label_hasil(hartapr, "anak Perempuan")

            elif len(lk) != 0 and len(pr) != 0:
                bagian1 = peninggalan2.get("istri")
                bagian2 = peninggalan2.get("suami")
                bagian3 = peninggalan2.get("ayah")
                bagian4 = peninggalan2.get("ibu")

                hartaistri = hitung_harta(istri, bagian1, harta)
                hartasuami = hitung_harta(suami, bagian2, harta)
                hartaibu = hitung_harta(ibu, bagian4, harta)
                hartaayah = hitung_harta(ayah, bagian3, harta)
                sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)) + (
                        hartaayah * int(ayah)))

                hartapr = (sisa / 3) / int(pr)
                hartalk = (sisa - hartapr) / int(lk)

                print(hartasuami)
                print(hartaistri)
                print(hartalk)
                print(hartapr)

                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartaayah, "Ayah")
                hasil = label_hasil(hartaibu, "ibu")
                hasil = label_hasil(hartalk, "anak Laki-laki")
                hasil = label_hasil(hartapr, "anak Perempuan")

        elif len(ayah) != 0 and len(ibu) == 0 and len(suami) == 0 and len(istri) == 0:
            if len(lk) == 0 and len(pr) == 0:
                if len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    if len(cucu) == 0:
                        bagian = int(harta)
                        text1 = f"Bagian ayah  : {bagian} / Orang"
                        daftarhasil.append(text1)
                        
                    else:
                        bagian1 = peninggalan2.get("ayah")
                        hartaistri = hitung_harta(ayah, bagian1, harta)
                        hartacucu = (int(harta) - (hartaistri * int(ayah))) / int(cucu)

                        hasil = label_hasil(int(hartaistri), "ayah")
                        hasil = label_hasil(hartacucu, "Cucu")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ayah")
                    hartaayah = hitung_harta(ayah, bagian1, harta)
                    hartaslki = (int(harta) - (hartaayah * int(ayah))) / int(sLi)

                    hasil = label_hasil(int(hartaayah), "ayah")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ayah")
                    hartaayah = hitung_harta(ayah, bagian1, harta)
                    hartaslki = (int(harta) - (hartaayah * int(ayah))) / int(sLi)

                    hasil = label_hasil(int(hartaayah), "ayah")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ayah")
                    hartaayah = hitung_harta(ayah, bagian1, harta)
                    hartaslki = (int(harta) - (hartaayah * int(ayah))) / int(sLi)

                    hasil = label_hasil(int(hartaayah), "ayah")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ayah")
                    hartaayah = hitung_harta(ayah, bagian1, harta)
                    hartaspri = (int(harta) - (hartaayah * int(ayah))) / int(spi)

                    hasil = label_hasil(int(hartaayah), "ayah")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ayah")
                    hartaayah = hitung_harta(ayah, bagian1, harta)
                    hartaspri = (int(harta) - (hartaayah * int(ayah))) / int(spi)

                    hasil = label_hasil(int(hartaayah), "ayah")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ayah")
                    hartaayah = hitung_harta(ayah, bagian1, harta)
                    hartaspri = (int(harta) - (hartaayah * int(ayah))) / int(spi)

                    hasil = label_hasil(int(hartaayah), "ayah")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")


                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ayah")
                    hartaayah = hitung_harta(ayah, bagian1, harta)
                    sisa = (int(harta) - (hartaayah * int(ayah))) / int(spi)

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(int(hartaayah), "ayah")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ayah")
                    hartaayah = hitung_harta(ayah, bagian1, harta)
                    sisa = (int(harta) - (hartaayah * int(ayah))) / int(spi)

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(int(hartaayah), "ayah")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ayah")
                    hartaayah = hitung_harta(ayah, bagian1, harta)
                    sisa = (int(harta) - (hartaayah * int(ayah))) / int(spi)

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(int(hartaayah), "ayah")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ayah")
                    hartaayah = hitung_harta(ayah, bagian1, harta)
                    sisa = (int(harta) - (hartaayah * int(ayah))) / int(spi)

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(int(hartaayah), "ayah")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ayah")
                    hartaayah = hitung_harta(ayah, bagian1, harta)
                    hartaslka = (int(harta) - (hartaayah * int(ayah))) / int(sLa)

                    hasil = label_hasil(int(hartaayah), "ayah")
                    hasil = label_hasil(hartaslka, "Saudara Laki-Laki Seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ayah")
                    hartaayah = hitung_harta(ayah, bagian1, harta)
                    hartaspra = (int(harta) - (hartaayah * int(ayah))) / int(spa)

                    hasil = label_hasil(int(hartaayah), "ayah")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan Seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ayah")
                    hartaayah = hitung_harta(ayah, bagian1, harta)
                    sisa = (int(harta) - (hartaayah * int(ayah))) / int(spi)

                    hartaspra = (sisa / 3) / int(spi)
                    hartaslka = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(int(hartaayah), "ayah")
                    hasil = label_hasil(hartaslka, "Saudara Laki-Laki seayah")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")


            elif len(lk) != 0 and len(pr) == 0:

                bagian2 = peninggalan2.get("ayah")
                hartaayah = hitung_harta(1, bagian2, harta)

                hartalk = (int(harta) - (hartaayah)) / int(lk)

                hasil = label_hasil(hartaayah, "ayah")
                hasil = label_hasil(hartalk, "anak Laki-laki")

            elif len(lk) == 0 and len(pr) != 0:
                bagian2 = peninggalan2.get("ayah")
                hartaayah = hitung_harta(1, bagian2, harta)

                hartapr = (int(harta) - (hartaayah)) / int(lk)

                hasil = label_hasil(hartaayah, "ayah")
                hasil = label_hasil(hartapr, "anak Perempuan")

            else:
                bagian2 = peninggalan2.get("ayah")
                hartaayah = hitung_harta(1, bagian2, harta)

                sisa = (int(harta) - (hartaayah))

                hartapr = (sisa / 3) / int(pr)
                hartalk = (sisa / 3 * 2) / int(lk)

                hasil = label_hasil(hartaayah, "ayah")
                hasil = label_hasil(hartalk, "anak Laki-laki")
                hasil = label_hasil(hartapr, "anak Perempuan")

        elif len(ayah) != 0 and len(ibu) != 0 and len(suami) == 0 and len(istri) == 0:
            if len(lk) == 0 and len(pr) == 0:
                if len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    if len(cucu) == 0:
                        bagian1 = peninggalan1.get("ibu")
                        bagian2 = peninggalan1.get("ayah")

                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        hartaayah = int(harta) - (hartaibu * int(ibu))

                        hasil = label_hasil(hartaayah, "ayah")
                        hasil = label_hasil(hartaibu, "ibu")
                    else:
                        bagian1 = peninggalan2.get("ibu")
                        bagian2 = peninggalan2.get("ayah")

                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        hartaayah = hitung_harta(ayah, bagian2, harta)
                        hartacucu = int(harta) - (hartaayah + (hartaibu * int(ibu))) / int(cucu)

                        hasil = label_hasil(hartaayah, "ayah")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartacucu, "cucu")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("ayah")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaslki = int(harta) - (hartaayah + (hartaibu * int(ibu))) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("ayah")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaslki = int(harta) - (hartaayah + (hartaibu * int(ibu))) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("ayah")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaslki = int(harta) - (hartaayah + (hartaibu * int(ibu))) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                    hasil = label_hasil("terhalang", "Saudara perempuan seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("ayah")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaspri = int(harta) - (hartaayah + (hartaibu * int(ibu))) / int(spi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("ayah")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaspri = int(harta) - (hartaayah + (hartaibu * int(ibu))) / int(spi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("ayah")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaspri = int(harta) - (hartaayah + (hartaibu * int(ibu))) / int(spi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("Terhalang", "Saudara Perempuan seayah")


                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("ayah")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartaibu * int(ibu)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("ayah")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartaibu * int(ibu)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("ayah")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartaibu * int(ibu)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("ayah")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartaibu * int(ibu)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("ayah")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaslka = int(harta) - (hartaayah + (hartaibu * int(ibu))) / int(sLa)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("ayah")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaspra = int(harta) - (hartaayah + (hartaibu * int(ibu))) / int(spa)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seibu")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("ayah")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartaibu * int(ibu)))

                    hartaspra = (sisa / 3) / int(spa)
                    hartaslka = ((sisa / 3) * 2) / int(sLa)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslka, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan Kandung")

            elif len(lk) != 0 and len(pr) == 0:
                a = 4
                b = 8
                print("The L.C.M. is", compute_lcm(a, b))
                kpk = compute_lcm(a, b)
                bagian1 = peninggalan2.get("ibu")
                bagian2 = peninggalan2.get("ayah")
                hartaibu = hitung_harta(ibu, bagian1, harta)
                hartaayah = hitung_harta(ayah, bagian2, harta)
                hartalk = (int(harta) - (hartaibu + hartaayah)) / int(lk)

                hasil = label_hasil(hartaayah, "ayah")
                hasil = label_hasil(hartaibu, "ibu")
                hasil = label_hasil(hartalk, "anak laki-laki")

            elif len(lk) == 0 and len(pr) != 0:
                a = 4
                b = 8
                print("The L.C.M. is", compute_lcm(a, b))
                kpk = compute_lcm(a, b)
                bagian1 = peninggalan2.get("ibu")
                hartaibu = hitung_harta(ibu, bagian1, harta)
                sisa = int(harta) - hartaibu
                hartaayah = sisa / 3 * 2
                hartapr = (sisa / 3) / int(pr)

                hasil = label_hasil(hartaibu, "ibu")
                hasil = label_hasil(hartaayah, "ayah")
                hasil = label_hasil(hartapr, "anak Perempuan")

            elif len(lk) != 0 and len(pr) != 0:
                bagian1 = peninggalan2.get("ayah")
                bagian2 = peninggalan2.get("ibu")

                hartaayah = hitung_harta(1, bagian1, harta)
                hartaibu = hitung_harta(ibu, bagian2, harta)

                sisa = int(harta) - (hartaayah + hartaibu)

                hartapr = (sisa / 3) / int(pr)
                hartalk = (sisa - hartapr) / int(lk)

                print(hartaayah)
                print(hartaibu)
                print(hartalk)
                print(hartapr)

                hasil = label_hasil(hartaibu, "ibu")
                hasil = label_hasil(hartaayah, "ayah")
                hasil = label_hasil(hartalk, "anak Laki-laki")
                hasil = label_hasil(hartapr, "anak Perempuan")

        elif len(ayah) != 0 and len(ibu) == 0 and len(suami) != 0 and len(istri) == 0:
            if len(lk) == 0 and len(pr) == 0:
                if len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    if len(cucu) == 0:
                        bagian1 = peninggalan1.get("suami")
                        bagian2 = peninggalan1.get("ayah")

                        hartasuami = hitung_harta(suami, bagian1, harta)
                        hartaayah = int(harta) - (hartasuami * int(suami))

                        hasil = label_hasil(hartaayah, "ayah")
                        hasil = label_hasil(hartasuami, "suami")
                    else:
                        bagian1 = peninggalan2.get("suami")
                        bagian2 = peninggalan2.get("ayah")

                        hartasuami = hitung_harta(suami, bagian1, harta)
                        hartaayah = hitung_harta(ayah, bagian2, harta)
                        hartacucu = int(harta) - (hartaayah + (hartasuami * int(suami))) / int(cucu)

                        hasil = label_hasil(hartaayah, "ayah")
                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartacucu, "cucu")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("suami")
                    bagian2 = peninggalan2.get("ayah")

                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaslki = int(harta) - (hartaayah + (hartasuami * int(suami))) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("suami")
                    bagian2 = peninggalan2.get("ayah")

                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaslki = int(harta) - (hartaayah + (hartasuami * int(suami))) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("suami")
                    bagian2 = peninggalan2.get("ayah")

                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaslki = int(harta) - (hartaayah + (hartasuami * int(suami))) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                    hasil = label_hasil("terhalang", "Saudara perempuan seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("suami")
                    bagian2 = peninggalan2.get("ayah")

                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaspri = int(harta) - (hartaayah + (hartasuami * int(suami))) / int(spi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("suami")
                    bagian2 = peninggalan2.get("ayah")

                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaspri = int(harta) - (hartaayah + (hartasuami * int(suami))) / int(spi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("suami")
                    bagian2 = peninggalan2.get("ayah")

                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaspri = int(harta) - (hartaayah + (hartasuami * int(suami))) / int(spi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("Terhalang", "Saudara Perempuan seayah")


                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("suami")
                    bagian2 = peninggalan2.get("ayah")

                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartasuami * int(suami)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("suami")
                    bagian2 = peninggalan2.get("ayah")

                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartasuami * int(suami)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("suami")
                    bagian2 = peninggalan2.get("ayah")

                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartasuami * int(suami)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("suami")
                    bagian2 = peninggalan2.get("ayah")

                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartasuami * int(suami)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("suami")
                    bagian2 = peninggalan2.get("ayah")

                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaslka = int(harta) - (hartaayah + (hartasuami * int(suami))) / int(sLa)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("suami")
                    bagian2 = peninggalan2.get("ayah")

                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaspra = int(harta) - (hartaayah + (hartasuami * int(suami))) / int(spa)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seibu")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("suami")
                    bagian2 = peninggalan2.get("ayah")

                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartasuami * int(suami)))

                    hartaspra = (sisa / 3) / int(spa)
                    hartaslka = ((sisa / 3) * 2) / int(sLa)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaslka, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan Kandung")

            elif len(lk) != 0 and len(pr) == 0:
                a = 4
                b = 8
                print("The L.C.M. is", compute_lcm(a, b))
                kpk = compute_lcm(a, b)
                bagian1 = peninggalan2.get("suami")
                bagian2 = peninggalan2.get("ayah")
                hartasuami = hitung_harta(suami, bagian1, harta)
                hartaayah = hitung_harta(ayah, bagian2, harta)
                hartalk = (int(harta) - (hartasuami + hartaayah)) / int(lk)

                hasil = label_hasil(hartaayah, "ayah")
                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartalk, "anak laki-laki")

            elif len(lk) == 0 and len(pr) != 0:
                a = 4
                b = 8
                print("The L.C.M. is", compute_lcm(a, b))
                kpk = compute_lcm(a, b)
                bagian1 = peninggalan2.get("suami")
                hartasuami = hitung_harta(suami, bagian1, harta)
                sisa = int(harta) - hartasuami
                hartaayah = sisa / 3 * 2
                hartapr = (sisa / 3) / int(pr)

                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartaayah, "ayah")
                hasil = label_hasil(hartapr, "anak Perempuan")

            elif len(lk) != 0 and len(pr) != 0:
                bagian1 = peninggalan2.get("ayah")
                bagian2 = peninggalan2.get("suami")

                hartaayah = hitung_harta(1, bagian1, harta)
                hartasuami = hitung_harta(suami, bagian2, harta)

                sisa = int(harta) - (hartaayah + hartasuami)

                hartapr = (sisa / 3) / int(pr)
                hartalk = (sisa - hartapr) / int(lk)

                print(hartaayah)
                print(hartasuami)
                print(hartalk)
                print(hartapr)

                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartaayah, "ayah")
                hasil = label_hasil(hartalk, "anak Laki-laki")
                hasil = label_hasil(hartapr, "anak Perempuan")

        elif len(ayah) != 0 and len(ibu) == 0 and len(suami) == 0 and len(istri) != 0:
            if len(lk) == 0 and len(pr) == 0:
                if len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    if len(cucu) == 0:
                        bagian1 = peninggalan1.get("istri")
                        bagian2 = peninggalan1.get("ayah")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartaayah = int(harta) - (hartaistri * int(istri))

                        hasil = label_hasil(hartaayah, "ayah")
                        hasil = label_hasil(hartaistri, "istri")
                    else:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("ayah")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartaayah = hitung_harta(ayah, bagian2, harta)
                        hartacucu = int(harta) - (hartaayah + (hartaistri * int(istri))) / int(cucu)

                        hasil = label_hasil(hartaayah, "ayah")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartacucu, "cucu")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaslki = int(harta) - (hartaayah + (hartaistri * int(istri))) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    shartaslkiisa = int(harta) - (hartaayah + (hartaistri * int(istri))) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaslki = int(harta) - (hartaayah + (hartaistri * int(istri))) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                    hasil = label_hasil("terhalang", "Saudara perempuan seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaspri = int(harta) - (hartaayah + (hartaistri * int(istri))) / int(spi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaspri = int(harta) - (hartaayah + (hartaistri * int(istri))) / int(spi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaspri = int(harta) - (hartaayah + (hartaistri * int(istri))) / int(spi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("Terhalang", "Saudara Perempuan seayah")


                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartaistri * int(istri)))

                    hartaspri = (sisa / 3) * int(spi)
                    hartaslki = ((sisa / 3) * 2) * int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartaistri * int(istri)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartaistri * int(istri)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartaistri * int(istri)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaslka = int(harta) - (hartaayah + (hartaistri * int(istri))) / int(sLa)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    hartaspra = int(harta) - (hartaayah + (hartaistri * int(istri))) / int(spa)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seistri")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaayah = hitung_harta(ayah, bagian2, harta)
                    sisa = int(harta) - (hartaayah + (hartaistri * int(istri)))

                    hartaspra = (sisa / 3) / int(spa)
                    hartaslka = ((sisa / 3) * 2) / int(sLa)

                    hasil = label_hasil(hartaayah, "ayah")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslka, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan Kandung")

            elif len(lk) != 0 and len(pr) == 0:
                a = 4
                b = 8
                print("The L.C.M. is", compute_lcm(a, b))
                kpk = compute_lcm(a, b)
                bagian1 = peninggalan2.get("istri")
                bagian2 = peninggalan2.get("ayah")
                hartaistri = hitung_harta(istri, bagian1, harta)
                hartaayah = hitung_harta(ayah, bagian2, harta)
                hartalk = (int(harta) - (hartaistri + hartaayah)) / int(lk)

                hasil = label_hasil(hartaayah, "ayah")
                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartalk, "anak laki-laki")

            elif len(lk) == 0 and len(pr) != 0:
                a = 4
                b = 8
                print("The L.C.M. is", compute_lcm(a, b))
                kpk = compute_lcm(a, b)
                bagian1 = peninggalan2.get("istri")
                hartaistri = hitung_harta(istri, bagian1, harta)
                sisa = int(harta) - hartaistri
                hartaayah = sisa / 3 * 2
                hartapr = (sisa / 3) / int(pr)

                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartaayah, "ayah")
                hasil = label_hasil(hartapr, "anak Perempuan")

            elif len(lk) != 0 and len(pr) != 0:
                bagian1 = peninggalan2.get("ayah")
                bagian2 = peninggalan2.get("istri")

                hartaayah = hitung_harta(1, bagian1, harta)
                hartaistri = hitung_harta(istri, bagian2, harta)

                sisa = int(harta) - (hartaayah + hartaistri)

                hartapr = (sisa / 3) / int(pr)
                hartalk = (sisa - hartapr) / int(lk)

                print(hartaayah)
                print(hartaistri)
                print(hartalk)
                print(hartapr)

                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartaayah, "ayah")
                hasil = label_hasil(hartalk, "anak Laki-laki")
                hasil = label_hasil(hartapr, "anak Perempuan")

        elif len(ayah) != 0 and len(ibu) == 0 and len(suami) != 0 and len(istri) != 0:
            if len(lk) == 0 and len(pr) == 0:
                if len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    if len(cucu) == 0:
                        bagian1 = peninggalan1.get("istri")
                        bagian2 = peninggalan1.get("suami")
                        bagian3 = peninggalan1.get("ayah")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaayah = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)))

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaayah, "Ayah")

                    else:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")
                        bagian3 = peninggalan2.get("ayah")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaayah = hitung_harta(ayah, bagian3, harta)
                        hartacucu = int(harta) - (
                                    (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaayah * int(ayah)))

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaayah, "Ayah")
                        hasil = label_hasil(hartacucu, "cucu")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaslki = int(harta) - (
                                (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaayah * int(ayah))) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaslki = int(harta) - (
                                (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaayah * int(ayah))) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)

                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaslki = int(harta) - (
                            (hartaistri * int(istri)) + (hartasuami * int(suami)) + (
                                hartaayah * int(ayah))) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")

                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                    hasil = label_hasil("terhalang", "Saudara perempuan seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)

                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaspr = int(harta) - (
                                (hartaistri * int(istri)) + (hartasuami * int(suami)) + (
                                hartaayah * int(ayah))) / int(spi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")

                    hasil = label_hasil(hartaspr, "Saudara kandung Perempuan")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)

                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaspri = int(harta) - (
                                (hartaistri * int(istri)) + (hartasuami * int(suami)) + (
                                hartaayah * int(ayah))) / int(spi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")

                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)

                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaspri = int(harta) - (
                                (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaayah * int(ibu)) + (
                                hartaayah * int(ayah))) / int(spi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")

                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("Terhalang", "Saudara Perempuan seayah")


                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)

                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (
                            hartaayah * int(ayah)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")

                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)

                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (
                            hartaayah * int(ayah)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")

                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)

                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (
                            hartaayah * int(ayah)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")

                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)

                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    sisa = int(harta) - (
                            (hartaistri * int(istri)) + (hartasuami * int(suami)) + (
                            hartaayah * int(ayah)))

                    hartaspri = (sisa / 3) * int(spi)
                    hartaslki = ((sisa / 3) * 2) * int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")

                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)

                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaslka = int(harta) - (
                                (hartaistri * int(istri)) + (hartasuami * int(suami)) + (
                                hartaayah * int(ayah))) / int(sLa)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")

                    hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)

                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    hartaspra = int(harta) - (
                                (hartaistri * int(istri)) + (hartasuami * int(suami)) + (
                                hartaayah * int(ayah))) / int(spa)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")

                    hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian3 = peninggalan2.get("ayah")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)

                    hartaayah = hitung_harta(ayah, bagian3, harta)
                    sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (
                            hartaayah * int(ayah)))

                    hartaspra = (sisa / 3) / int(spa)
                    hartaslka = ((sisa / 3) * 2) / int(sLa)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaayah, "Ayah")

                    hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")

            elif len(lk) != 0 and len(pr) == 0:
                bagian1 = peninggalan2.get("istri")
                bagian2 = peninggalan2.get("suami")
                bagian3 = peninggalan2.get("ayah")

                hartaistri = hitung_harta(istri, bagian1, harta)
                hartasuami = hitung_harta(suami, bagian2, harta)
                hartaayah = hitung_harta(ayah, bagian3, harta)
                hartalk = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (
                        hartaayah * int(ayah))) / int(lk)

                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartaayah, "Ayah")
                hasil = label_hasil(hartalk, "anak laki-laki")

            elif len(lk) == 0 and len(pr) != 0:
                bagian1 = peninggalan2.get("istri")
                bagian2 = peninggalan2.get("suami")
                bagian3 = peninggalan2.get("ayah")

                hartaistri = hitung_harta(istri, bagian1, harta)
                hartasuami = hitung_harta(suami, bagian2, harta)
                hartaayah = hitung_harta(ayah, bagian3, harta)
                sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaayah * int(ayah)))

                hartasuami = sisa / 3 * 2
                hartapr = (sisa / 3) / int(pr)

                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartaayah, "Ayah")
                hasil = label_hasil(hartapr, "anak Perempuan")

            elif len(lk) != 0 and len(pr) != 0:
                bagian1 = peninggalan2.get("istri")
                bagian2 = peninggalan2.get("suami")
                bagian3 = peninggalan2.get("ayah")

                hartaistri = hitung_harta(istri, bagian1, harta)
                hartasuami = hitung_harta(suami, bagian2, harta)
                hartaayah = hitung_harta(ayah, bagian3, harta)
                sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (
                        hartaayah * int(ayah)))

                hartapr = (sisa / 3) / int(pr)
                hartalk = (sisa - hartapr) / int(lk)

                print(hartasuami)
                print(hartaistri)
                print(hartalk)
                print(hartapr)

                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartaayah, "Ayah")
                hasil = label_hasil(hartalk, "anak Laki-laki")
                hasil = label_hasil(hartapr, "anak Perempuan")

        elif len(ayah) == 0 and len(ibu) != 0 and len(suami) == 0 and len(istri) == 0:
                if len(lk) == 0 and len(pr) == 0 :
                    if len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                        if len(cucu) == 0:
                            bagian = int(harta)
                            textibu = f"Bagian ibu  : {bagian} / Orang"
                            daftarhasil.append(textibu)
                            
                        else:
                            bagian1 = peninggalan2.get("ibu")
                            hartaistri = hitung_harta(ibu, bagian1, harta)
                            hartacucu = (int(harta) - (hartaistri * int(ibu))) / int(cucu)

                            hasil = label_hasil(int(hartaistri), "ibu")
                            hasil = label_hasil(hartacucu, "Cucu")

                    elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                        bagian1 = peninggalan2.get("ibu")
                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        hartaslki = (int(harta) - (hartaibu * int(ibu))) / int(sLi)

                        hasil = label_hasil(int(hartaibu), "ibu")
                        hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")

                    elif len(sLi) != 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                        bagian1 = peninggalan2.get("ibu")
                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        hartaslki = (int(harta) - (hartaibu * int(ibu))) / int(sLi)

                        hasil = label_hasil(int(hartaibu), "ibu")
                        hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")
                        hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                    elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                        bagian1 = peninggalan2.get("ibu")
                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        hartaslki = (int(harta) - (hartaibu * int(ibu))) / int(sLi)

                        hasil = label_hasil(int(hartaibu), "ibu")
                        hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")
                        hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                    elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                        bagian1 = peninggalan2.get("ibu")
                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        hartaspri = (int(harta) - (hartaibu * int(ibu))) / int(spi)

                        hasil = label_hasil(int(hartaibu), "ibu")
                        hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")

                    elif len(sLi) == 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                        bagian1 = peninggalan2.get("ibu")
                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        hartaspri = (int(harta) - (hartaibu * int(ibu))) / int(spi)

                        hasil = label_hasil(int(hartaibu), "ibu")
                        hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                        hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                    elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                        bagian1 = peninggalan2.get("ibu")
                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        hartaspri = (int(harta) - (hartaibu * int(ibu))) / int(spi)

                        hasil = label_hasil(int(hartaibu), "ibu")
                        hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                        hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")


                    elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                        bagian1 = peninggalan2.get("ibu")
                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        sisa = (int(harta) - (hartaibu * int(ibu))) / int(spi)

                        hartaspri = (sisa / 3) /int(spi)
                        hartaslki = ((sisa / 3) * 2) /int(sLi)

                        hasil = label_hasil(int(hartaibu), "ibu")
                        hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                        hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")

                    elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                        bagian1 = peninggalan2.get("ibu")
                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        sisa = (int(harta) - (hartaibu * int(ibu))) / int(spi)

                        hartaspri = (sisa / 3)/int(spi)
                        hartaslki = ((sisa / 3) * 2)/int(sLi)

                        hasil = label_hasil(int(hartaibu), "ibu")
                        hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                        hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                        hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                    elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                        bagian1 = peninggalan2.get("ibu")
                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        sisa = (int(harta) - (hartaibu * int(ibu))) / int(spi)

                        hartaspri = (sisa / 3) / int(spi)
                        hartaslki = ((sisa / 3) * 2) / int(sLi)

                        hasil = label_hasil(int(hartaibu), "ibu")
                        hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                        hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                        hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                    elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) != 0:
                        bagian1 = peninggalan2.get("ibu")
                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        sisa = (int(harta) - (hartaibu * int(ibu))) / int(spi)

                        hartaspri = (sisa / 3) / int(spi)
                        hartaslki = ((sisa / 3) * 2) / int(sLi)

                        hasil = label_hasil(int(hartaibu), "ibu")
                        hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                        hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                        hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")
                        hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                    elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                        bagian1 = peninggalan2.get("ibu")
                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        hartaslka = (int(harta) - (hartaibu * int(ibu))) / int(sLa)

                        hasil = label_hasil(int(hartaibu), "ibu")
                        hasil = label_hasil(hartaslka, "Saudara Laki-Laki seayah")

                    elif len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                        bagian1 = peninggalan2.get("ibu")
                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        hartaspra = (int(harta) - (hartaibu * int(ibu))) / int(spa)

                        hasil = label_hasil(int(hartaibu), "ibu")
                        hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")

                    elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) != 0:
                        bagian1 = peninggalan2.get("ibu")
                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        sisa = (int(harta) - (hartaibu * int(ibu))) / int(spi)

                        hartaspra = (sisa / 3) / int(spi)
                        hartaslka = ((sisa / 3) * 2) / int(sLi)

                        hasil = label_hasil(int(hartaibu), "ibu")
                        hasil = label_hasil(hartaslka, "Saudara Laki-Laki seayah")
                        hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")


                elif len(lk) != 0 and len(pr) == 0:

                    bagian2 = peninggalan2.get("ibu")
                    hartaibu = hitung_harta(1, bagian2, harta)

                    hartalk = (int(harta) - (hartaibu)) / int(lk)

                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartalk, "anak Laki-laki")

                elif len(lk) == 0 and len(pr) != 0:
                    bagian2 = peninggalan2.get("ibu")
                    hartaibu = hitung_harta(1, bagian2, harta)

                    hartapr = (int(harta) - (hartaibu)) / int(lk)

                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartapr, "anak Perempuan")

                else:
                    bagian2 = peninggalan2.get("ibu")
                    hartaibu = hitung_harta(1, bagian2, harta)

                    sisa = (int(harta) - (hartaibu))

                    hartapr = (sisa / 3) / int(pr)
                    hartalk = (sisa / 3 * 2) / int(lk)

                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartalk, "anak Laki-laki")
                    hasil = label_hasil(hartapr, "anak Perempuan")

        elif len(ayah) == 0 and len(ibu) != 0 and len(suami) != 0 and len(istri) == 0:
            if len(lk) == 0 and len(pr) == 0:
                if len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    if len(cucu) == 0:
                        bagian1 = peninggalan1.get("ibu")
                        bagian2 = peninggalan1.get("suami")

                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        hartasuami = int(harta) - (hartaibu * int(ibu))

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaibu, "ibu")
                    else:
                        bagian1 = peninggalan2.get("ibu")
                        bagian2 = peninggalan2.get("suami")

                        hartaibu = hitung_harta(ibu, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartacucu = int(harta) - (hartasuami + (hartaibu * int(ibu))) / int(cucu)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartacucu, "cucu")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("suami")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaslki = int(harta) - (hartasuami + (hartaibu * int(ibu))) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("suami")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaslki = int(harta) - (hartasuami + (hartaibu * int(ibu))) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki sesuami")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("suami")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaslki = int(harta) - (hartasuami + (hartaibu * int(ibu))) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                    hasil = label_hasil("terhalang", "Saudara perempuan sesuami")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("suami")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaspri = int(harta) - (hartasuami + (hartaibu * int(ibu))) / int(spi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("suami")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaspri = int(harta) - (hartasuami + (hartaibu * int(ibu))) / int(spi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki sesuami")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("suami")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaspri = int(harta) - (hartasuami + (hartaibu * int(ibu))) / int(spi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("Terhalang", "Saudara Perempuan sesuami")


                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("suami")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    sisa = int(harta) - (hartasuami + (hartaibu * int(ibu)))

                    hartaspri = (sisa / 3) * int(spi)
                    hartaslki = ((sisa / 3) * 2) * int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("suami")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    sisa = int(harta) - (hartasuami + (hartaibu * int(ibu)))

                    hartaspri = (sisa / 3)/int(spi)
                    hartaslki = ((sisa / 3) * 2) /int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki sesuami")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("suami")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    sisa = int(harta) - (hartasuami + (hartaibu * int(ibu)))

                    hartaspri = (sisa / 3) /int(spi)
                    hartaslki = ((sisa / 3) * 2) /int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Perempuan sesuami")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("suami")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    sisa = int(harta) - (hartasuami + (hartaibu * int(ibu)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki sesuami")
                    hasil = label_hasil("terhalang", "Saudara Perempuan sesuami")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("suami")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaslka = int(harta) - (hartasuami + (hartaibu * int(ibu))) / int(sLa)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslka, "Saudara Laki-laki sesuami")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("suami")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaspra = int(harta) - (hartasuami + (hartaibu * int(ibu))) / int(spa)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seibu")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("ibu")
                    bagian2 = peninggalan2.get("suami")

                    hartaibu = hitung_harta(ibu, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    sisa = int(harta) - (hartasuami + (hartaibu * int(ibu)))

                    hartaspra = (sisa / 3) / int(spa)
                    hartaslka = ((sisa / 3) * 2) / int(sLa)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")

            elif len(lk) != 0 and len(pr) == 0:
                a = 4
                b = 8
                print("The L.C.M. is", compute_lcm(a, b))
                kpk = compute_lcm(a, b)
                bagian1 = peninggalan2.get("ibu")
                bagian2 = peninggalan2.get("suami")
                hartaibu = hitung_harta(ibu, bagian1, harta)
                hartasuami = hitung_harta(suami, bagian2, harta)
                hartalk = (int(harta) - (hartaibu + hartasuami)) / int(lk)

                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartaibu, "ibu")
                hasil = label_hasil(hartalk, "anak laki-laki")

            elif len(lk) == 0 and len(pr) != 0:
                a = 4
                b = 8
                print("The L.C.M. is", compute_lcm(a, b))
                kpk = compute_lcm(a, b)
                bagian1 = peninggalan2.get("ibu")
                hartaibu = hitung_harta(ibu, bagian1, harta)
                sisa = int(harta) - hartaibu
                hartasuami = sisa / 3 * 2
                hartapr = (sisa / 3) / int(pr)

                hasil = label_hasil(hartaibu, "ibu")
                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartapr, "anak Perempuan")

            elif len(lk) != 0 and len(pr) != 0:
                bagian1 = peninggalan2.get("suami")
                bagian2 = peninggalan2.get("ibu")

                hartasuami = hitung_harta(1, bagian1, harta)
                hartaibu = hitung_harta(ibu, bagian2, harta)

                sisa = int(harta) - (hartasuami + hartaibu)

                hartapr = (sisa / 3) / int(pr)
                hartalk = (sisa - hartapr) / int(lk)

                print(hartasuami)
                print(hartaibu)
                print(hartalk)
                print(hartapr)

                hasil = label_hasil(hartaibu, "ibu")
                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartalk, "anak Laki-laki")
                hasil = label_hasil(hartapr, "anak Perempuan")

        elif len(ayah) == 0 and len(ibu) != 0 and len(suami) != 0 and len(istri) != 0:
                if len(lk) == 0 and len(pr) == 0:
                    if len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                        if len(cucu) == 0:
                            bagian1 = peninggalan1.get("istri")
                            bagian2 = peninggalan1.get("suami")
                            bagian4 = peninggalan1.get("ibu")

                            hartaistri = hitung_harta(istri, bagian1, harta)
                            hartasuami = hitung_harta(suami, bagian2, harta)
                            hartaibu = hitung_harta(ibu, bagian4, harta)
                            sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)))

                            hartaistri = hartaistri + sisa
                            hartasuami = hartasuami + sisa
                            hartaibu = hartaibu + sisa

                            hasil = label_hasil(hartasuami, "suami")
                            hasil = label_hasil(hartaistri, "istri")
                            hasil = label_hasil(hartaibu, "ibu")

                        else:
                            bagian1 = peninggalan2.get("istri")
                            bagian2 = peninggalan2.get("suami")
                            bagian4 = peninggalan2.get("ibu")

                            hartaistri = hitung_harta(istri, bagian1, harta)
                            hartasuami = hitung_harta(suami, bagian2, harta)
                            hartaibu = hitung_harta(ibu, bagian4, harta)

                            hartacucu = int(harta) - (
                                    (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)))

                            hasil = label_hasil(hartasuami, "suami")
                            hasil = label_hasil(hartaistri, "istri")

                            hasil = label_hasil(hartaibu, "ibu")
                            hasil = label_hasil(hartacucu, "cucu")

                    elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")
                        bagian4 = peninggalan2.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = hitung_harta(ibu, bagian4, harta)

                        hartaslki = int(harta) - (
                                    (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu))) / int(
                            sLi)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")

                    elif len(sLi) != 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")

                        bagian4 = peninggalan2.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = hitung_harta(ibu, bagian4, harta)

                        hartaslki = int(harta) - (
                                    (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu))) / int(
                            sLi)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                        hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                    elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")

                        bagian4 = peninggalan2.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = hitung_harta(ibu, bagian4, harta)

                        hartaslki = int(harta) - (
                                (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu))) / int(sLi)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                        hasil = label_hasil("terhalang", "Saudara perempuan seayah")

                    elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")

                        bagian4 = peninggalan2.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = hitung_harta(ibu, bagian4, harta)

                        hartaspr = int(harta) - (
                                    (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu))) / int(
                            spi)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartaspr, "Saudara kandung Perempuan")

                    elif len(sLi) == 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")

                        bagian4 = peninggalan2.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = hitung_harta(ibu, bagian4, harta)

                        hartaspri = int(harta) - (
                                    (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu))) / int(
                            spi)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                        hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                    elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")

                        bagian4 = peninggalan2.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = hitung_harta(ibu, bagian4, harta)

                        hartaspri = int(harta) - (
                                    (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu))) / int(
                            spi)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                        hasil = label_hasil("Terhalang", "Saudara Perempuan seayah")


                    elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")

                        bagian4 = peninggalan2.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = hitung_harta(ibu, bagian4, harta)

                        sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)))

                        hartaspri = (sisa / 3) / int(spi)
                        hartaslki = ((sisa / 3) * 2) / int(sLi)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                        hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")

                    elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")

                        bagian4 = peninggalan2.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = hitung_harta(ibu, bagian4, harta)

                        sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)))

                        hartaspri = (sisa / 3) / int(spi)
                        hartaslki = ((sisa / 3) * 2) / int(sLi)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                        hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                        hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                    elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")

                        bagian4 = peninggalan2.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = hitung_harta(ibu, bagian4, harta)

                        sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)))

                        hartaspri = (sisa / 3) / int(spi)
                        hartaslki = ((sisa / 3) * 2) / int(sLi)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                        hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                        hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                    elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) != 0:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")

                        bagian4 = peninggalan2.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = hitung_harta(ibu, bagian4, harta)

                        sisa = int(harta) - (
                                (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)))

                        hartaspri = (sisa / 3) * int(spi)
                        hartaslki = ((sisa / 3) * 2) * int(sLi)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                        hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                        hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")
                        hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                    elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")

                        bagian4 = peninggalan2.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = hitung_harta(ibu, bagian4, harta)

                        hartaslka = int(harta) - (
                                    (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu))) / int(
                            sLa)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")

                    elif len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")

                        bagian4 = peninggalan2.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = hitung_harta(ibu, bagian4, harta)

                        hartaspra = int(harta) - (
                                    (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu))) / int(
                            spa)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")

                    elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) != 0:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")

                        bagian4 = peninggalan2.get("ibu")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartaibu = hitung_harta(ibu, bagian4, harta)

                        sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)))

                        hartaspra = (sisa / 3) / int(spa)
                        hartaslka = ((sisa / 3) * 2) / int(sLa)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartaibu, "ibu")
                        hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")
                        hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")

                elif len(lk) != 0 and len(pr) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    hartalk = int(harta) - (
                                (hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu))) / int(lk)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartalk, "anak laki-laki")

                elif len(lk) == 0 and len(pr) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)))

                    hartasuami = sisa / 3 * 2
                    hartapr = (sisa / 3) / int(pr)

                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartapr, "anak Perempuan")

                elif len(lk) != 0 and len(pr) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")
                    bagian4 = peninggalan2.get("ibu")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaibu = hitung_harta(ibu, bagian4, harta)
                    sisa = int(harta) - ((hartaistri * int(istri)) + (hartasuami * int(suami)) + (hartaibu * int(ibu)))

                    hartapr = (sisa / 3) / int(pr)
                    hartalk = (sisa - hartapr) / int(lk)

                    print(hartasuami)
                    print(hartaistri)
                    print(hartalk)
                    print(hartapr)

                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaibu, "ibu")
                    hasil = label_hasil(hartalk, "anak Laki-laki")
                    hasil = label_hasil(hartapr, "anak Perempuan")

        elif len(ayah) == 0 and len(ibu) == 0 and len(suami) != 0 and len(istri) != 0:
            if len(lk) == 0 and len(pr) == 0:
                if len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    if len(cucu) == 0:
                        bagian1 = peninggalan1.get("istri")
                        bagian2 = peninggalan1.get("suami")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = int(harta) - (hartaistri * int(istri))

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                    else:
                        bagian1 = peninggalan2.get("istri")
                        bagian2 = peninggalan2.get("suami")

                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartasuami = hitung_harta(suami, bagian2, harta)
                        hartacucu = int(harta) - (hartasuami + (hartaistri * int(istri))) / int(cucu)

                        hasil = label_hasil(hartasuami, "suami")
                        hasil = label_hasil(hartaistri, "istri")
                        hasil = label_hasil(hartacucu, "cucu")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaslki = int(harta) - (hartasuami + (hartaistri * int(istri))) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaslki = int(harta) - (hartasuami + (hartaistri * int(istri))) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaslki = int(harta) - (hartasuami + (hartaistri * int(istri))) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-laki")
                    hasil = label_hasil("terhalang", "Saudara perempuan seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaspri = int(harta) - (hartasuami + (hartaistri * int(istri))) / int(spi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaspri = int(harta) - (hartasuami + (hartaistri * int(istri))) / int(spi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaspri = int(harta) - (hartasuami + (hartaistri * int(istri))) / int(spi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("Terhalang", "Saudara Perempuan seayah")


                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    sisa = int(harta) - (hartasuami + (hartaistri * int(istri)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    sisa = int(harta) - (hartasuami + (hartaistri * int(istri)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    sisa = int(harta) - (hartasuami + (hartaistri * int(istri)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    sisa = int(harta) - (hartasuami + (hartaistri * int(istri)))

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaslka = int(harta) - (hartasuami + (hartaistri * int(istri))) / int(sLa)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    hartaspra = int(harta) - (hartasuami + (hartaistri * int(istri))) / int(spa)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seibu")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    bagian2 = peninggalan2.get("suami")

                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartasuami = hitung_harta(suami, bagian2, harta)
                    sisa = int(harta) - (hartasuami + (hartaistri * int(istri)))

                    hartaspra = (sisa / 3) / int(spa)
                    hartaslka = ((sisa / 3) * 2) / int(sLa)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")

            elif len(lk) != 0 and len(pr) == 0:
                a = 4
                b = 8
                print("The L.C.M. is", compute_lcm(a, b))
                kpk = compute_lcm(a, b)
                bagian1 = peninggalan2.get("istri")
                bagian2 = peninggalan2.get("suami")
                hartaistri = hitung_harta(istri, bagian1, harta)
                hartasuami = hitung_harta(suami, bagian2, harta)
                hartalk = (int(harta) - (hartaistri + hartasuami)) / int(lk)

                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartalk, "anak laki-laki")

            elif len(lk) == 0 and len(pr) != 0:
                a = 4
                b = 8
                print("The L.C.M. is", compute_lcm(a, b))
                kpk = compute_lcm(a, b)
                bagian1 = peninggalan2.get("istri")
                hartaistri = hitung_harta(istri, bagian1, harta)
                sisa = int(harta) - hartaistri
                hartasuami = sisa / 3 * 2
                hartapr = (sisa / 3) / int(pr)

                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartapr, "anak Perempuan")

            elif len(lk) != 0 and len(pr) != 0:
                bagian1 = peninggalan2.get("suami")
                bagian2 = peninggalan2.get("istri")

                hartasuami = hitung_harta(1, bagian1, harta)
                hartaistri = hitung_harta(istri, bagian2, harta)

                sisa = int(harta) - (hartasuami + hartaistri)

                hartapr = (sisa / 3) / int(pr)
                hartalk = (sisa - hartapr) / int(lk)

                print(hartasuami)
                print(hartaistri)
                print(hartalk)
                print(hartapr)

                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartasuami, "suami")
                hasil = label_hasil(hartalk, "anak Laki-laki")
                hasil = label_hasil(hartapr, "anak Perempuan")

        elif len(ayah) == 0 and len(ibu) == 0 and len(suami) == 0 and len(istri) != 0:
            if len(lk) == 0 and len(pr) == 0:

                if len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    if len(cucu) == 0:
                        bagian = int(harta) / int(istri)
                        text123 = f"Bagian Suami  : {bagian} / Orang"
                        daftarhasil.append(text123)
                        
                    else:
                        bagian1 = peninggalan2.get("istri")
                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartacucu = (int(harta) - (hartaistri * int(istri))) / int(cucu)

                        hasil = label_hasil(int(hartaistri), "istri")
                        hasil = label_hasil(hartacucu, "Cucu")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaslki = (int(harta) - (hartaistri * int(istri))) / int(sLi)

                    hasil = label_hasil(int(hartaistri), "istri")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaslki = (int(harta) - (hartaistri * int(istri))) / int(sLi)

                    hasil = label_hasil(int(hartaistri), "istri")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaslki = (int(harta) - (hartaistri * int(istri))) / int(sLi)

                    hasil = label_hasil(int(hartaistri), "istri")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaspri = (int(harta) - (hartaistri * int(istri))) / int(spi)

                    hasil = label_hasil(int(hartaistri), "istri")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    hartaistri = hitung_harta(istri, bagian1, harta)

                    bagian2 = peninggalan2.get("sPseibu")
                    hartaspri = hitung_harta(spi, bagian2, harta)
                    hartaspra = (int(harta) - hartaspri) / int(spa)

                    hasil = label_hasil(int(hartaistri), "istri")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    hartaistri = hitung_harta(istri, bagian1, harta)

                    hartaspra = (((int(harta) - (hartaistri * int(istri))) / 3) * 2) / int(sLa)
                    hartaspri = ((int(harta) - (hartaistri * int(istri))) / 3) / int(spi)

                    hasil = label_hasil(int(hartaistri), "istri")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")


                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    hartaistri = hitung_harta(istri, bagian1, harta)
                    sisa = int(harta) - hartaistri

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    hartaistri = hitung_harta(istri, bagian1, harta)
                    sisa = int(harta) - hartaistri

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    hartaistri = hitung_harta(istri, bagian1, harta)
                    sisa = int(harta) - hartaistri

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    hartaistri = hitung_harta(istri, bagian1, harta)
                    sisa = int(harta) - hartaistri

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("istri")
                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaslka = (int(harta) - (hartaistri * int(istri))) / int(sLa)

                    hasil = label_hasil(int(hartaistri), "istri")
                    hasil = label_hasil(hartaslka, "Saudara Laki-Laki Seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    hartaistri = hitung_harta(istri, bagian1, harta)
                    hartaspra = (int(harta) - (hartaistri * int(istri))) / int(spa)

                    hasil = label_hasil(int(hartaistri), "istri")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan Seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("istri")
                    hartaistri = hitung_harta(istri, bagian1, harta)
                    sisa = int(harta) - hartaistri

                    hartaspra = (sisa / 3) / int(spa)
                    hartaslka = ((sisa / 3) * 2) / int(sLa)

                    hasil = label_hasil(hartaistri, "istri")
                    hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")


            elif len(lk) != 0 and len(pr) == 0:
                pr = 0
                print("jumlah anak anak pr :", pr)
                aibu = 8
                banak = 1
                print("The L.C.M. is", compute_lcm(aibu, banak))
                kpk = compute_lcm(aibu, banak)

                bagian1 = peninggalan2.get("istri")
                hartaistri = hitung_harta(istri, bagian1, harta)

                hartalk = int(harta) - ((hartaistri * int(istri)))

                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartalk, "anak laki-laki")


            elif len(lk) == 0 and len(pr) != 0:
                lk = 0
                aibu = 8
                bagian1 = peninggalan2.get("istri")
                hartaistri = hitung_harta(istri, bagian1, harta)
                hartapr = int(harta) - ((hartaistri * int(istri)))

                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartapr, "anak Perempuan")

            else:
                bagian1 = peninggalan2.get("istri")
                hartaistri = hitung_harta(istri, bagian1, harta)
                sisa = int(harta) - hartaistri

                hartapr = (sisa / 3)/int(pr)
                hartalk = (sisa / 3 * 2)/int(lk)

                hasil = label_hasil(hartaistri, "istri")
                hasil = label_hasil(hartalk, "anak Laki-laki")
                hasil = label_hasil(hartapr, "anak Perempuan")

        elif len(ayah) == 0 and len(ibu) == 0 and len(suami) != 0 and len(istri) == 0:
            if len(lk) == 0 and len(pr) == 0:
                if len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    if len(cucu) == 0:
                        bagian = int(harta)
                        text12345 = f"Bagian Suami  : {bagian} / Orang"
                        
                    else:
                        bagian1 = peninggalan2.get("suami")
                        hartaistri = hitung_harta(istri, bagian1, harta)
                        hartacucu = (int(harta) - (hartaistri * int(istri))) / int(cucu)

                        hasil = label_hasil(int(hartaistri), "istri")
                        hasil = label_hasil(hartacucu, "Cucu")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("suami")
                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaslki = (int(harta) - (hartasuami * int(suami))) / int(sLi)

                    hasil = label_hasil(int(hartasuami), "suami")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("suami")
                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaslki = (int(harta) - (hartasuami * int(suami))) / int(sLi)

                    hasil = label_hasil(int(hartasuami), "suami")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("suami")
                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaslki = (int(harta) - (hartasuami * int(suami))) / int(sLi)

                    hasil = label_hasil(int(hartasuami), "suami")
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("suami")
                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaspri = (int(harta) - (hartasuami * int(suami))) / int(spi)

                    hasil = label_hasil(int(hartasuami), "suami")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("suami")
                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaspri = (int(harta) - (hartasuami * int(suami))) / int(spi)

                    hasil = label_hasil(int(hartasuami), "suami")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("suami")
                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaspri = (int(harta) - (hartasuami * int(suami))) / int(spi)

                    hasil = label_hasil(int(hartasuami), "suami")
                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")


                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("suami")
                    hartasuami = hitung_harta(suami, bagian1, harta)
                    sisa = int(harta) - hartasuami

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("suami")
                    hartasuami = hitung_harta(suami, bagian1, harta)
                    sisa = int(harta) - hartasuami

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("suami")
                    hartasuami = hitung_harta(suami, bagian1, harta)
                    sisa = int(harta) - hartasuami

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("suami")
                    hartasuami = hitung_harta(suami, bagian1, harta)
                    sisa = int(harta) - hartasuami

                    hartaspri = (sisa / 3) / int(spi)
                    hartaslki = ((sisa / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartasuami, "suami")
                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("suami")
                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaslka = (int(harta) - (hartasuami * int(suami))) / int(sLa)

                    hasil = label_hasil(int(hartasuami), "Suami")
                    hasil = label_hasil(hartaslka, "Saudara Laki-Laki Seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("suami")
                    hartasuami = hitung_harta(suami, bagian1, harta)
                    hartaspra = (int(harta) - (hartasuami * int(suami))) / int(spa)

                    hasil = label_hasil(int(hartasuami), "Suami")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan Seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("suami")
                    hartasuami = hitung_harta(suami, bagian1, harta)
                    sisa = int(harta) - hartasuami

                    hartaspra = (sisa / 3) / int(spa)
                    hartaslka = ((sisa / 3) * 2) / int(sLa)

                    hasil = label_hasil(hartasuami, "Suami")
                    hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")


            elif len(lk) != 0 and len(pr) == 0:
                pr = 0
                print("jumlah anak anak pr :", pr)
                aibu = 4
                banak = 1
                print("The L.C.M. is", compute_lcm(aibu, banak))
                kpk = compute_lcm(aibu, banak)

                bagian2 = peninggalan2.get("suami")
                hartasuami = hitung_harta(1, bagian2, harta)

                hartalk = (int(harta) - (hartasuami)) / int(lk)

                hasil = label_hasil(hartasuami, "Suami")
                hasil = label_hasil(hartalk, "anak Laki-laki")

            elif len(lk) == 0 and len(pr) != 0:
                lk = 0
                bagian2 = peninggalan2.get("suami")
                hartasuami = hitung_harta(1, bagian2, harta)
                hartapr = (int(harta) - hartasuami) / int(pr)

                hasil = label_hasil(hartasuami, "Suami")
                hasil = label_hasil(hartapr, "anak Perempuan")

            else:
                bagian2 = peninggalan2.get("suami")
                hartasuami = hitung_harta(1, bagian2, harta)
                sisa = int(harta) - hartasuami

                hartapr = (sisa / 3) / int(pr)
                hartalk = (sisa / 3 * 2) / int(lk)

                hasil = label_hasil(hartasuami, "istri")
                hasil = label_hasil(hartalk, "anak Laki-laki")
                hasil = label_hasil(hartapr, "anak Perempuan")

        elif len(ayah) == 0 and len(ibu) == 0 and len(suami) == 0 and len(istri) == 0:
            if (len(lk) != 0 and len(pr) != 0):
                bagian3 = peninggalan1.get("anakP")
                hartapr = hitung_harta(pr, bagian3, harta)

                hartalk = (int(harta) - (hartapr * int(pr))) / int(lk)

                hasil = label_hasil(hartalk, "anak Laki-laki")
                hasil = label_hasil(hartapr, "anak Perempuan")

            elif (len(lk) != 0 and len(pr) == 0):
                bagian4 = peninggalan1.get("anakL")
                hartalk = hitung_harta(lk, bagian3, harta)

                hasil = label_hasil(hartalk, "anak Laki-laki")

            elif (len(lk) == 0 and len(pr) != 0):
                bagian4 = peninggalan1.get("anakP")
                hartapr = hitung_harta(pr, bagian3, harta)

                hasil = label_hasil(hartapr, "anak Perempuan")

            elif len(lk) == 0 and len(pr) == 0:

                if len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) == 0:

                    hartaslki = int(harta) / int(sLi)
                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:

                    hartaslki = int(harta) / int(sLi)

                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:

                    hartaslki = int(harta) / int(sLi)

                    hasil = label_hasil(hartaslki, "Saudara kandung Laki-Laki")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:

                    hartaspri = int(harta) / int(spi)

                    hasil = label_hasil(hartaspri, "Saudara kandung Perempuan")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:
                    bagian1 = peninggalan2.get("spseibu")
                    hartaspri = hitung_harta(spi, bagian1, harta)
                    hartaslki = (int(harta) - (hartaspri * int(sLa))) / int(sLa)

                    hasil = label_hasil(int(hartaspri), "Saudara kandung perempuan")
                    hasil = label_hasil(hartaslki, "Saudara laki-laki seayah")

                elif len(sLi) == 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:
                    bagian1 = peninggalan2.get("spibu")
                    hartaspri = hitung_harta(spi, bagian1, harta)
                    hartaspra = (int(harta) - (hartaspri * int(spa))) / int(spa)

                    hasil = label_hasil(int(hartaspri), "Saudara kandung perempuan")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")


                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) == 0:
                    hartaspri = (int(harta) / 3) / int(spi)
                    hartaslki = ((int(harta) / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) == 0:

                    hartaspri = (int(harta) / 3) / int(spi)
                    hartaslki = ((int(harta) / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) == 0 and len(spa) != 0:

                    hartaspri = (int(harta) / 3) /int(spi)
                    hartaslki = ((int(harta) / 3) * 2) /int(sLi)

                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) != 0 and len(spi) != 0 and len(sLa) != 0 and len(spa) != 0:

                    hartaspri = (int(harta) / 3) / int(spi)
                    hartaslki = ((int(harta) / 3) * 2) / int(sLi)

                    hasil = label_hasil(hartaslki, "Saudara Laki-laki Kandung")
                    hasil = label_hasil(hartaspri, "Saudara Perempuan Kandung")
                    hasil = label_hasil("terhalang", "Saudara Laki-Laki seayah")
                    hasil = label_hasil("terhalang", "Saudara Perempuan seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) == 0:

                    hartaslka = int(harta) / int(sLa)

                    hasil = label_hasil(hartaslka, "Saudara Laki-Laki Seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) == 0 and len(spa) != 0:

                    hartaspra = int(harta) / int(sLa)

                    hasil = label_hasil(hartaspra, "Saudara Perempuan Seayah")

                elif len(sLi) == 0 and len(spi) == 0 and len(sLa) != 0 and len(spa) != 0:

                    hartaspra = (int(harta) / 3) / int(spa)
                    hartaslka = (int(harta) * 2) / int(sLa)

                    hasil = label_hasil(hartaslka, "Saudara Laki-laki seayah")
                    hasil = label_hasil(hartaspra, "Saudara Perempuan seayah")

MainApp().run()