from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from  accounts.models import UserAccount

@shared_task
def send_activation_email(subject, message, recipient_email, email_body):
    try:
        send_mail(
            subject,
            message,
            from_email=None,
            recipient_list=[recipient_email],
            html_message=email_body,
        )

        return "Email sent successfully"
    
    except Exception as e:
        return f"Failed to send email: {str(e)}"


@shared_task
def delete_expired_inactive_users():
    threshold_time = timezone.now() - timedelta(minutes=1)
    expired_users = UserAccount.objects.filter(is_active=False, date_joined__lt=threshold_time)
    deleted_count = expired_users.count()
    expired_users.delete()
    print(f"Deleted {deleted_count} expired inactive users.")
    return f"Deleted {deleted_count} expired inactive users."

