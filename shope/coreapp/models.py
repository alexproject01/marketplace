from django.db import models


class BaseModel(models.Model):
    """
    Класс базовой модели
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()

    class Meta:
        abstract = True
