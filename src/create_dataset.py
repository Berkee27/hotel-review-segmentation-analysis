from pathlib import Path
import pandas as pd


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_PATH = DATA_DIR / "hotel_reviews.csv"


positive_reviews = [
    "Otelin konumu harikaydı, oda temizdi ve personel ilgiliydi. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Kahvaltı lezzetliydi, yatak rahattı, tekrar gelmek isterim. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Resepsiyon hızlı yardımcı oldu, oda manzarası güzeldi. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Temizlik başarılıydı, banyo düzenliydi, otelden memnun kaldık. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Personel güler yüzlüydü, hizmet kalitesi beklentimin üzerindeydi. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Oda sessizdi, klima iyi çalışıyordu, rahat bir gece geçirdik. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Denize yakın olması büyük avantajdı, konaklama keyifliydi. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Fiyat performans olarak iyi bir oteldi. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Otel merkezi yerdeydi, ulaşım kolaydı, tavsiye ederim. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Yemekler tazeydi, çalışanlar yardımseverdi, genel deneyim olumluydu. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Check-in hızlıydı, odamız erken hazırlandı, memnun kaldık. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Havuz temizdi, ortak alanlar düzenliydi, aile için uygundu. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Oda genişti, yatak konforluydu, dinlenmek için idealdi. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Manzara mükemmeldi, balkon keyifliydi, tatilimiz güzel geçti. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Personel sorunlarımızı hemen çözdü, hizmetten memnun kaldık. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Otel sessiz ve huzurluydu, gece rahat uyuduk. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Kahvaltı çeşitleri yeterliydi, ürünler taze görünüyordu. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Oda dekorasyonu şıktı, temizlik kokusu güzeldi. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Konum sayesinde her yere yürüyerek ulaşabildik. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Çalışanlar nazikti, girişten çıkışa kadar iyi ilgilendiler. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Otopark kolaylığı vardı, araçla gelenler için rahattı. Genel olarak memnun kaldım ve tavsiye ederim.",
    "İnternet hızlıydı, iş seyahati için uygundu. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Çocuklu aileler için güvenli ve rahat bir ortam vardı. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Spa alanı temizdi, masaj hizmeti başarılıydı. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Oda servisi hızlı geldi, siparişler sıcak ve lezzetliydi. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Fiyatına göre odalar kaliteli ve bakımlıydı. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Resepsiyondaki ekip profesyoneldi ve çözüm odaklıydı. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Otel genel olarak temiz, düzenli ve konforluydu. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Tatilimiz beklentimizin üzerinde geçti, kesinlikle öneririm. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Her şey planlıydı, çıkış işlemleri bile hızlıydı. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Mini bar düzenliydi, havlular temizdi, oda ferah görünüyordu. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Gece sessizliği iyiydi, koridorlarda gürültü yoktu. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Plaja yürüyerek birkaç dakikada ulaştık, konum şahane. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Personel kibar davrandı ve valizlerimize yardımcı oldu. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Kahve ve tatlı servisi beklediğimden iyiydi. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Otel fotoğraflardaki gibi temiz ve moderndi. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Duş sıcak suyu sorunsuzdu, banyo hijyenikti. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Kısa konaklama için pratik ve rahat bir seçim oldu. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Yatak çarşafları tertemizdi, uyku kalitesi iyiydi. Genel olarak memnun kaldım ve tavsiye ederim.",
    "Genel atmosfer sakin, güvenli ve misafirperverdi. Genel olarak memnun kaldım ve tavsiye ederim."
]


negative_reviews = [
    "Oda kirliydi, banyo kötü kokuyordu ve personel ilgisizdi. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Kahvaltı zayıftı, ürünler bayattı, memnun kalmadık. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Resepsiyon yavaştı, check-in sırasında uzun süre bekledik. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Klima çalışmıyordu, oda sıcaktı ve rahatsız uyuduk. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Yatak sertti, çarşaflar temiz görünmüyordu. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Otel gürültülüydü, gece boyunca uyuyamadık. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Fiyatına göre hizmet kalitesi düşüktü. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Denize yakın denmişti ama konum beklentiyi karşılamadı. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Personel kaba davrandı, sorunlarımızla ilgilenmedi. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Banyo eskiydi, duş başlığı bozuktu, temizlik yetersizdi. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Oda küçüktü, valiz koyacak alan bile yoktu. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "İnternet sürekli koptu, iş toplantıma giremedim. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Yemekler soğuktu, servis geç geldi. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Havuz kalabalık ve kirli görünüyordu. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Otopark doluydu, araç için yer bulamadık. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Oda servisi geç geldi ve sipariş eksikti. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Fotoğraflardaki otelle gerçek otel arasında büyük fark vardı. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Koridorlar gürültülüydü, odanın ses yalıtımı kötüydü. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Havlular eskiydi, temizlik konusunda güven vermedi. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Çıkış işlemleri yavaştı, gereksiz bekletildik. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Mini bar boştu, oda bakımsız görünüyordu. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Pencere kapanmıyordu, gece soğuk içeri girdi. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Asansör sürekli arızalıydı, katlara çıkmak zor oldu. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Personel sorulara net cevap vermedi, iletişim zayıftı. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Kahvaltı alanı kalabalıktı ve masalar temizlenmemişti. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Duşta sıcak su yoktu, banyo deneyimi kötüydü. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Oda rutubet kokuyordu, duvarlarda lekeler vardı. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Konum merkezi değildi, ulaşım beklediğimizden zordu. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Genel deneyim olumsuzdu, tekrar tercih etmem. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Rezervasyon bilgileri karıştırıldı, odamız geç verildi. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Yatak rahatsızdı, sabah bel ağrısıyla uyandım. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Odada böcek gördük, hijyen ciddi şekilde kötüydü. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Fiyat yüksek ama hizmet vasattı. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Çalışanlar ilgisizdi, şikayetimize dönüş yapılmadı. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Oda havasızdı, pencere küçük ve manzara kötüydü. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Restoran servisi düzensizdi, siparişler karıştı. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Ses yalıtımı zayıftı, yan odadaki konuşmalar duyuluyordu. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Otel eski ve bakımsızdı, yenilenmeye ihtiyacı var. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Temizlik yapılmamıştı, çöp kutusu doluydu. Genel olarak memnun kalmadım ve tavsiye etmem.",
    "Konaklama beklentimizin altında kaldı, tavsiye etmem. Genel olarak memnun kalmadım ve tavsiye etmem."
]


def main():
    DATA_DIR.mkdir(exist_ok=True)

    positive_data = [{"review": review, "sentiment": "positive"} for review in positive_reviews]
    negative_data = [{"review": review, "sentiment": "negative"} for review in negative_reviews]

    df = pd.DataFrame(positive_data + negative_data)
    df.to_csv(DATA_PATH, index=False, encoding="utf-8-sig")

    print(f"Dataset created: {DATA_PATH}")
    print(f"Row count: {len(df)}")
    print(df.head())


if __name__ == "__main__":
    main()