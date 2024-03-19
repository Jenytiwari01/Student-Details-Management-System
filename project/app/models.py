from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)  # Use AutoField for auto-incrementing IDs
    # name = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.id:
            # If the object is being created and doesn't have an ID yet
            last_object = Student.objects.last()
            if last_object:
                # If there are existing objects, reuse the last ID + 1
                self.id = last_object.id + 1
            else:
                # If there are no existing objects, start from ID 1
                self.id = 1
        super().save(*args, **kwargs)
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 25, blank= False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=25)

    def __str__(self):
        return self.name