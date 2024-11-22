from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from app.models import CustomUser


def send_registration_email(user : CustomUser):
    subject = "Successfully registration Email"
    html_message = render_to_string('email_reg_body.html',{
            "username" : user.username.capitalize(),
    })
    message = strip_tags(html_message)
    email = EmailMultiAlternatives(
            subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email]
        )
    email.attach_alternative(html_message, "text/html")
    email.send()