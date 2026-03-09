from django.contrib import admin
from .models import HFModel

@admin.register(HFModel)
class HFModelAdmin(admin.ModelAdmin):
    list_display = ('model_id', 'author', 'downloads') # Các cột hiển thị
    search_fields = ('model_id', 'author')           # Thanh tìm kiếm