# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Lecturer

@receiver(post_save, sender=Lecturer)
def ensure_user_for_lecturer(sender, instance, created, **kwargs):
    if created and not instance.user:
        user = User.objects.create_user(
            username=instance.lecturer_id,
            password="change-me-now!",
            first_name=instance.full_name.split()[0],
            last_name=" ".join(instance.full_name.split()[1:]),
            is_staff=True,
        )
        instance.user = user
        instance.save()
