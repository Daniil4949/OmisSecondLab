from django.db import models
from django.contrib.auth.models import User, AbstractUser

from users.abstract.models import IUser


class UserModel(AbstractUser):
    """
    Бухгалтер
    """
    budget = models.IntegerField(null=True)

    # activity_set создается автоматически

    # def change_fullname(self, new_full_name: str):
    #     self.fullname = new_full_name
    #
    #     self.save()

    def change_budget(self, budget: int):
        self.budget = budget
        self.save()

    def get_password(self):
        return self.password

    # def get_fullname(self):
    #     return self.fullname

    def get_budget(self):
        return self.budget
