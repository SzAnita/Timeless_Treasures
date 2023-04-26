import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class NumberValidator:
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("The password must contain at least 1 digit, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 digit, 0-9.")

class UpperCaseValidator:
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(_("The password must contain at least 1 uppercase letter"))

    def get_help_text(self):
        return _("Your password must contain at least 1 uppercase letter")

class SymbolValidator:
    def validate(self, password, user=None):
        if not re.findall('[!@#$%^&*,._+=(){}/?-]', password):
            raise ValidationError(_("The password must contain at least 1 symbol: !@#$%^&*,._+={}/?-"))