import os
import google.generativeai as genai
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()

def _initialize_client():
    """Gemini modelini yapılandırır ve döndürür."""
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY ortam değişkeni bulunamadı!")
    
    # Yeni kütüphane yapısına uygun yapılandırma
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('models/gemini-1.5-flash')


def get_task_breakdown(task_name):
    """Görevi mikro adımlara böler."""
    try:
        model = _initialize_client()
        prompt = (
            f"Kullanıcı şu görevi 3 kez erteledi: {task_name}. "
            f"Lütfen bu göreve başlamasını kolaylaştıracak 3 çok küçük ve basit adım öner."
        )
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Hata oluştu: {str(e)}"
