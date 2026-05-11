import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Bazı ortamlar için API anahtarını çift dikiş tanımlayalım
api_key = os.environ.get('GEMINI_API_KEY')
if api_key:
    genai.configure(api_key=api_key)

def get_task_breakdown(task_name):
    try:
        # Modeli burada tanımlamak bağlantı hatalarını azaltabilir
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"{task_name} görevini tamamlamam için bana 3 çok kısa adım söyle."
        
        response = model.generate_content(prompt)
        
        if response.text:
            return response.text
        else:
            return "Yapılandırılmış bir yanıt alınamadı."
            
    except Exception as e:
        # Hatayı daha detaylı görelim ki neyle savaştığımızı bilelim
        return f"Bağlantı Hatası: {str(e)}"
