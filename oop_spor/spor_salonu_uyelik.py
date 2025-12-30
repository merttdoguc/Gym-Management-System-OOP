from datetime import datetime, timedelta
import time

# OdemeIslemi class
class OdemeIslemi:
    def __init__(self, uye_id, uye_isim, tutar, aciklama):
        self._uye_id = uye_id
        self._uye_isim = uye_isim
        self._tutar = tutar
        self._aciklama = aciklama
        self._tarih = datetime.now()

    def get_tutar(self):
        return self._tutar

    def odeme_yap(self):
        return self._tutar > 0

    def __str__(self):
        return f"[{self._tarih.strftime('%Y-%m-%d %H:%M')}] ID:{self._uye_id} {self._uye_isim} -> {self._tutar} TL ({self._aciklama})"


# UyelikPaketi class
class UyelikPaketi:
    def __init__(self, paket_adi, fiyat, sure_ay):
        self._paket_adi = paket_adi
        self._fiyat = fiyat
        self._sure_ay = sure_ay

    def get_paket_adi(self):
        return self._paket_adi

    def get_fiyat(self):
        return self._fiyat

    def get_sure_ay(self):
        return self._sure_ay

    def __str__(self):
        return f"{self.get_paket_adi()} ({self.get_sure_ay()} Ay) - {self.get_fiyat()} TL"


# uye class
class Uye:
    def __init__(self, isim, soyisim, yas, telefon, e_posta, paket):
        self._isim = isim
        self._soyisim = soyisim
        self._yas = yas
        self._telefon = telefon
        self._e_posta = e_posta
        self._paket = paket
        self._kayit_tarihi = datetime.now()
        self._uyelik_bitis_tarihi = self._kayit_tarihi + timedelta(days=30 * paket.get_sure_ay())

    # GETTERLAR
    def get_isim(self):
        return self._isim

    def get_soyisim(self):
        return self._soyisim

    def get_yas(self):
        return self._yas

    def get_telefon(self):
        return self._telefon

    def get_eposta(self):
        return self._e_posta

    def get_paket(self):
        return self._paket

    def get_uyelik_bitis_tarihi(self):
        return self._uyelik_bitis_tarihi

    # SETTER
    def set_paket(self, paket):
        self._paket = paket

    def set_uyelik_bitis_tarihi(self, tarih):
        self._uyelik_bitis_tarihi = tarih

    # DAVRANIS
    def uyelik_kontrol(self):
        return datetime.now() < self._uyelik_bitis_tarihi

    def bilgi_goster(self):
        durum = "Aktif" if self.uyelik_kontrol() else "Pasif (Süre Dolmuş)"

        print("\n--- ÜYE BİLGİLERİ ---")
        print("İsim:", self.get_isim(), self.get_soyisim())
        print("Yaş:", self.get_yas())
        print("Telefon:", self.get_telefon())
        print("E-posta:", self.get_eposta())
        print("Paket:", self.get_paket().get_paket_adi())
        print("Bitiş Tarihi:", self.get_uyelik_bitis_tarihi().strftime("%Y-%m-%d"))
        print("Üyelik Durumu:", durum)
        print("--------------------\n")


# SporSalonu class
class SporSalonu:
    def __init__(self):
        self._uyeler = {}
        self._odemeler = []
        self._uye_sayaci = 0

        self._paketler = [
            UyelikPaketi("Aylık", 300, 1),
            UyelikPaketi("3 Aylık", 800, 3),
            UyelikPaketi("6 Aylık", 1500, 6),
            UyelikPaketi("Yıllık", 2500, 12)
        ]

    def get_paketler(self):
        return self._paketler

    def odeme_kaydet(self, uye_id, uye_isim, tutar, aciklama):
        odeme = OdemeIslemi(uye_id, uye_isim, tutar, aciklama)
        self._odemeler.append(odeme)
        print(f"*** {tutar} TL ödeme alındı ***")

    def uye_ekle(self, isim, soyisim, yas, telefon, e_posta, paket_no):
        try:
            p_idx = int(paket_no) - 1
            if p_idx < 0 or p_idx >= len(self._paketler): # geçersiz paket numarası kontrolü
                print("HATA: Geçersiz paket")
                return

            paket = self._paketler[p_idx]
            self._uye_sayaci += 1
            uye_id = self._uye_sayaci

            uye = Uye(isim, soyisim, yas, telefon, e_posta, paket)
            self._uyeler[uye_id] = uye

            print(f"{isim} {soyisim} (ID:{uye_id}) eklendi")
            self.odeme_kaydet(uye_id, f"{isim} {soyisim}", paket.get_fiyat(), "Yeni Kayıt")
            uye.bilgi_goster()
        except ValueError:
            print("HATA: Paket numarası rakam olmalıı")

    def uye_sil(self, uye_id):
        if uye_id in self._uyeler:
            del self._uyeler[uye_id]
            print("Üye silindi")
        else:
            print("Üye bulunamadı")

    def uye_bilgilerini_goster(self, uye_id):
        uye = self._uyeler.get(uye_id)
        if uye:
            uye.bilgi_goster()
        else:
            print("Üye bulunamadı")

    def uyelik_satin_al(self, uye_id, paket_no):
        uye = self._uyeler.get(uye_id)
        if not uye:
            print("Üye bulunamadı")
            return

        try:
            paket = self._paketler[int(paket_no) - 1]

            baslangic = uye.get_uyelik_bitis_tarihi() # üyelik bitti mi bitmedi mi kontrolü
            if baslangic < datetime.now():
                baslangic = datetime.now() 

            yeni_bitis = baslangic + timedelta(days=30 * paket.get_sure_ay()) # yeni bitiş tarihi hesaplama
            uye.set_uyelik_bitis_tarihi(yeni_bitis)
            uye.set_paket(paket)

            print("Üyelik uzatıldı:", yeni_bitis.strftime("%Y-%m-%d"))
            self.odeme_kaydet(uye_id, uye.get_isim() + " " + uye.get_soyisim(), paket.get_fiyat(), "Süre Uzatma")
        except (ValueError, IndexError):
            print("HATA: Geçersiz paket seçimi")

    def kasa_raporu(self):
        toplam = 0
        print("\n--- KASA RAPORU ---")
        for odeme in self._odemeler:
            print(odeme)
            toplam += odeme.get_tutar()
        print("TOPLAM CİRO:", toplam, "TL")
        print("------------------")


# ana menu
if __name__ == "__main__":
    salon = SporSalonu()

    while True:
        print("1- Üye Ekle")
        print("2- Üye Sil")
        print("3- Üye Bilgisi Göster")
        print("4- Üyelik Uzat")
        print("5- Kasa Raporu")
        print("6- Çıkış")

        secim = input("Seçim: ")

        if secim == "1":
            isim = input("İsim: ")
            soyisim = input("Soyisim: ")
            
            # Sayısal veri kontrolü
            try:
                yas = int(input("Yaş: "))
            except ValueError:
                print("HATA: Yaş rakam olmalı!")
                continue

            while True:
                telefon = input("Telefon: ")
                if len(telefon) == 11 and telefon.isdigit():
                    break
                else:
                    print("HATA: Telefon 11 haneli ve sadece rakam olmalı!")

            while True:
                e_posta = input("E-posta: ")
                if "@" in e_posta and len(e_posta) > 3:
                    break
                else:
                    print("HATA: Geçerli bir e-posta giriniz!")

            for i, p in enumerate(salon.get_paketler(), 1): #paketleri listeme 
                print(f"{i}. {p}")

            paket_no = input("Paket No: ")
            salon.uye_ekle(isim, soyisim, yas, telefon, e_posta, paket_no)

        elif secim == "2":
            try:
                uye_id = int(input("Üye ID: "))
                salon.uye_sil(uye_id)
            except ValueError:
                print("HATA: ID rakam olmalı")

        elif secim == "3":
            try:
                uye_id = int(input("Üye ID: "))
                salon.uye_bilgilerini_goster(uye_id)
            except ValueError:
                print("HATA: ID rakam olmalı")

        elif secim == "4":
            try:
                uye_id = int(input("Üye ID: "))
                for i, p in enumerate(salon.get_paketler(), 1):
                    print(f"{i}. {p}")
                paket_no = int(input("Paket No: "))
                salon.uyelik_satin_al(uye_id, paket_no)
            except ValueError:
                print("HATA: Lütfen geçerli sayılar giriniz")

        elif secim == "5":
            salon.kasa_raporu()

        elif secim == "6":
            print("Çıkış yapılıyor...")
            time.sleep(1)
            break

        else:
            print("Geçersiz seçim")