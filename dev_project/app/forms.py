from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(
        label='Выберите файл',
        help_text='Загрузить файл'
    )


class FindUser(forms.Form):
    person = forms.CharField(
        label="Введите Имя и Фамилию для поиска"
    )