from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

class CustomUser(AbstractUser):
    MANAGER = '1'
    STAFF = '2'

    EMAIL_TO_USER_TYPE_MAP = {
        'manager': MANAGER,
        'staff': STAFF

    }
 
    user_type_data = ((MANAGER, "manager"), (STAFF, "staff"))
    user_type = models.CharField(default='1', choices=user_type_data, max_length=10)

#Tools required for manufactring the tool
class tools(models.Model):
	tool_name = models.CharField(max_length=40, primary_key = True)
	tool_life = models.IntegerField()
	bought_on = models.DateField(default = datetime.today())
	parts_manufactured = models.IntegerField(null=True)
	num_polished = models.IntegerField(null=True)
	last_polished_on = models.DateField(null=True)
	price = models.CharField(max_length = 8)

#Arrange these in increasing quantity so that every number would 
#denote the step number completed
OPERATIONS = [

	("1", "Procuring Raw Material"), 
	("2", "Cleaning"),
	("3", "Heating"),
	("4", "Shaping"),
	("5", "Cooling"), 
	("6", "Cutting"),
	("7", "Resting"),
	("8", "Polishing"),
	("9", "Packing")
]

#Parts that need to be manufactured
class parts(models.Model):
	part_name = models.CharField(max_length=40, primary_key = True)
	price = models.FloatField()

#Store the tools required for each operation
class Operations(models.Model):
	operation_name=models.CharField(max_length=1, choices=OPERATIONS, default='1')
	tool_name=models.ForeignKey(tools, on_delete=models.CASCADE)

#Data to be maintained to check the productivity of the company
class manufacturers(models.Model):
	lead = models.CharField(max_length=50, primary_key = True)
	lead_contact = models.CharField(max_length = 12, null=True)
	lead_email = models.CharField(max_length = 150, null=True)

class requirement(models.Model):
	order_id = models.CharField(max_length = 10, primary_key = True)
	customer_name = models.CharField(max_length = 30)
	part_name = models.ForeignKey(parts, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	order_date = models.DateField()
	date_of_transport = models.DateField()
	acceptance_status = models.CharField(max_length = 1)
	deadline = models.DateField()
	customer_email = models.CharField(max_length = 100)
	customer_phone1 = models.CharField(max_length = 10)
	customer_phone2 = models.CharField(max_length = 10)

#Rejections from customers
class rejections(models.Model):
	order_id = models.ForeignKey(requirement, on_delete=models.CASCADE)
	rejection_date = models.DateField()
	rejection_amount = models.IntegerField()
	operations_required = models.ForeignKey(Operations, on_delete=models.CASCADE)
	operation_status = models.CharField(max_length=1, default = '0')

class completed_processes(models.Model):
	part_name = models.ForeignKey(parts, on_delete=models.CASCADE)
	operation_name = models.ForeignKey(Operations, on_delete=models.CASCADE)
	total_produced = models.IntegerField()
	date = models.DateField()
	order_id = models.ForeignKey(requirement, on_delete=models.SET_NULL, null=True)

class targets(models.Model):
	order_id = models.ForeignKey(requirement, on_delete=models.CASCADE)
	operation_lead = models.ForeignKey(manufacturers, on_delete=models.SET_NULL, null = True)
	production = models.IntegerField()
	current_average = models.FloatField()
	date_of_production = models.DateField()
	expected_average = models.FloatField()

 #Tables for maintaining the manager's personal data for login
class Managers(models.Model):
	id = models.AutoField(primary_key=True)
	admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = models.Manager()
 
 #Tables for maintaining staff's personal data for login
class Staff(models.Model):
	id = models.AutoField(primary_key=True)
	admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = models.Manager()