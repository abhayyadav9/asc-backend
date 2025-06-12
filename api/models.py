from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    credits = models.IntegerField(default=3)  # Default to 3 credits
    department = models.CharField(max_length=100, default='Computer Science')  # Default department

    def __str__(self):
        return f"{self.course_code} - {self.title}"

class Instance(models.Model):
    year = models.IntegerField()
    semester = models.IntegerField()  # 1 or 2
    course = models.ForeignKey(Course, related_name='instances', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.title} - {self.year} Semester {self.semester}"
