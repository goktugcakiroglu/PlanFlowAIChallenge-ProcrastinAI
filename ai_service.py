import os
import google.generativeai as genai
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()

def _initialize_client():
    """
    Gemini modelini yapılandırır ve döndürür. 
    Bu fonksiyonun dışarıdan erişilebilir olması diğer dosyaların için kritiktir.
    """
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        # Streamlit Cloud üzerinde Secrets kısmına GEMINI_API_KEY eklediğinden emin ol
        raise ValueError("GEMINI_API_KEY bulunamadı!")
    
    # Çift dikiş yapılandırma
    genai.configure(api_key=api_key)
    os.environ["GOOGLE_API_KEY"] = api_key 
    
    return genai.GenerativeModel('gemini-1.5-flash')

def get_task_breakdown(task_name):
    """Görevi mikro adımlara böler."""
    try:
        # Eksik olan fonksiyonu burada çağırıyoruz
        model = _initialize_client()
        
        prompt = (
            f"Kullanıcı şu görevi tamamlamakta zorlanıyor: {task_name}. "
            f"Lütfen bu göreve başlamasını sağlayacak çok kısa ve motive edici 3 mikro adım yaz."
        )
        
        response = model.generate_content(prompt)
        
        if response.text:
            return response.text
        return "Yapay zeka yanıt üretti ancak metin boş geldi."
            
    except Exception as e:
        # 404 v1beta hatası devam ederse jüriye teknik ama kibar bir mesaj gösterir
        return f"Bağlantı Hatası: {str(e)}"
