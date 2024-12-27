from django.forms import TextInput, ModelForm, ValidationError, CharField
from .models import Participant

class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        widgets = {
            # 'name': TextInput(attrs={'class': 'form-control'}),
            'legal_address': TextInput(attrs={'class': 'form-control'}),
            'actual_address': TextInput(attrs={'class': 'form-control'}),
            'inn': TextInput(attrs={'class': 'form-control'}),
            'kpp': TextInput(attrs={'class': 'form-control'}),
            'ogrn': TextInput(attrs={'class': 'form-control'}),
        }
        fields = [
            'name',
            'legal_address',
            'actual_address',
            'inn',
            'kpp',
            'ogrn',
        ]
    name = CharField(
        error_messages={'required': 'Пожалуйста введите ваше имя'},
        widget=TextInput(attrs={'class': 'form-control'}),
        label="Имя участника договора"
    )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     errors_dict = dict(self.errors)
    #     for field, field_errors in errors_dict.items():
    #         for i, error in enumerate(field_errors):
    #             if error == 'This field is required.':
    #                 errors_dict[field][i] = f'Параметр не может быть пустым'
    #     return cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Participant.objects.filter(name=name).exists():
            raise ValidationError('Участник с таким именем уже зарегистрирован')
        return name

    def clean_inn(self):
        inn = self.cleaned_data.get('inn')
        if Participant.objects.filter(name=inn).exists():
            raise ValidationError('Участник с таким ИНН уже зарегистрирован')
        if len(inn) not in (10, 12):
            raise ValidationError('ИНН должен состоять из 10 или 12 цифр')
        if not inn.isdigit():
            raise ValidationError('ИНН должен содержать только цифры')
        return inn

    def clean_kpp(self):
        kpp = self.cleaned_data.get('kpp')
        if Participant.objects.filter(name=kpp).exists():
            raise ValidationError('Участник с таким КПП уже зарегистрирован')
        if len(kpp) != 9:
            raise ValidationError('КПП должен состоять из 9 цифр')
        if not kpp.isdigit():
            raise ValidationError('КПП должен содержать только цифры')
        return kpp

    def clean_ogrn(self):
        ogrn = self.cleaned_data.get('ogrn')
        if Participant.objects.filter(name=ogrn).exists():
            raise ValidationError('Участник с таким ОГРН уже зарегистрирован')
        if len(ogrn) != 15:
            raise ValidationError('КПП должен состоять из 15 цифр')
        if not ogrn.isdigit():
            raise ValidationError('КПП должен содержать только цифры')
        return ogrn