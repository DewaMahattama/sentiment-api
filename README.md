# Scraping Berita & Analisis Sentimen Otomatis

[![Laravel](https://img.shields.io/badge/Laravel-Framework-red)](https://laravel.com/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-IndoBERT-yellow)](https://huggingface.co/)
[![Python](https://img.shields.io/badge/Python-3.9-blue)](https://www.python.org/)

## 🧠 Model

Model yang digunakan adalah IndoBERT yang telah di-fine-tune untuk **analisis sentimen berita**.  
Model ini dapat diunduh langsung dari **Hugging Face Hub**.  

---

## 📚 Library & Framework
 
- [Python](https://www.python.org/)  
- [Transformers (Hugging Face)](https://huggingface.co/transformers/)  
- [Torch](https://pytorch.org/)  
- [Pandas, NumPy, scikit-learn, matplotlib](https://scikit-learn.org/stable/)  

---

## ⚙️ Cara Menjalankan Sistem (Lokal)

1. **Clone repo ini:**
   ```bash
   git clone https://github.com/DewaMahattama/sentiment-api
   cd sentiment-api
2. **Buat Virtual Enviorment** 
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux / MacOS
    venv\Scripts\activate      # Windows
2. **Install Dependensi ini:**
   ```bash
   pip install -r requirements.txt
4. **Ganti model_path**
   ```bash
   model dapat diakses: yeaylow/analisis-berita-indobertp2
3. **Jalankan Rest API**
   ```bash
   python app.py
