from django import forms

class ApplicationForm(forms.Form):
    applicant_name = forms.CharField(label='Your name', max_length=50)
    mobile_number = forms.CharField(label='Mobile No', max_length=13)
    tapal_number = forms.CharField(label='Tapal Number', max_length=50)
    tapal_subject = forms.CharField(label='Subject', max_length=50)
    tapal_type = forms.CharField(label='Type of tapal', max_length=50)


# class TapalForwardDatabase(models.Model):
#     first_clerk = models.CharField(max_length=35)
#     second_clerk = models.CharField(max_length=35)
#     inward_number = models.ForeignKey(ApplicationDatabase, on_delete=models.SET_NULL)
#
#
# class InwardClerk(models.Model):
#     clerk_name = models.CharField(max_length=35)
#     inward_number = models.ForeignKey(ApplicationDatabase, on_delete=models.SET_NULL)
#     remarks = models.CharField(max_length=35)
#
#
# class SpecialDept(models.Model):
#     clerk_name = models.CharField(max_length=35)
#     serial_number = models.AutoField(primary_key=True)
#     received_date = models.DateField()
#     inward_number = models.ForeignKey(ApplicationDatabase,  on_delete=models.SET_NULL)
#     special_dept_name = models.CharField(max_length=35)
#     remarks = models.CharField(max_length=35)
#
#
# class ClerkWork(models.Model):
#     clerk_name = models.CharField(max_length=35)
#     work_serial_number = models.AutoField(primary_key=True)
#     inward_number = models.ForeignKey(ApplicationDatabase, on_delete=models.SET_NULL)
#     completion_date = models.CharField(max_length=35)
#     receivers_name = models.CharField(max_length=35)
#     remarks = models.CharField(max_length=35)
#
#
# class InternalDistribution(models.Model):
#     clerk_name = models.CharField(max_length=35)
#     serial_number = models.AutoField(primary_key=True)
#     table_name = models.CharField(max_length=35)
#     inward_number = models.ForeignKey(ApplicationDatabase, on_delete=models.SET_NULL)
#     received_date_time = models.DateTimeField()
#
#
# class OutwardClerk(models.Model):
#     clerk_name = models.CharField(max_length=35)
#     serial_number = models.AutoField(primary_key=True)
#     work_serial_number = models.ForeignKey(ClerkWork,  on_delete=models.SET_NULL)
#     received_date_time = models.DateTimeField()
#
#
# class OutDistribution(models.Model):
#     clerk_name = models.CharField(max_length=35)
#     # serial_number = models.AutoField()
#     dept_name = models.CharField(max_length=35)
#     inward_number = models.ForeignKey(ApplicationDatabase,  on_delete=models.SET_NULL)
#     work_serial_number = models.ForeignKey(ClerkWork, on_delete=models.SET_NULL)
