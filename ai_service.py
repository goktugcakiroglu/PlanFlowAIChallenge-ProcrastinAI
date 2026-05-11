import os
from google import genai
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()

def get_task_breakdown(task_name):
    """Görevi mikro adımlara bölen tek ve ana fonksiyon."""
    try:
        # API Anahtarını Secrets'tan veya .env'den al
        api_key = os.environ.get('GEMINI_API_KEY')
        
        if not api_key:
            return "Hata: API anahtarı sistemde tanımlı değil."

        # Yeni kütüphane yapısıyla bağlantıyı başlat
        client = genai.Client(api_key=api_key)
        
        # İstek gönder (En sade ve hızlı haliyle)
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=f"Kullanıcı şu görevi erteledi: {task_name}. Bu göreve başlamasını sağlamak için 3 çok kısa ve somut adım yaz."
        )
        
        return response.text

    except Exception as e:
        # Hata olursa arayüzde 'Bağlantı Hatası' olarak görünür
        return f"Bağlantı Hatası: {str(e)}"
