from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ClerkApps(models.Model):
    clerk = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    apptitle = models.CharField(max_length=200)
    appdesc = models.TextField(null=True,blank=True)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __list__(self):
        return [self.apptitle,self.appdesc,self.status,self.created]

    class Meta:
        ordering = ['status']


class ApplicationDatabase(models.Model):
    inward_number = models.AutoField(primary_key=True)
    applicant_name = models.CharField(max_length=35)
    mobile_number = models.CharField(max_length=13)
    inward_date = models.DateField()
    tapal_number = models.CharField(max_length=50)
    tapal_subject = models.CharField(max_length=50)
    tapal_type = models.CharField(max_length=35)


class TapalForwardDatabase(models.Model):
    first_clerk = models.CharField(max_length=35)
    second_clerk = models.CharField(max_length=35)
    inward_number = models.ForeignKey(ApplicationDatabase, on_delete=models.SET('Null'))


class InwardClerk(models.Model):
    clerk_name = models.CharField(max_length=35)
    inward_number = models.ForeignKey(ApplicationDatabase, on_delete=models.SET('Null'))
    remarks = models.CharField(max_length=35)


class SpecialDept(models.Model):
    clerk_name = models.CharField(max_length=35)
    serial_number = models.AutoField(primary_key=True)
    received_date = models.DateField()
    inward_number = models.ForeignKey(ApplicationDatabase, on_delete=models.SET('Null'))
    special_dept_name = models.CharField(max_length=35)
    remarks = models.CharField(max_length=35)


class ClerkWork(models.Model):
    clerk_name = models.CharField(max_length=35)
    work_serial_number = models.AutoField(primary_key=True)
    inward_number = models.ForeignKey(ApplicationDatabase, on_delete=models.SET('Null'))
    completion_date = models.CharField(max_length=35)
    receivers_name = models.CharField(max_length=35)
    remarks = models.CharField(max_length=35)


class InternalDistribution(models.Model):
    clerk_name = models.CharField(max_length=35)
    serial_number = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=35)
    inward_number = models.ForeignKey(ApplicationDatabase, on_delete=models.SET('Null'))
    received_date_time = models.DateTimeField()


class OutwardClerk(models.Model):
    clerk_name = models.CharField(max_length=35)
    serial_number = models.AutoField(primary_key=True)
    work_serial_number = models.ForeignKey(ClerkWork,  on_delete=models.SET('Null'))
    received_date_time = models.DateTimeField()


class OutDistribution(models.Model):
    clerk_name = models.CharField(max_length=35)
    # serial_number = models.AutoField()
    dept_name = models.CharField(max_length=35)
    inward_number = models.ForeignKey(ApplicationDatabase,  on_delete=models.SET('Null'))
    work_serial_number = models.ForeignKey(ClerkWork, on_delete=models.SET('Null'))

