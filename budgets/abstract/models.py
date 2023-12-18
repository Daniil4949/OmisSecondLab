from django.db import models


class IBudget(models.Model):
    class Meta:
        abstract = True

    def create_instance(self, *args, **kwargs):
        raise NotImplementedError

    def get_instance_info(self):
        raise NotImplementedError

    def save_info(self):
        raise NotImplementedError
