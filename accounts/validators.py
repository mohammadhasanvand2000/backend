from django.core import validators
from django.utils.deconstruct import deconstructible
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_iranian_phoneNumber(value):
    if not re.match(r'^09\d{9}$', value):
        raise ValidationError(
            ('لطفا شماره موبایلت رو درست وارد کن '),
        )