import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def _initialize_client():
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY bulunamadı!")
    
    # Doğru ve güncel yapı budur:
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name="gemini-1.5-flash")


def get_task_breakdown(task_name):
    try:
        model = _initialize_client()
        prompt = f"Kullanıcı şu görevi 3 kez erteledi: {task_name}. Lütfen bu göreve başlamasını kolaylaştıracak 3 çok küçük ve basit adım öner."
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI hatası: {str(e)}"
