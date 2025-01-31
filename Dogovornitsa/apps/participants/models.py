from django.db import models

class Participant(models.Model):
    name = models.CharField('Наименование клиента', max_length=50)
    legal_address = models.CharField('Юридический адрес', max_length=50)
    actual_address = models.CharField('Фактический адрес', max_length=50)
    inn = models.CharField('ИНН', max_length=12)
    kpp = models.CharField('КПП', max_length=9)
    ogrn = models.CharField('ОГРН', max_length=13)

    def __str__(self):
        return f"{self.name} (ИНН: {self.inn})"