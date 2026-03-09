import os
import django
import requests

# Thiết lập môi trường Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from models_viewer.models import HFModel

def fetch_huggingface_models():
    print("Đang lấy dữ liệu từ Hugging Face...")
    # Gọi API lấy 100 model tải nhiều nhất
    url = "https://huggingface.co/api/models?sort=downloads&direction=-1&limit=100"
    response = requests.get(url)
    
    if response.status_code == 200:
        models_data = response.json()
        for item in models_data:
            # Lưu hoặc cập nhật vào database
            HFModel.objects.update_or_create(
                model_id=item.get('id'),
                defaults={
                    'author': item.get('author'),
                    'downloads': item.get('downloads', 0),
                }
            )
        print("Xong! Đã lưu 100 model vào database.")
    else:
        print("Lỗi khi gọi API.")

if __name__ == "__main__":
    fetch_huggingface_models()