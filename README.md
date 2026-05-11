# ProcrastinAI - PlanFlow AI Challenge 

Bu proje, İstanbul Sağlık ve Teknoloji Üniversitesi PlanFlow AI Challenge kapsamında geliştirilmiştir.

## Seçilen Problem
**Problem 3: Sürekli Ertelenen Görevler**
Kullanıcıların gözünde büyüyen, karmaşıklaşan veya başlangıç noktası belirsiz olan görevleri tekrar tekrar ertelemesi. Bu döngü, zaman kaybına ve motivasyon düşüşüne neden olmaktadır.

## Çözüm Yaklaşımı
"ProcrastinAI", kullanıcının erteleme döngüsünü tespit eden adaptif bir görev yönetim prototipidir. Bir görev üst üste 3 kez ertelendiğinde sistem zihinsel bariyeri fark eder ve Google Gemini AI entegrasyonu ile devreye girerek, o görevi uygulaması çok kolay 3 "mikro adıma" böler. Amaç suçluluk hissettirmek değil, ilk adımı kolaylaştırmaktır.

## Kullanılan Teknolojiler
* **Python 3**
* **Streamlit:** Hızlı ve etkileşimli kullanıcı arayüzü (UI) için.
* **Google GenAI SDK (gemini-2.5-flash):** Görev parçalama ve eyleme geçirici adım önerileri üretmek için.

## Kurulum Talimatları
Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1. Repoyu bilgisayarınıza indirin veya klonlayın.
2. Gerekli kütüphaneleri yüklemek için terminalde şu komutu çalıştırın:
   ```bash
   pip install streamlit google-generativeai python-dotenv

## Projeyi Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için terminal (veya komut satırı) üzerinden projenin bulunduğu dizine gidin ve şu komutu çalıştırın:

```bash
py -m streamlit run app.py
