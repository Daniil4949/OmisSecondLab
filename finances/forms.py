from django.forms import ModelForm

from finances.models import FinanceOperation


class FinanceOperationCreationForm(ModelForm):

    class Meta:
        model = FinanceOperation
        fields = ("operation_type", "amount")

    def __init__(self, *args, **kwargs):
        super(FinanceOperationCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
