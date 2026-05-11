import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def get_task_breakdown(task_name):
    try:
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            return "Hata: API anahtarı tanımlı değil."

        # Yeni kütüphane yapısı
        client = genai.Client(api_key=api_key)
        
        # KRİTİK NOKTA: model isminin başına 'models/' ekleyerek 
        # ve sade bir istek göndererek v1beta hatasını aşmayı deniyoruz.
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=f"Görevi 3 küçük adıma böl: {task_name}"
        )
        
        return response.text

    except Exception as e:
        # Eğer hala 404 verirse, model ismini 'gemini-pro' olarak değiştirmeyi deneyeceğiz.
        return f"Bağlantı Hatası: {str(e)}"
