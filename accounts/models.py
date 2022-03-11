from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

from core.models import CoreModel


class User(AbstractUser,CoreModel):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={"unique": _("A user with that username already exists."),},
        blank=True,
        null=True,
    )
    full_name = models.CharField(_("full name"), max_length=180, 
    blank=True, help_text=_("The name length can't more than 150 charecter"))
    email = models.EmailField(_("email address"), blank=True, null=True)
    user_type = models.CharField(
        _("user type"), max_length=20, default="Customer", blank=True, null=True,
    )
    deafult_address = models.CharField(_("deafult_address"))
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []







