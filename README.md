# ProcrastinAI - PlanFlow AI Challenge 

Bu proje, İstanbul Sağlık ve Teknoloji Üniversitesi PlanFlow AI Challenge kapsamında geliştirilmiştir.

## Seçilen Problem
**Problem 3: Sürekli Ertelenen Görevler**
Kullanıcıların gözünde büyüyen, karmaşıklaşan veya başlangıç noktası belirsiz olan görevleri tekrar tekrar ertelemesi. Bu döngü, zaman kaybına ve motivasyon düşüşüne neden olmaktadır.

## Çözüm Yaklaşımı
"ProcrastinAI", kullanıcının erteleme döngüsünü tespit eden adaptif bir görev yönetim prototipidir. Bir görev üst üste 3 kez ertelendiğinde sistem zihinsel bariyeri fark eder ve Google Gemini 2.5 Flash entegrasyonu ile devreye girerek, o görevi uygulaması çok kolay 3 "mikro adıma" böler. Amaç kullanıcıya suçluluk hissettirmek değil, ilk adımı kolaylaştırmaktır.

## Kullanılan Teknolojiler
* **Python 3**
* **Streamlit:** Hızlı ve etkileşimli kullanıcı arayüzü (UI) için.
* **Google Gemini REST API:** Görev parçalama ve eyleme geçirici adım önerileri üretmek için (requests kütüphanesi ile doğrudan API haberleşmesi).
* **python-dotenv:** Çevresel değişkenleri ve API anahtarını güvenli bir şekilde yönetmek için.
## Kurulum Talimatları
Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1. Repoyu bilgisayarınıza indirin veya klonlayın.
2. Gerekli kütüphaneleri yüklemek için terminalde şu komutu çalıştırın:
   ```bash
   pip install streamlit google-generativeai python-dotenv
   ```
3. Projenin ana dizininde bir .env dosyası oluşturun ve Gemini API anahtarınızı içine ekleyin:
   ```env
   GEMINI_API_KEY=sizin_api_anahtariniz_buraya
   ```
## Streamlit Cloud Üzerinde Çalıştırma (Deploy) İçin:

Proje Streamlit Cloud'a yüklendiğinde, API anahtarı güvenli bir şekilde Streamlit Secrets üzerinden yönetilmektedir. Jürinin kendi Cloud ortamında test edebilmesi için, uygulamanın yönetim panelinden (Advanced Settings -> Secrets) anahtar aşağıdaki formatta eklenmelidir:
   ```toml
   GEMINI_API_KEY="sizin_api_anahtariniz_buraya"
   ```
## Projeyi Çalıştırma
Projeyi kendi bilgisayarınızda çalıştırmak için terminal (veya komut satırı) üzerinden projenin bulunduğu dizine gidin ve şu komutu çalıştırın:

   ```bash
   py -m streamlit run app.py
   ```
