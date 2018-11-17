from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class Accounts(object):
    """docstring for Accounts"""
    def __init__(self, arg):
        super(Accounts, self).__init__()
        self.arg = arg

#TODO add queryset and manager afterwards


class AccountDetails(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    slug = models.SlugField(unique=True, blank=True, null=True)

    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        blank=True,
        null=True
    )
    birth_date = models.DateField(("birthdate"),  blank=True, null=True)
    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Plain text, any formatting or links will be removed"),
        unique=False,
        null=True,
        blank=True
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

