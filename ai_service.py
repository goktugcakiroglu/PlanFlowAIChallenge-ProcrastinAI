import os
import google.generativeai as genai
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()

# Streamlit Cloud ve bazı kütüphane versiyonları için zorunlu tanımlama
if os.environ.get('GEMINI_API_KEY'):
    os.environ["GOOGLE_API_KEY"] = os.environ.get('GEMINI_API_KEY')

def _initialize_client():
    """Gemini modelini yapılandırır ve döndürür."""
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY ortam değişkeni bulunamadı!")

    genai.configure(api_key=api_key)
    
    # En stabil model ismini seçiyoruz
    return genai.GenerativeModel('gemini-1.5-flash')

def get_task_breakdown(task_name):
    """Görevi mikro adımlara böler."""
    try:
        model = _initialize_client()
        prompt = (
            f"Kullanıcı şu görevi 3 kez erteledi: {task_name}. "
            f"Lütfen bu göreve başlamasını kolaylaştıracak 3 çok küçük ve basit adım öner. "
            f"Yanıtın sadece adımları içersin."
        )

        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Hata oluştu: {str(e)}"
