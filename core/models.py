from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class BaseModel(models.Model):
    """
    Base abstract model that provides common fields
    Inherited by all of the app models

    @field
    is_active : deactivating instead of delete the record
    """

    created_time = models.DateTimeField(_("created"), auto_now_add=True)
    updated_time = models.DateTimeField(_("updated"), auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    is_active = models.BooleanField(_("active"), default=True)

    class Meta:
        abstract = True
