from django.db import models

from reports.abstract.models import IReport
from users.models import UserModel


class Report(IReport):
    report_type = models.CharField(max_length=10)
    description = models.TextField()
    report_amount = models.IntegerField()


    def create_instance(self, *args, **kwargs):
        return Report.objects.create(**kwargs)

    def get_instance_info(self):
        return str(self.id) + " " + str(self.report_type) + " " + str(self.report_amount) + " " + str(self.description)

    def save_info(self):
        self.save()
