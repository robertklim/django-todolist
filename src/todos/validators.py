from django.core.exceptions import ValidationError
from datetime import date

def validate_expires(value):
    if value < date.today():
        raise ValidationError(F"Expire date ({value}) can't be from the past")
