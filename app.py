import streamlit as st
import ai_service
import task_manager

# Streamlit sayfasını yapılandır
st.set_page_config(
    page_title="ProcrastinAI",
    page_icon="⏰",
    layout="wide"
)

# Başlık ve açıklama
st.title("⏰ ProcrastinAI")
st.markdown("Ertelediğiniz görevleri yönetin ve yapay zeka desteğiyle küçük adımlara bölün!")
st.divider()

# Session state (Veri tabanımız)
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'ai_responses' not in st.session_state:
    st.session_state.ai_responses = {}

# --- GÖREV EKLEME BÖLÜMÜ ---
st.subheader("➕ Yeni Görev Ekle")
col1, col2 = st.columns([4, 1])

with col1:
    task_input = st.text_input(
        label="Görev adını yazın",
        label_visibility="collapsed",
        placeholder="örn: Rapor yazma, İtfaiye kağıdını doldurma..."
    )
with col2:
    add_button = st.button("Ekle", use_container_width=True, type="primary")

if add_button:
    # İşi task_manager'a devret ve sonucu al
    success, message = task_manager.add_task(st.session_state.tasks, task_input)
    if success:
        st.success(message)
        st.rerun() # Sayfayı yenile ki liste güncellensin
    else:
        st.warning(message)

# --- GÖREVLERİ LİSTELEME BÖLÜMÜ ---
st.subheader("📋 Görevleriniz")

if not st.session_state.tasks:
    st.info("Henüz görev eklemediniz. Yukarıdan yeni bir görev ekleyin!")
else:
    for idx, task in enumerate(st.session_state.tasks):
        task_name = task["ad"]
        postponement_count = task["erteleme_sayisi"]
        
        with st.container(border=True):
            col_title, col_complete, col_postpone = st.columns([3, 1, 1])
            
            # 1. Sütun: Başlık ve Durum
            with col_title:
                emoji = "🔴" if postponement_count >= 3 else "🟢" if postponement_count == 0 else "🟡"
                st.markdown(f"**{emoji} {task_name}**")
                st.caption(f"Erteleme sayısı: {postponement_count}")
            
            # 2. Sütun: Tamamla Butonu
            with col_complete:
                if st.button("✅ Tamamla", key=f"complete_{idx}", use_container_width=True):
                    success, msg = task_manager.complete_task(st.session_state.tasks, st.session_state.ai_responses, idx)
                    if success:
                        st.success(msg)
                        st.rerun()
            
            # 3. Sütun: Ertele Butonu
            with col_postpone:
                if st.button("⏸️ Ertele", key=f"postpone_{idx}", use_container_width=True):
                    task_manager.postpone_task(st.session_state.tasks, idx)
                    st.rerun()
            
            # AI YARDIM ALANI (Sadece 3 kere ertelenirse görünür)
            if postponement_count >= 3:
                st.warning("⚠️ **Bu görevi sürekli erteliyorsun!** İşi küçük ve basit adımlara bölerek başlamayı deneyelim mi?")
                
                if st.button("🤖 Yapay Zeka ile Böl", key=f"split_ai_{idx}", use_container_width=True, type="secondary"):
                    try:
                        with st.spinner("🤔 Yapay zeka düşünüyor..."):
                            # İşi ai_service'e devret
                            ai_response = ai_service.get_task_breakdown(task_name)
                            st.session_state.ai_responses[task_name] = ai_response
                            st.rerun()
                    except Exception as e:
                        st.error(f"❌ AI tarafından hata oluştu: {str(e)}\n\nLütfen .env dosyanızdaki API anahtarını kontrol edin.")
            
            # AI Yanıtı Varsa Göster
            if task_name in st.session_state.ai_responses:
                st.info(f"💡 **Yapay Zeka'nın Önerdiği Adımlar:**\n\n{st.session_state.ai_responses[task_name]}")

            # Tamamla Butonu (Görevi Silme) - AI yanıtı varsa onu da temizle
            if st.button("✅ Görevi Tamamla", key=f"tamamla_{idx}", type="primary"):
                # Görevi listeden sil (task_manager'ın içinden)
                task_manager.delete_task(task_name) 
                
                # Eğer bu görevin AI yanıtı varsa ekranı temizlemek için onu da sil
                if task_name in st.session_state.ai_responses:
                    del st.session_state.ai_responses[task_name]
                    
                st.rerun() # Ekranı yenile ki görev uçsun gitsin!
            
            st.divider() # Görevler arasına şık bir çizgi çeker

# Alt kısım
st.divider()
st.markdown("### 💡 İpuçları\n- Bir görev 3 kez ertelendikten sonra yapay zeka desteğini kullanabilirsiniz.\n- Görevleri küçük adımlara bölmek ertelemeyi azaltmanın en etkili yoludur.")
