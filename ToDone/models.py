from django.contrib.auth import get_user_model
from django.db import models


class BaseModel(models.Model):
    """
    An abstract base class including base fields like created_at and updated_at.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(BaseModel):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
