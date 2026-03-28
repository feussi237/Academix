from django.core.management.base import BaseCommand
from student_management.models import Student
from datetime import date
import random

class Command(BaseCommand):
    help = 'Populate database with sample student data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=20,
            help='Number of sample students to create',
        )

    def handle(self, *args, **options):
        count = options['count']

        first_names = [
            'Alice', 'Bob', 'Charlie', 'Diana', 'Edward', 'Fiona', 'George', 'Helen',
            'Ian', 'Julia', 'Kevin', 'Laura', 'Michael', 'Nancy', 'Oliver', 'Paula',
            'Quincy', 'Rachel', 'Steven', 'Tina', 'Ursula', 'Victor', 'Wendy', 'Xavier',
            'Yasmine', 'Zachary'
        ]

        last_names = [
            'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller',
            'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez',
            'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin'
        ]

        academic_levels = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 's1', 's2', 's3', 's4', 's5', 's6']
        enrollment_statuses = ['active', 'transferred', 'dismissed', 'graduated']

        students_created = 0

        for i in range(count):
            # Generate random birth date (between 6 and 18 years old)
            birth_year = random.randint(2006, 2018)
            birth_month = random.randint(1, 12)
            birth_day = random.randint(1, 28)  # Avoid invalid dates
            birth_date = date(birth_year, birth_month, birth_day)

            student = Student.objects.create(
                first_name=random.choice(first_names),
                last_name=random.choice(last_names),
                birth_date=birth_date,
                gender=random.choice(['M', 'F']),
                current_academic_level=random.choice(academic_levels),
                enrollment_status=random.choice(enrollment_statuses)
            )
            students_created += 1

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {students_created} sample students')
        )