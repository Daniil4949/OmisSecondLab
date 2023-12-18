from django.forms import ModelForm

from users.models import UserModel


class UserModelCreationForm(ModelForm):
    '''Форма регистрации Пользователя, поля такие же как в модели'''

    class Meta:
        model = UserModel
        fields = ("username", "first_name", "last_name", "password", "budget")

    def __init__(self, *args, **kwargs):
        super(UserModelCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
