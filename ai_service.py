import os
from google import genai
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()

def get_task_breakdown(task_name):
    try:
        # Google'ın yeni nesil Client yapısı
        client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
        
        # Yeni nesil model çağırma yöntemi
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=f"Kullanıcı şu görevi erteledi: {task_name}. Bunu başlatması için 3 çok kısa adım yaz."
        )
        
        return response.text
    except Exception as e:
        return f"Bağlantı Hatası: {str(e)}"
