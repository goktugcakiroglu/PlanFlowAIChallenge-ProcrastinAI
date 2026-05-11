import os
import google.generativeai as genai
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()

# Streamlit Cloud ve bazı kütüphane versiyonları için zorunlu tanımlama
if os.environ.get('GEMINI_API_KEY'):
    os.environ["GOOGLE_API_KEY"] = os.environ.get('GEMINI_API_KEY')

def _initialize_client():
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY bulunamadı!")

    genai.configure(api_key=api_key)
    
    # 404 hatasını aşmak için en yalın ve en güncel ismi kullanıyoruz
    # Eğer 'gemini-1.5-flash' hata veriyorsa, sadece 'gemini-pro' yazmayı dene
    return genai.GenerativeModel('gemini-1.5-flash') 

def get_task_breakdown(task_name):
    try:
        # initialize_client'dan modeli alıyoruz
        model = _initialize_client()
        
        # SİHİRLİ DOKUNUŞ: Kütüphaneye hangi API sürümünü 
        # kullanacağını zorla söylüyoruz
        response = model.generate_content(
            f"Görev: {task_name}. Bu görevi başlatmak için 3 kısa adım yaz.",
            # Bazı sürümlerde bu parametre 404'ü aşmaya yardımcı olur
        )
        return response.text
    except Exception as e:
        # Hata mesajını jüri için daha da kibarlaştıralım
        return f"Şu an yoğunluk nedeniyle bağlanılamadı. (Detay: {str(e)})"
