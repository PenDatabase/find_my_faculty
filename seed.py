#!/usr/bin/env python
"""
Seed the database with data for the “Students Find Lecturers” app.
"""

import os
from django.db import transaction

# ──────────────────────────────────────────────────────────────────────────────
# Django setup – adjust the DJANGO_SETTINGS_MODULE to your project’s settings
# ──────────────────────────────────────────────────────────────────────────────
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base_project.settings")
import django

django.setup()

from find_my_lecturer_app.models import (
    College,
    Department,
    Office,
    Lecturer,
    HODLecturer,
    SecretaryLecturer,
)


@transaction.atomic
def populate_database():
    # Step 1: Populate College table
    colleges = [
        {"college_id": "CST001", "name": "College of Science and Technology"},
        {"college_id": "CMSS001", "name": "College of Management Social Sciences"},
        {"college_id": "C0E003", "name": "College of Engineering"},
        {"college_id": "CLDS004", "name": "College of Leadership Development Studies"},
    ]
    for college_data in colleges:
        College.objects.get_or_create(**college_data)

    # Step 2: Populate Office table
    offices = [
        {"office_id": "0123AC", "office_number": "A316", "location": "CST Building", "floor": 300, "type": Office.TYPE_STANDARD},
        {"office_id": "0124AD", "office_number": "A314", "location": "CST Building", "floor": 300, "type": Office.TYPE_STANDARD},
        {"office_id": "0125AF", "office_number": "A310", "location": "CST Building", "floor": 300, "type": Office.TYPE_STANDARD},
        {"office_id": "0126AG", "office_number": "A306", "location": "CST Building", "floor": 300, "type": Office.TYPE_STANDARD},
        {"office_id": "0127BA", "office_number": "CIS Dept. Office A (Right)", "location": "CST Building", "floor": 300, "type": Office.TYPE_CUBICLE},
        {"office_id": "0128BB", "office_number": "CIS Dept. Office C (Middle)", "location": "CST Building", "floor": 300, "type": Office.TYPE_CUBICLE},
        {"office_id": "0129BC", "office_number": "CIS Dept. Office B (Right)", "location": "CST Building", "floor": 300, "type": Office.TYPE_CUBICLE},
        {"office_id": "0130BD", "office_number": "Center of Information and Technology", "location": "CST Building", "floor": 300, "type": Office.TYPE_STANDARD},
        {"office_id": "0131BE", "office_number": "Center of Info & Tech", "location": "CST Building", "floor": 300, "type": Office.TYPE_STANDARD},
        {"office_id": "0132CA", "office_number": "Software Eng. Lab, 200 Floor", "location": "CST Building", "floor": 200, "type": Office.TYPE_LAB},
        {"office_id": "0133CB", "office_number": "A315", "location": "CST Building", "floor": 300, "type": Office.TYPE_STANDARD},
        {"office_id": "0134CC", "office_number": "A320", "location": "CST Building", "floor": 300, "type": Office.TYPE_STANDARD},
        {"office_id": "0135CD", "office_number": "D105", "location": "CMSS", "floor": 100, "type": Office.TYPE_STANDARD},
    ]
    for office_data in offices:
        Office.objects.get_or_create(**office_data)

    # Step 3: Populate Department table (without HOD and Secretary initially)
    departments = [
        {"department_id": "012AC", "name": "C.I.S", "college_id": "CST001"},
        {"department_id": "013AD", "name": "Mathematics", "college_id": "CST001"},
        {"department_id": "014AF", "name": "Biology", "college_id": "CST001"},
        {"department_id": "015AG", "name": "Physics", "college_id": "CST001"},
        {"department_id": "015GT", "name": "Estate Management", "college_id": "CST001"},
        {"department_id": "015AU", "name": "Architecture", "college_id": "CST001"},
    ]
    for dept_data in departments:
        college = College.objects.get(college_id=dept_data["college_id"])
        Department.objects.get_or_create(
            department_id=dept_data["department_id"],
            name=dept_data["name"],
            college=college
        )

    # Step 4: Populate Lecturer table
    lecturers = [
        {"lecturer_id": "00010AI", "full_name": "Miss Adeleke Ti-Jesu", "office_id": "0123AC", "department_id": "012AC", "role": Lecturer.ROLE_LECTURER, "notes": "CIS, CST Building, 300 Floor"},
        {"lecturer_id": "00011AJ", "full_name": "Miss Ade Nathanael Jemimah", "office_id": "0123AC", "department_id": "012AC", "role": Lecturer.ROLE_LECTURER, "notes": "CIS, CST Building, 300 Floor"},
        {"lecturer_id": "00012AK", "full_name": "Mr Henry Ogbu", "office_id": "0124AD", "department_id": "012AC", "role": Lecturer.ROLE_LECTURER, "notes": "CIS, CST Building"},
        {"lecturer_id": "00013AL", "full_name": "Prof C.O. Ikoham", "office_id": "0125AF", "department_id": "012AC", "role": Lecturer.ROLE_LECTURER, "notes": "CIS, CST Building"},
        {"lecturer_id": "00014AM", "full_name": "Mr Damilola Odunayo", "office_id": "0126AG", "department_id": "012AC", "role": Lecturer.ROLE_LECTURER, "notes": "CIS, CST Building"},
        {"lecturer_id": "00015AN", "full_name": "Mr Tope Jegede", "office_id": "0127BA", "department_id": "012AC", "role": Lecturer.ROLE_LECTURER, "notes": "Shared space"},
        {"lecturer_id": "00016BA", "full_name": "Mr Ibickpo Dada", "office_id": "0127BA", "department_id": "012AC", "role": Lecturer.ROLE_LECTURER, "notes": "Shared space"},
        {"lecturer_id": "00017BB", "full_name": "Mr Ejiboh Chukuebuka", "office_id": "0128BB", "department_id": "012AC", "role": Lecturer.ROLE_LECTURER, "notes": "Shared space"},
        {"lecturer_id": "00018BC", "full_name": "Mrs Abiodun Theisah", "office_id": "0129BC", "department_id": "012AC", "role": Lecturer.ROLE_LECTURER, "notes": "Shared space"},
        {"lecturer_id": "00019BD", "full_name": "Mr Franklyn Emmanuel", "office_id": None, "department_id": "012AC", "role": Lecturer.ROLE_LECTURER, "notes": "CIS Dept. Office E (Right), Shared space"},
        {"lecturer_id": "00020BE", "full_name": "Prof Oni Atinuke", "office_id": "0130BD", "department_id": "012AC", "role": Lecturer.ROLE_HOD, "notes": "HOD"},
        {"lecturer_id": "00021CC", "full_name": "Mrs Comfort Olamilekan", "office_id": "0131BE", "department_id": "012AC", "role": Lecturer.ROLE_SECRETARY, "notes": "Secretary"},
        {"lecturer_id": "00022CD", "full_name": "Mr Otavie Okuyo", "office_id": "0132CA", "department_id": "012AC", "role": Lecturer.ROLE_LECTURER, "notes": "Not in 300 Floor"},
        {"lecturer_id": "00023CE", "full_name": "Dr Babalola D.O", "office_id": "0133CB", "department_id": "012AC", "role": Lecturer.ROLE_LECTURER, "notes": "CIS, CST Building"},
        {"lecturer_id": "00024CH", "full_name": "Dr Sholauke A.B", "office_id": "0134CC", "department_id": "012AC", "role": Lecturer.ROLE_LECTURER, "notes": "CIS, CST Building"},
        {"lecturer_id": "00025DA", "full_name": "Dr Oluranti Jonathan", "office_id": "0135CD", "department_id": None, "role": Lecturer.ROLE_LECTURER, "notes": "Not in CST building"},
    ]
    for lecturer_data in lecturers:
        office = Office.objects.get(office_id=lecturer_data["office_id"]) if lecturer_data["office_id"] else None
        department = Department.objects.get(department_id=lecturer_data["department_id"]) if lecturer_data["department_id"] else None
        Lecturer.objects.get_or_create(
            lecturer_id=lecturer_data["lecturer_id"],
            full_name=lecturer_data["full_name"],
            office=office,
            department=department,
            role=lecturer_data["role"],
            notes=lecturer_data["notes"]
        )

    # Step 5: Populate HODLecturer and SecretaryLecturer tables
    hod_lecturers = [
        {"hod_id": "0016FF", "lecturer_id": "00020BE"},
    ]
    for hod_data in hod_lecturers:
        lecturer = Lecturer.objects.get(lecturer_id=hod_data["lecturer_id"])
        HODLecturer.objects.get_or_create(
            hod_id=hod_data["hod_id"],
            lecturer=lecturer
        )

    secretary_lecturers = [
        {"secretary_id": "0016AF", "lecturer_id": "00021CC"},
    ]
    for secretary_data in secretary_lecturers:
        lecturer = Lecturer.objects.get(lecturer_id=secretary_data["lecturer_id"])
        SecretaryLecturer.objects.get_or_create(
            secretary_id=secretary_data["secretary_id"],
            lecturer=lecturer
        )

    # Step 6: Update Department table with HOD and Secretary
    department_updates = [
        {"department_id": "012AC", "hod_id": "0016FF", "secretary_id": "0016AF"},
        {"department_id": "013AD", "hod_id": None, "secretary_id": None},
        {"department_id": "014AF", "hod_id": None, "secretary_id": None},
        {"department_id": "015AG", "hod_id": None, "secretary_id": None},
        {"department_id": "015GT", "hod_id": None, "secretary_id": None},
        {"department_id": "015AU", "hod_id": None, "secretary_id": None},
    ]
    for update in department_updates:
        department = Department.objects.get(department_id=update["department_id"])
        department.hod = HODLecturer.objects.get(hod_id=update["hod_id"]) if update["hod_id"] else None
        department.secretary = SecretaryLecturer.objects.get(secretary_id=update["secretary_id"]) if update["secretary_id"] else None
        department.save()

if __name__ == "__main__":
    populate_database()