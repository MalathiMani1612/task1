import time
from django.db.models.signals import post_save # type: ignore
from django.dispatch import receiver # type: ignore
from django.contrib.auth.models import User # type: ignore

# Signal handler
@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print("Signal handler starts")
    time.sleep(5)  # Simulate long-running operation
    print("Signal handler ends")

# Example of saving a user
user = User.objects.create(username='exampleuser')
