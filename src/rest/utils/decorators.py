import functools
from utils.validators import ValidationException


def validate(validator_class):
    def decorator_validate(func):
        @functools.wraps(func)
        def wrapper(api_view, request, *args, **kwargs):

            validator = validator_class(request.data)
            if validator.is_valid():
                kwargs["validated_data"] = validator.validated_data
                return func(api_view, request, *args, **kwargs)
            else:
                raise ValidationException(validator.error)

        return wrapper
    return decorator_validate
