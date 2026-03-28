from django.test import TestCase
from .models import Student
from datetime import date

class StudentModelTest(TestCase):

    def setUp(self):
        self.student = Student.objects.create(
            first_name="John",
            last_name="Doe",
            birth_date=date(2000, 1, 1),
            gender="M",
            current_academic_level="s1",
            enrollment_status="active"
        )

    def test_student_creation(self):
        """Test that a student can be created"""
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.last_name, "Doe")
        self.assertEqual(self.student.get_age(), 24)  # Assuming current year is 2024
        self.assertEqual(str(self.student), "John Doe")

    def test_student_age_calculation(self):
        """Test age calculation"""
        age = self.student.get_age()
        self.assertIsInstance(age, int)
        self.assertGreaterEqual(age, 0)

    def test_gender_choices(self):
        """Test gender field choices"""
        self.assertIn(self.student.gender, ['M', 'F'])
        self.assertEqual(self.student.get_gender_display(), "Male")

    def test_academic_level_choices(self):
        """Test academic level field choices"""
        valid_levels = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 's1', 's2', 's3', 's4', 's5', 's6']
        self.assertIn(self.student.current_academic_level, valid_levels)

    def test_enrollment_status_choices(self):
        """Test enrollment status field choices"""
        valid_statuses = ['active', 'transferred', 'dismissed', 'graduated']
        self.assertIn(self.student.enrollment_status, valid_statuses)
        self.assertEqual(self.student.get_enrollment_status_display(), "Active")
