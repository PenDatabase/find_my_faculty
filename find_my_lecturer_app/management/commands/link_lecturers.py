# management/commands/link_lecturer_users.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from find_my_lecturer_app.models import Lecturer

class Command(BaseCommand):
    help = "Create/attach auth.User accounts for each Lecturer"

    def handle(self, *args, **kwargs):
        created, linked = 0, 0
        for lec in Lecturer.objects.all():
            if lec.user:
                linked += 1
                continue
            user, _ = User.objects.get_or_create(
                username=lec.lecturer_id,          # login = lecturer_id
                defaults={
                    "first_name":  lec.full_name.split()[0],
                    "last_name":   " ".join(lec.full_name.split()[1:]),
                    "is_staff":    True,           # let them use admin, optional
                    "is_active":   True,
                },
            )
            user.set_password("change-me-now!")    # force change at first login
            user.save()
            lec.user = user
            lec.save()
            created += 1
        self.stdout.write(
            self.style.SUCCESS(f"Created {created} users, linked {linked} existing.")
        )
