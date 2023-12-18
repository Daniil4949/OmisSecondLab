from django.db import models

from finances.abstract.models import IFinanceOperation
from users.models import UserModel


class FinanceOperation(IFinanceOperation):
    operation_type = models.CharField(max_length=10)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def create_instance(self, *args, **kwargs):
        return FinanceOperation.objects.create(**kwargs)

    def get_instance_info(self):
        return str(self.operation_type) + " " + str(self.user.id) + " " + str(self.amount)

    def save_info(self):
        self.save()
