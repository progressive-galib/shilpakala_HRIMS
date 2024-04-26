from django.db import models
from django.utils.translation import gettext_lazy as _

class Employee(models.Model):
    class EmployeeCategory(models.TextChoices):
        OFFICER = "Officer", _("Officer")
        ARTIST = "Artist", _("Artist")
        CADRE = "Cadre", _("Cadre")
        CONTRACTUAL = "Contractual", _("Contractual")
        MASTERROLE = "Masterrole", _("Masterrole")
        OUTSOURCING = "Outsourcing", _("Outsourcing")

    #id = models.IntegerField(unique=True)  # YYXXXX; first two digit for joining year and four digit for index
    username = models.CharField(max_length=20, unique=True)
    password = models.TextField()
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    nid = models.BigIntegerField(unique=True)
    dateofbirth = models.DateField()
    joiningdate = models.DateField()
    bloodgroup = models.CharField(max_length=5)
    mobileno = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()
    photo = models.ImageField(upload_to="files/photo/")
    designation = models.TextField()
    currentsalary = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_cl = models.FloatField()    # Remaining casual leave
    remaining_el = models.FloatField()    # Remaining Earned leave
    remaining_hel = models.FloatField()   # Remaining Half Earned leave
    status = models.BooleanField(default=True)
    employee_category = models.CharField(max_length=20,choices=EmployeeCategory.choices)
    assigened_office = models.ForeignKey("Office",on_delete = models.CASCADE)

class Division(models.Model):
    name = models.CharField(max_length=255)

class District(models.Model):
    name = models.CharField(max_length=255)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

class Upazilla(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

class Office(models.Model):
    officehead = models.ForeignKey(Employee, on_delete=models.CASCADE)
    officename = models.CharField(max_length=255)
    division = models.CharField(max_length=255) # You can use CharField for division and district if they are not predefined choices
    district = models.CharField(max_length=255)
    upazilla = models.ForeignKey(Upazilla, on_delete=models.CASCADE)
    officeaddress = models.TextField(max_length=512)
    notes = models.TextField(max_length=512)

class Leave(models.Model):
    class LeaveType(models.TextChoices):
        CASUAL_LEAVE = "CL", _("Casual Leave")
        EARNED_LEAVE = "EL", _("Earned Leave")
        HALF_EARNED_LEAVE = "HEL", _("Half Earned Leave")
        EDUCATION_LEAVE = "EDUL", _("Education Leave")
        EX_BANGLADESH_LEAVE = "EXBDL", _("Ex-Bangladesh Leave")

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    file = models.FileField(upload_to="files/leave/%Y/")
    is_exbangladesh = models.BooleanField()
    leave_type = models.CharField(max_length=20, choices=LeaveType.choices)

class ACR(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rating = models.FloatField()
    comments = models.TextField(max_length=511)
    file = models.FileField(upload_to="files/acr/%Y/")
