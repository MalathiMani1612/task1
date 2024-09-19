from django.db import transaction # type: ignore
from django.db.models.signals import post_save # type: ignore
from django.dispatch import receiver # type: ignore
from django.contrib.auth.models import User # type: ignore

# Signal handler
@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("Signal handler is inside a transaction")
    else:
        print("Signal handler is outside a transaction")

# Example of saving a user within a transaction
def save_user():
    with transaction.atomic():
        user = User.objects.create(username='exampleuser')

save_user()
