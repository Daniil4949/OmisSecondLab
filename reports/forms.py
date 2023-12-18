from django.forms import ModelForm

from reports.models import Report


class ReportCreationForm(ModelForm):
    class Meta:
        model = Report
        fields = ("report_type", "report_amount", "description")

    def __init__(self, *args, **kwargs):
        super(ReportCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
