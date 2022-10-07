from django.db import models
from datetime import datetime

#Tools required for manufactring the tool
class tools(models.Model):
	tool_name = models.CharField(max_length=40)
	tool_life = models.IntegerField()
	bought_on = models.DateField(default = datetime.today())
	parts_manufactured = models.IntegerField(null=True)
	num_polished = models.IntegerField(null=True)
	last_polished_on = models.DateField(null=True)
	max_polish = models.IntegerField()
	price = models.IntegerField()

	class Meta:
		constraints=[
		models.UniqueConstraint(fields=['bought_on', 'tool_name' ], 
			name = 'prim_key_for_tools')
		]

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

#New customer requests will be added here
class customer(models.Model):
	name = models.CharField(max_length=50)
	request_date = models.DateField(default = datetime.today())
	contact=models.IntegerField()
	alternate_contact = models.IntegerField()
	email=models.CharField(max_length=150)
	deadline = models.DateField()
	part_name = models.CharField(max_length=40)
	order_id = models.CharField(max_length=15, primary_key=True)

#Parts that need to be manufactured
class parts(models.Model):
	part_name = models.CharField(max_length=40)
	order_id = models.ForeignKey(customer, on_delete=models.CASCADE)
	quantity_manufactured = models.IntegerField(null=True)
	required_quantity = models.IntegerField()
	operation_done = models.CharField(max_length=1, choices=OPERATIONS, default='1')
	batch_id = models.CharField(max_length=15, primary_key=True)
	mfd_date = models.DateField(default = datetime.today())

#Rejections from customers
class rejections(models.Model):
	part_name = models.ForeignKey(parts, on_delete=models.PROTECT)
	order_id = models.ForeignKey(customer, on_delete=models.PROTECT)
	batch_id = models.ForeignKey(parts, on_delete=models.PROTECT, related_name = "part_batch_id")
	rejection_date = models.DateField()
	rejection_amount = models.IntegerField()
	operations_required = models.CharField(max_length=1, choices=OPERATIONS)
	operation_status = models.CharField(max_length=1)

#Store the tools required for each operation
class Operations(models.Model):
	operation_name=models.CharField(max_length=1, choices=OPERATIONS, default='1')
	tools_required=models.ForeignKey(tools, on_delete=models.PROTECT)
	#Is this a good way though?? Storing every operation redundantly for every part used
	#since we every operation has a different part requirement??? -- ASK

#Selling cost for that part
class part_cost(models.Model):
	part_name = models.ForeignKey(parts, on_delete=models.CASCADE)
	part_price = models.IntegerField()

#Data to be maintained to check the productivity of the company
class manufacturers(models.Model):
	order_id = models.ForeignKey(customer, on_delete=models.CASCADE)
	production_today = models.IntegerField()
	date = models.DateField(default = datetime.today())
	expected_production_rate = models.IntegerField()
	current_production_rate = models.IntegerField()
	lead = models.CharField(max_length=50, null=True)
	lead_contact = models.IntegerField(null=True)
	lead_email = models.CharField(max_length = 150, null=True)

#Tables for maintaining the manager's personal data for login
class Managers(models.Model):
	manager_name = models.CharField(max_length=50)
	manager_id = models.CharField(max_length=100)

#Tables for maintaining staff's personal data for login
class workers(models.Model):
	worker_name = models.CharField(max_length=50)
	worker_id = models.CharField(max_length=100)