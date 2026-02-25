from django.db import models

class Patient(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    dateregistered = models.DateTimeField()
    medicalhistory = models.TextField()

    def __str__(self):
        return self.firstname

class Doctor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    years_of_specialization = models.IntegerField()

    def __str__(self):
        return self.first_name
    

class MyAppointments(models.Model):
    name = models.CharField(max_length=200) 
    email = models.EmailField()
    phone = models.CharField(max_length=20)   
    datetime = models.DateTimeField()
    department = models.CharField(max_length=10)
    doctor = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name