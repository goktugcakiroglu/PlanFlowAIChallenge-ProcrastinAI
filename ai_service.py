import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_task_breakdown(task_name):
    try:
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            return "Hata: API anahtarı tanımlı değil."

        # v1beta genelde yeni anahtarlarla daha iyi çalışır
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        
        headers = {'Content-Type': 'application/json'}
        data = {
            "contents": [{
                "parts": [{"text": f"Görev: {task_name}. Bu görevi başlatmak için 3 kısa adım yaz."}]
            }]
        }

        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if response.status_code == 200:
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"API Hatası ({response.status_code}): {result.get('error', {}).get('message')}"

    except Exception as e:
        return f"Bağlantı Hatası: {str(e)}"
