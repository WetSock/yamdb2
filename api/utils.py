from django.core import mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework_simplejwt.tokens import RefreshToken

from api_yamdb.settings import NOREPLY_YAMDB_EMAIL


def email_is_valid(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def generate_mail(to_email, code):
    mail.send_mail(
        recipient_list=[to_email],
        from_email=NOREPLY_YAMDB_EMAIL,
        subject='Confirmation code fore yamdb.',
        message=f'Your confirmation code: {code}',
        fail_silently=False
    )


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
