from django.db import models
from config.models import BasedModel

class Item(BasedModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
