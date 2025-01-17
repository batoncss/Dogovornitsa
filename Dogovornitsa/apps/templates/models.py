from ckeditor.fields import RichTextField
from django.db import models

class Template(models.Model):
    name = models.CharField('Наименование шаблона', max_length=50, null=False)
    body = RichTextField('Тело шаблона')
    def __str__(self):
        return f"{self.name}"
