from django.db import models
from django.conf import settings


class College(models.Model):
    """Top‑level academic units (e.g. College of Science & Technology)."""

    college_id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "College"

    def __str__(self):
        return self.name


class HODLecturer(models.Model):
    """Link table that assigns a *Lecturer* record to a generated HOD ID.

    ‑  ``hod_id`` is the business/PK used in the source data (e.g. *0016FF*).
    ‑  Each HOD record must point to exactly **one** lecturer; a lecturer can be
       the HOD of **at most** one department, so we make this a *One‑to‑One*
       relationship.
    """

    hod_id = models.CharField(primary_key=True, max_length=8)
    lecturer = models.OneToOneField(
        "Lecturer",
        on_delete=models.PROTECT,
        related_name="hod_record",
    )

    class Meta:
        db_table = "HODLecturer"

    def __str__(self):
        return f"HOD {self.hod_id} – {self.lecturer.full_name}"


class SecretaryLecturer(models.Model):
    """Link table that assigns a *Lecturer* record to a generated Secretary ID."""

    secretary_id = models.CharField(primary_key=True, max_length=8)
    lecturer = models.OneToOneField(
        "Lecturer",
        on_delete=models.PROTECT,
        related_name="secretary_record",
    )

    class Meta:
        db_table = "SecretaryLecturer"

    def __str__(self):
        return f"Secretary {self.secretary_id} – {self.lecturer.full_name}"


class Department(models.Model):
    department_id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=100)
    college = models.ForeignKey(
        College,
        on_delete=models.PROTECT,
        related_name="departments",
    )
    # The department no longer points directly to a *Lecturer* for its HOD or
    # secretary.  Instead, it references the dedicated link tables above.  This
    # keeps role‑specific metadata (the generated IDs) in their own tables and
    # preserves 3‑NF.
    hod = models.ForeignKey(
        "HODLecturer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="departments",
    )
    secretary = models.ForeignKey(
        "SecretaryLecturer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="departments",
    )

    class Meta:
        db_table = "Department"

    def __str__(self):
        return self.name


class Office(models.Model):
    TYPE_STANDARD = "STANDARD"
    TYPE_CUBICLE = "CUBICLE"
    TYPE_LAB = "LABORATORY"

    TYPE_CHOICES = [
        (TYPE_STANDARD, "Standard"),
        (TYPE_CUBICLE, "Cubicle"),
        (TYPE_LAB, "Laboratory"),
    ]

    office_id = models.CharField(primary_key=True, max_length=8)
    office_number = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    floor = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    class Meta:
        db_table = "Office"

    def __str__(self):
        return f"{self.office_number} – {self.location} (Floor {self.floor})"


class Lecturer(models.Model):
    ROLE_LECTURER = "LECTURER"
    ROLE_HOD = "HOD"  # kept for quick filtering; actual role linkage is via *HODLecturer*
    ROLE_SECRETARY = "SECRETARY"  # idem

    ROLE_CHOICES = [
        (ROLE_LECTURER, "Lecturer"),
        (ROLE_HOD, "Head of Department"),
        (ROLE_SECRETARY, "Secretary"),
    ]
    user = models.OneToOneField(          
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="lecturer_profile",
        null=True,                        
        blank=True,
    )
    lecturer_id = models.CharField(primary_key=True, max_length=8)
    full_name = models.CharField(max_length=120)
    office = models.ForeignKey(
        Office,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="lecturers",
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="lecturers",
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = "Lecturer"

    def __str__(self):
        return self.full_name
