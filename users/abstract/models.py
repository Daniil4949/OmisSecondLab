from django.db import models


class IUser(models.Model):
    class Meta:
        abstract = True

    def get_password(self):
        raise NotImplementedError

    def get_fullname(self):
        raise NotImplementedError

    def create_user(self, email, password):
        raise NotImplementedError

    def get_user_info(self):
        raise NotImplementedError
