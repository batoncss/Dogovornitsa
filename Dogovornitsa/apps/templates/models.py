from ckeditor.fields import RichTextField
from django.db import models

class Template(models.Model):
    class TemplateCategory(models.TextChoices):
        SALES_CONTRACT = ("sales", "Договор купли продажи")
        RENT_CONTRACT = ("rent", "Договор аренды")
    name = models.CharField('Наименование шаблона', max_length=50, null=False)
    body = RichTextField('Тело шаблона')
    category = models.CharField(choices=TemplateCategory.choices, max_length=10, null=False)

    def __str__(self):
        return f"{self.name}"
