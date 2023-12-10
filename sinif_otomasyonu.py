ogrenciler = {
    "1234": {"isim": "Ahmet Yılmaz", "devamsizlikhakki": 6, "sinav_notu": 0},
    "5678": {"isim": "Ayşe Kaya", "devamsizlikhakki": 6, "sinav_notu": 0},
    "4545": {"isim": "Mehmet Demir", "devamsizlikhakki": 6, "sinav_notu": 0},
    "3223": {"isim": "Mustafa Koç", "devamsizlikhakki": 6, "sinav_notu": 0},
    "1778": {"isim": "Aylin Yıldız", "devamsizlikhakki": 6, "sinav_notu": 0}
    # Diğer öğrenciler buraya eklenebilir
}

# Genel yoklama al
def genel_yoklama_al():
    for hafta in range(1, 11):
        print(f"{hafta}. Hafta")
        for ogrenci_numarasi, ogrenci_bilgileri in ogrenciler.items():
            cevap = input(f"{ogrenci_bilgileri['isim']} sınıfta mı? (E/H): ").upper()
            if cevap == "H":
                ogrenci_bilgileri['devamsizlikhakki'] -= 1

def ogrenci_sorgula():
    for ogrenci_numarasi, ogrenci_bilgileri in ogrenciler.items():
        if ogrenci_bilgileri['devamsizlikhakki'] <= 3:
            print(f"{ogrenci_bilgileri['isim']} kritik durumda.")
            if ogrenci_bilgileri['devamsizlikhakki'] > 0:
                print(f"{ogrenci_bilgileri['isim']}, devamsızlık hakkı var, sınava girebilir.")
                cevap = input(f"{ogrenci_bilgileri['isim']}, sınava girdi mi? (E/H): ").upper()
            else:
                print(f"{ogrenci_bilgileri['isim']} devamsızlık hakkı bittiği için başarısız.")
        elif 3 < ogrenci_bilgileri['devamsizlikhakki'] <= 6:
            print(f"{ogrenci_bilgileri['isim']} sınava girebilir.")
            cevap = input(f"{ogrenci_bilgileri['isim']}, sınava girdi mi? (E/H): ").upper()
            if cevap == "H":
                print(f"{ogrenci_bilgileri['isim']} sınava girmediği için başarısız.")
            else:
                notu = int(input(f"{ogrenci_bilgileri['isim']}, sınav notunu girin: "))
                ogrenci_bilgileri['sinav_notu'] = notu
                if notu >= 50:
                    print(f"{ogrenci_bilgileri['isim']} başarılı.")
                else:
                    print(f"{ogrenci_bilgileri['isim']} başarısız.")
                    
def raporlar():
    print("--------------------------")
    print("-------- RAPORLAR --------")
    print("--------------------------")
    print("1. Genel Yoklama Listesi(Kritikler '*' İşaretli)")
    print("-------------------------")
    print("2. Sınava Gelmeyenler Listesi")
    print("-------------------------")
    print("3. Sınav Sonuçları Listesi")
    print("-------------------------")
    secim = input("Lütfen bir rapor seçin (1-3): ")
    
    if secim == "1":
        for ogrenci_numarasi, ogrenci_bilgileri in ogrenciler.items():
            if ogrenci_bilgileri['devamsizlikhakki'] <= 3:
                print(f"* {ogrenci_bilgileri['isim']} kritik sınıfta.")
            else:
                print(f"{ogrenci_bilgileri['isim']}")
        
    elif secim == "2":
        for ogrenci_numarasi, ogrenci_bilgileri in ogrenciler.items():
            if ogrenci_bilgileri['sinav_notu'] == 0 :
                print(f"{ogrenci_bilgileri['isim']} sınava gelmedi ve başarısız kabul edildi.")
                
    elif secim == "3":
        for ogrenci_numarasi, ogrenci_bilgileri in ogrenciler.items():
            if ogrenci_bilgileri['sinav_notu'] != 0:
                if ogrenci_bilgileri['sinav_notu'] >= 50:
                    print(f"{ogrenci_bilgileri['isim']} : {ogrenci_bilgileri['sinav_notu']} Başarılı")
                else:
                    print(f"{ogrenci_bilgileri['isim']} : {ogrenci_bilgileri['sinav_notu']} Başarısız")
           # else:
           #     print(f"{ogrenci_bilgileri['isim']} sınav sonucu henüz açıklanmadı.")
                

print("----------------------")
print("-------- MENÜ --------")
print("----------------------")
print("1. Genel Yoklama Al")
print("----------------------")
print("2. Öğrenci Durumlarını Kontrol Et")
print("----------------------")
print("3. Raporlar")
print("----------------------")
print("4. Çıkış")
print("----------------------")

while True:
    secim = input("Lütfen bir seçenek girin (1-4): ")

    if secim == "1":
        genel_yoklama_al()
    elif secim == "2":
        ogrenci_sorgula()
    elif secim == "3":
        raporlar()
    elif secim == "4":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")
