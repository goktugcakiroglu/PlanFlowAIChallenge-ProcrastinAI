def add_task(tasks_list, task_name):
    """
    Yeni görev ekler. 
    Dönüş değeri: (Başarılı mı? (bool), Mesaj (str))
    """
    task_name = task_name.strip()
    
    if not task_name:
        return False, "Lütfen bir görev adı girin!"
    
    # Aynı isimde görev var mı kontrolü
    if any(task["ad"] == task_name for task in tasks_list):
        return False, "⚠️ Bu görev zaten listede var!"
        
    # Yeni görevi listeye ekle
    tasks_list.append({
        "ad": task_name,
        "erteleme_sayisi": 0
    })
    return True, f"✅ '{task_name}' görevi eklendi!"

def complete_task(tasks_list, ai_responses_dict, index):
    """
    Görevi tamamlar (listeden siler) ve o göreve ait bir AI yanıtı varsa temizler.
    """
    if 0 <= index < len(tasks_list):
        task_name = tasks_list[index]["ad"]
        tasks_list.pop(index)
        
        # Eğer bu görev için üretilmiş bir AI tavsiyesi varsa, belleği temizle
        if task_name in ai_responses_dict:
            del ai_responses_dict[task_name]
            
        return True, f"🎉 '{task_name}' tamamlandı!"
    return False, "Görev bulunamadı."

def postpone_task(tasks_list, index):
    """
    Görevin erteleme sayısını 1 artırır.
    """
    if 0 <= index < len(tasks_list):
        tasks_list[index]["erteleme_sayisi"] += 1
        return True
    return False