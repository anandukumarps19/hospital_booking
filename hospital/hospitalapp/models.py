from django.db import models

# Create your models here.

class Department(models.Model):
    Department_name = models.CharField(max_length=250)
    Department_des = models.TextField()

    def __str__(self):
        return self.Department_name

class Doctors(models.Model):
    Doctor_name= models.CharField(max_length=250)
    Doctor_spec=models.CharField(max_length=250)
    Department_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    Doctor_image=models.ImageField(upload_to='pics')

    def __str__(self):
        return 'Dr .' + self.Doctor_name +' - ('+ self.Doctor_spec + ')'

class Booking(models.Model):
    name=models.CharField(max_length=250)
    number=models.CharField(max_length=250)
    email=models.EmailField()
    Doctor_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    date=models.DateField()
    Booked_on=models.DateField(auto_now=True)

    def __str__(self):
        return self.name