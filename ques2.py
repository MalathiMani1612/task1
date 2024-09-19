import threading
from django.db.models.signals import post_save # type: ignore
from django.dispatch import receiver  # type: ignore
from django.contrib.auth.models import User # type: ignore

# Signal handler
@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")

# Example of saving a user
def save_user():
    print(f"Caller thread: {threading.current_thread().name}")
    user = User.objects.create(username='exampleuser')

save_user()
