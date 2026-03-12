import matplotlib.pyplot as plt
import numpy as np
import logging

# 1. HATA YÖNETİMİ: Uygulamanın çökmemesi için günlük tutma sistemi
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class KesirSiralamaSistemi:
    """
    5. Sınıf müfredatına uygun, Diskalkuli dostu 
    Kesir Karşılaştırma ve Sıralama Motoru.
    """
    def __init__(self, payda: int):
        # Güvenlik Kontrolü: Payda 0 veya negatif olamaz
        if payda <= 0:
            logging.error("Hatalı Veri: Payda 0'dan büyük olmalıdır.")
            raise ValueError("Payda (alt sayı) 0'dan büyük bir sayı seçilmelidir.")
        
        self.payda = payda
        # Diskalkuli için yüksek kontrastlı renk paleti
        self.renkler = ['#E63946', '#457B9D', '#A8DADC', '#F1FAEE']

    def asama_1_somut_deneyim(self, ogrenci_adi: str, pay_degerleri: list):
        """SOMUT AŞAMA: Fiziksel nesne simülasyonu (ASCII Lego)"""
        print(f"\n{'='*50}")
        print(f"🌟 HOŞ GELDİN {ogrenci_adi.upper()}! 🌟")
        print(f"{'='*50}\n")
        print(f"ADIM 1: SOMUT DENEYİM (Lego Kuleleri)")
        print(f"Toplam {self.payda} parçalık bir zeminimiz var.\n")

        for i, pay in enumerate(pay_degerleri):
            kule = "█" * pay + "░" * (self.payda - pay)
            print(f"{i+1}. Kule ({pay}/{self.payda}): [{kule}]")
        print("\nSoru: Hangi kule daha çok yer kaplıyor? (Gözle kontrol et!)")

    def asama_2_gorsellestirme(self, pay_degerleri: list):
        """YARI-SOMUT AŞAMA: Alan modelleri ve grafikler"""
        logging.info("Grafik motoru hazırlanıyor...")
        
        try:
            fig, ax = plt.subplots(len(pay_degerleri), 1, figsize=(10, 6))
            if len(pay_degerleri) == 1: ax = [ax]

            for i, pay in enumerate(pay_degerleri):
                # Bütünün tamamını (çerçeve) çiz
                ax[i].barh(0, 1, color='none', edgecolor='black', linewidth=3)
                # Alınan parçayı (pay) boya
                ax[i].barh(0, pay/self.payda, color=self.renkler[i % len(self.renkler)])
                
                # Diskalkuli desteği: Bölmeleri tek tek göster (Grid)
                for j in range(1, self.payda):
                    ax[i].axvline(j/self.payda, color='black', linestyle='--', alpha=0.3)
                
                ax[i].set_xlim(0, 1)
                ax[i].set_yticks([])
                ax[i].set_title(f"Kesir: {pay} / {self.payda}", fontweight='bold')

            plt.tight_layout()
            print("\nADIM 2: GÖRSELLEŞTİRME (Kesir Çubukları)")
            print("Görsel penceresi açılıyor, lütfen kontrol et...")
            plt.show()
        except Exception as e:
            logging.error(f"Grafik çizilirken bir hata oluştu: {e}")

    def asama_3_soyut_kural(self, pay_degerleri: list):
        """SOYUT AŞAMA: Matematiksel semboller ve kural tanımlama"""
        print(f"\nADIM 3: SOYUT KURAL (Matematik Dili)")
        # Payları büyükten küçüğe sırala
        sirali_paylar = sorted(pay_degerleri, reverse=True)
        
        sonuc_metni = " > ". join([f"{p}/{self.payda}" for p in sirali_paylar])
        
        print("💡 UNUTMA: Paydalar (alt sayılar) eşitse, üstü (payı) büyük olan kesir daha büyüktür!")
        print(f"Sıralama Sonucu: {sonuc_metni}")
        print("\n" + "="*50)

# --- ÇALIŞTIRMA BÖLÜMÜ ---
if __name__ == "__main__":
    # Senaryo: Paydası 8 olan bir bütünü karşılaştıralım
    try:
        egitim = KesirSiralamaSistemi(payda=8)
        ogrenci_paylari = [3, 5, 2] # Öğrencinin karşılaştıracağı kesirler
        
        egitim.asama_1_somut_deneyim("Küçük Matematikçi", ogrenci_paylari)
        egitim.asama_2_gorsellestirme(ogrenci_paylari)
        egitim.asama_3_soyut_kural(ogrenci_paylari)
        
    except ValueError as e:
        print(f"Giriş Hatası: {e}")
