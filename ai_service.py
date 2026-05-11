import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_task_breakdown(task_name):
    """Kütüphane hatalarını aşmak için direkt REST API üzerinden bağlantı kurar."""
    try:
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            return "Hata: API anahtarı sistemde tanımlı değil."

        # Google'ın ana API adresi (v1 sürümü üzerinden, beta değil!)
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={api_key}"

        
        headers = {'Content-Type': 'application/json'}
        
        data = {
            "contents": [{
                "parts": [{"text": f"Kullanıcı şu görevi erteledi: {task_name}. Bunu başlatmak için 3 kısa adım yaz."}]
            }]
        }

        # İsteği gönder
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        # Yanıtı çözümle
        if response.status_code == 200:
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            error_msg = result.get('error', {}).get('message', 'Bilinmeyen hata')
            return f"API Hatası ({response.status_code}): {error_msg}"

    except Exception as e:
        return f"Bağlantı Hatası: {str(e)}"
