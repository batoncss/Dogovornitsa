from ckeditor.fields import RichTextField
from django.db import models

class Template(models.Model):
    name = models.CharField('Наименование шаблона', max_length=50, null=False)
    body = RichTextField('Тело шаблона')  # Устанавливаем пустое значение по умолчанию
