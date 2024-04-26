from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Employee(models.Model):
  id = models.IntegerField(max_length=6, unique=True)  #YYXXXX; first two digit for joining year and four digit for index
  username = models.TextField(max_length=20, unique=True)
  password = models.TextField()
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  nid = models.IntegerField(max_length=17)
  dateofbirth = models.DateField()
  joiningdate = models.DateField()
  bloodgroup = models.TextField()

  mobileno = models.IntegerField(max_length=11)
  email = models.EmailField()
  address = models.TextField()
  photo = models.FileField(upload_to="files/photo/")
  
  designation = models.TextField()
  #grade = models.IntegerChoices()
  currentsalary =  models.IntegerField()

  remaining_cl = models.FloatField()    #remaining casual leave
  remaining_el = models.FloatField()    #remaining Earned leave
  remaining_hel = models.FloatField()   #remaining Half Earned leave
  
  #office = models.ForeignKey(Office, on_delete=models.CASCADE)
  status = models.BooleanField()

class Upazilla(models.Model):
  upazilla_name = models.TextField()
  upazilla_division = models.TextField()
  upazilla_district = models.TextField()

class Office(models.Model):
  officehead = models.ForeignKey(Employee, on_delete=models.CASCADE)
  officename = models.TextField()
  division = models.TextChoices()
  """ 
    DHAKA = "Dhaka", _("dhaka")
    CHOTTOGRAM = "Chottogram", _("chottogram")
    Khunla
    Rajshahi
    Barishal
    Rangpur
    Sylhet
    Mymensign
  """
  district = models.TextChoices()
  """
    DHAKA = "Dhaka", _("dhaka")
    CHOTTOGRAM = "Chottogram", _("chottogram") 
    """
  upazilla = models.ForeignKey(Upazilla, on_delete = models.CASCADE)
  officeaddress = models.TextField(512)
  notes = models.TextField(512)
   

  """ class EmployeeDepartment(models.TextChoices):
    "DG Office"
    "Secretary office"
    "Department of Fine Arts"
    "Department of Theatre and Film"
    "Department of Research and Publicaitons"
    "Department of Music Dance and Recitation"
    "Department of Training"
    "Department of Production"
    "Administration"
    "Finance and Accounts"
    "Maintainence and Enginernig"
    "Establishment"
    "Common Service"
    "Auditorium Management"
    "Public Relations"
    "Ethnic Minority" """

  class EmployeeCategory(models.TextChoices):
    OFFICER = "Officer", _("Officer")
    ARTIST = "Artist", _("Artist")
    CADRE = "Cadre", _("Cadre")
    CONTRACTUAL = "Contractual", _("Contractual")
    MASTERROLE = "Masterrole", _("Masterrole")
    OUTSOURCING = "Outsourcing", _("Outsourcing")
  

class Leave(models.Model):
  class levavetype(models.TextChoices):
    CASUAL_LEAVE = "CL", _("Casul Leave")
    EARNED_LEAVE = "EL", _("Earned Leave")
    HALF_EARND_LEAVE = "HEL", _("Half Earned Leave")
    EDUCATION_LEAVE = "EDUL", _("Education Leave")
    #EXBANGLADESH_LEAVE = "EXBDL", _("Ex-Bangladesh Leave")
  employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
  startDate = models.DateField()
  endDate = models.DateField()
  file = models.FileField(upload_to="files/leave/%Y/")
  #isapproved = models.BooleanField()
  isexbangladesh = models.BooleanField()
  #approvedby = models.ForeignKey(Employee, on_delete = models.CASCADE)


class ACR(models.Model):
  employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
  startDate = models.DateField()
  endDate = models.DateField()
  rating = models.FloatField()
  comments = models.TextField(511)
  file = models.FileField(upload_to="files/acr/%Y/")

  



