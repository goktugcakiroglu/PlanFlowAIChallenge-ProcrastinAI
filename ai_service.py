import os
from dotenv import load_dotenv
from google import genai

# Ortam değişkenlerini sadece bu modül yüklüyor
load_dotenv()

def _initialize_client():
    """Gizli bir yardımcı fonksiyon: İstemciyi oluşturur."""
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY ortam değişkeni bulunamadı! Lütfen .env dosyanızı kontrol edin.")
    return genai.Client(api_key=api_key)

def get_task_breakdown(task_name):
    """
    Dışarıya (app.py'ye) açılan ana fonksiyon.
    Görev adını alır, yapay zekaya sorar ve dönen metni string olarak geri verir.
    """
    client = _initialize_client()
    
    prompt = (
        f"Kullanıcı şu görevi 3 kez erteledi: {task_name}. "
        f"Lütfen bu göreve başlamasını kolaylaştıracak 3 çok küçük ve basit adım öner."
    )
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    return response.text