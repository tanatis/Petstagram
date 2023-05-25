from django.core.exceptions import ValidationError


def validate_image_less_than_5mb(image):
    if image.size > 5242880:
        raise ValidationError(f'Max file size id 5MB')
