from django import forms

from .models import *

class DateInput(forms.DateInput):
    input_type = "date"

tool_life_list = [1, 2, 3, 4, 5, 6, 7, 8]

class updateToolsForm(forms.Form):

    tool_name = forms.CharField(label = "Tool Name",
                                 max_length=40, 
                                 widget=forms.TextInput(attrs={"class":"form-control"}))
    tool_life = forms.ChoiceField(label = "Tool Life (In Years)", 
                                  choices = tool_life_list,
                                  widget=forms.Select(attrs={"class":"form-control"}))
    bought_on = forms.DateField(label = "Date Of Purchase ")
    price = forms.CharField(label = "Tool price",
                                 max_length=8, 
                                 widget=forms.TextInput(attrs={"class":"form-control"}))
    
class update_production(forms.Form):

    try:
        orders = requirement.objects.filter(acceptance_status = '0')
        order_list = []
        for order in orders:
            single_order = (orders.order_id, orders.customer_name, orders.order_date)
            order_list.append(single_order)
    except:
        print('here')
        order_list = []

    order_id = forms.ChoiceField(label = "Order Id",
                                 choices = order_list, 
                                 widget=forms.Select(attrs={"class":"form-control"}))
    operation_lead = forms.CharField(label = "Operation lead by",
                                 max_length=40, 
                                 widget=forms.TextInput(attrs={"class":"form-control"}))
    production = int(forms.CharField(label = "Production ",
                                 max_length=6, 
                                 widget=forms.TextInput(attrs={"class":"form-control"})))
    date_of_production = forms.DateField(label = "Date Of Production")

class add_customer(forms.Form):
    customer_name = forms.CharField(label = 'Customer Name ', max_length = 30, widget = forms.TextInput(attr={"class":"form-control"}))
    part_name = forms.CharField(label = 'Part Requested', max_length = 40, widget = forms.TextInput(attr={"class":"form-control"}))
    quantity = int(forms.CharField(label = 'Quantity', max_length = 6, widget = forms.TextInput(attr={"class":"form-control"})))
    order_date = forms.DateField(label = 'Order Date')
    deadline = forms.DateField(label = 'Deadline ')
    customer_email = forms.EmailField(max_length = 100)
    customer_phone1 = forms.CharField(label = 'Customer Phone', max_length = 12, widget = forms.TextInput(attr={"class":"form-control"}))
    customer_phone2 = forms.CharField(label = 'Customer Alternate Phone', max_length = 12, widget = forms.TextInput(attr={"class":"form-control"}))

class add_rejections(forms.Form):
    try:
        orders = requirement.objects.filter(acceptance_status = '0')
        order_list = []
        for order in orders:
            single_order = (order.order_id, order.customer_name, order.order_date)
            order_list.append(single_order)
    except:
        print('here')
        order_list = []
    OPERATIONS = [
	 "Procuring Raw Material", 
	 "Cleaning",
	 "Heating",
	 "Shaping",
	 "Cooling", 
	 "Cutting",
	 "Resting",
	 "Polishing",
	 "Packing"
    ]
    order_id = forms.ChoiceField(label = "Order Id",
                                 choices = order_list, 
                                 widget=forms.Select(attrs={"class":"form-control"}))
    rejection_date = forms.DateField(label = 'Rejection Date')
    rejection_amount = int(forms.CharField(label = "Rejection Amount", max_length = 6, widget=forms.TextInput(attrs={"class":"form-control"})))
    operations_required = forms.ChoiceField(label = "Required Operation", choices = OPERATIONS, widget=forms.Select(attrs={'class':'form-control'}))

class add_parts(forms.Form):
    part_name = forms.CharField(label="Part Name", max_length = 40, widget = forms.TextInput(attr={"class":"form-control"}))
    price = forms.FloatField(label = "Price ")

class update_processes(forms.Form):
    try:
        parts = parts.objects.all()
        part_list = set()
        for part in parts:
            single_part = (part.part_name)
            part_list.add(single_part)
    except:
        print('here')
        part_list = set()
    
    OPERATIONS = [
	 "Procuring Raw Material", 
	 "Cleaning",
	 "Heating",
	 "Shaping",
	 "Cooling", 
	 "Cutting",
	 "Resting",
	 "Polishing",
	 "Packing"
    ]
    try:
        orders = requirement.objects.filter(acceptance_status = '0')
        order_list = []
        for order in orders:
            single_order = (order.order_id, order.customer_name, order.order_date)
            order_list.append(single_order)
    except:
        print('here')
        order_list = []

    part_name = forms.ChoiceField(label = 'Part Name', choices = part_list, widget=forms.Select(attrs={'class':'form-control'}))
    operation = forms.ChoiceField(label = 'Operation Name', choices = OPERATIONS, widget=forms.Select(attrs={'class':'form-control'}))
    total_produced = int(forms.CharField(label = "Amount", max_length = 6, widget=forms.TextInput(attrs={"class":"form-control"})))
    order_id = forms.ChoiceField(label = "Order Id",
                                 choices = order_list, 
                                 widget=forms.Select(attrs={"class":"form-control"}))

