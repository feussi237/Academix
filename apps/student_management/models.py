from django.db import models
import uuid

class Student(models.Model):

    GENDER_CHOICES = (
        ("M","Male"),
        ("F","Female")
    )

    ACADEMIC_LEVEL_CHOICES = (
        ('p1','Primary 1'),
        ('p2','Primary 2'),
        ('p3','Primary 3'),
        ('p4','Primary 4'),
        ('p5','Primary 5'),
        ('p6','Primary 6'),
        ('s1','Secondary 1'),
        ('s2','Secondary 2'),
        ('s3','Secondary 3'),
        ('s4','Secondary 4'),
        ('s5','Secondary 5'),
        ('s6','Secondary 6')
    )
    ENROLLMENT_STATUS_CHOICES = (
        ('active', 'Active'),
        ('transferred', 'Transferred'),
        ('dismissed', 'Dismissed'),
        ('graduated', 'Graduated'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField("First Name",max_length=50)
    last_name = models.CharField("Last Name",max_length=50)
    birth_date = models.DateField("Birth Date")
    gender = models.CharField("Gender",max_length=10, choices= GENDER_CHOICES, default='M')
    current_academic_level = models.CharField("Current Academic Level",max_length=10,choices=ACADEMIC_LEVEL_CHOICES)
    enrollment_status = models.CharField("Enrollment Status",max_length=20, choices=ENROLLMENT_STATUS_CHOICES)
    photo = models.ImageField('photo',upload_to='students/photos',blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    

    def get_age(self):
        from datetime import date
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month,today.day) < (self.birth_date.month, self.birth_date.day))
        return age 