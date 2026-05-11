from django.db import models

class Course(models.Model):
    field = models.CharField(max_length=150)

    def __str__(self):
        return self.field

    def __repr__(self):
        return f"PK: {self.pk} . {self.field} "

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=10)
    address = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    field = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"PK: {self.pk} . {self.name} "