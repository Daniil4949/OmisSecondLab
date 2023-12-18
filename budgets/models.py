from django.db import models

from budgets.abstract.models import IBudget
from users.models import UserModel


class Budget(IBudget):
    status = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    goal = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def create_instance(self, *args, **kwargs):
        return Budget.objects.create(**kwargs)

    def get_instance_info(self):
        return str(self.status) + " " + str(self.address) + " " + str(self.goal) + " " + str(self.date)

    def save_info(self):
        self.save()
