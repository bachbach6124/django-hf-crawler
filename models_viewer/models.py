from django.db import models

class HFModel(models.Model):
    model_id = models.CharField(max_length=255, unique=True) # Tên model trên Hugging Face
    author = models.CharField(max_length=255, null=True, blank=True)
    downloads = models.IntegerField(default=0)
    last_modified = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.model_id