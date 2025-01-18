from django.db import models

class Participant(models.Model):
    name = models.CharField('Наименование клиента', max_length=50, null=True, default=None)
    legal_address = models.CharField('Юридический адрес', max_length=50, null=True, default=None)
    actual_address = models.CharField('Фактический адрес', max_length=50, null=True, default=None)
    inn = models.CharField('ИНН', null=True, default="", max_length=12, unique=True)
    kpp = models.CharField('КПП', null=True, default=None, max_length=9)
    ogrn = models.CharField('ОГРН', null=True, default=None, max_length=15)

    def __str__(self):
        return f"{self.name} (ИНН: {self.inn})"