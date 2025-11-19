from django.db import models

class EducationalBackground (models.Model):
    elementary_name = models.CharField(max_length=100)
    elementary_address = models.CharField(max_length=100)
    elementary_honors = models.CharField(max_length=100)

    highschool_name = models.CharField(max_length=100)
    highschool_address = models.CharField(max_length=100)
    highschool_honors = models.CharField(max_length=100)

    college_name = models.CharField(max_length=100)
    college_address = models.CharField(max_length=100)
    college_honors = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.college_name}"

# Create your models here.
