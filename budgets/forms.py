from django.forms import ModelForm

from budgets.models import Budget


class BudgetCreationForm(ModelForm):
    class Meta:
        model = Budget
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BudgetCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
