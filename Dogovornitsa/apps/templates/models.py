from django_ckeditor_5.fields import CKEditor5Field
from django.db import models


class Template(models.Model):
    class TemplateCategory(models.TextChoices):
        SALES_CONTRACT = ("sales", "Договор купли-продажи")
        RENT_CONTRACT = ("rent", "Договор аренды")

    name = models.CharField("Наименование шаблона", max_length=50)
    body = CKEditor5Field("Тело шаблона", config_name="default")
    category = models.CharField(
        choices=TemplateCategory.choices,
        max_length=10,
    )

    def __str__(self):
        return self.name
