from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)  # Field to store the category name

    def __str__(self):
        return self.name  # String representation of the Category object

class Grade(models.Model):
    name = models.CharField(max_length=100)  # Field to store the grade name

    def __str__(self):
        return self.name  # String representation of the Grade object

class Material(models.Model):
    name = models.CharField(max_length=100)  # Field to store the material name
    file = models.FileField(upload_to='materials/')  # Field to upload and store a file associated with the material
    url = models.URLField(blank=True)  # Field to store a URL associated with the material (optional)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Relationship with Category model
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)  # Relationship with Grade model

    def __str__(self):
        return self.name  # String representation of the Material object
