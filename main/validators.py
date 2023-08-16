import re

from rest_framework.serializers import ValidationError


def validate_link(value):
    """ Проверка содержимого на наличие недопустимых ссылок """

    pattern = r'(https?://)?(www\.)?youtube\.com'
    if not re.search(pattern, value):
        raise ValidationError("Недопустимая ссылка")
    return value