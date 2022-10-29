from ast import Num
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from datetime import datetime
from .models import *
from django.core import validators
from django.utils.dateparse import parse_date

def manager_home_page(request):
	production_today = targets.objects.all()
	rejections_pending_count = rejections.objects.filter(operation_status = '0').count()
	pending_customers_count = requirement.objects.filter(acceptance_status = '0').count()
	rejections_pending = rejections.objects.filter(operation_status = '0')
	pending_customers = requirement.objects.filter(acceptance_status = '0' )
	
	context = {
		"production_today" : production_today,
		"rejections_pending_count" : rejections_pending_count,
		"pending_customers_count" : pending_customers_count, 
		"rejections_pending" : rejections_pending,
		"pending_customers" : pending_customers
	}

	return render(request, "inventory/manager_template/home_content.html", context)

def manager_profile(request):
	user = CustomUser.objects.get(request.user.id)
	manager = Managers.objects.get(admin=user)


def manager_new_customer(request):
	customer_name = requirement.objects.all()
	context = {
		"name":customer_name
	}
	return render(request, "inventory/manager_template/manager_new_customer.html", context)

def manager_new_customer_save(request):
	if request.method != "POST":
		messages.error(request, "Method Not Allowed!")
		return redirect('manager_new_customer')
	else:
		Customer_name = request.POST.get('customer_name')
		Part_name = request.POST.get('part_name')
		Quantity = int(request.POST.get('quantity'))
		Deadline = request.POST.get('deadline')
		Customer_email = request.POST.get('customer_email')
		Customer_phone1 = request.POST.get('customer_phone1')
		Customer_phone2 = request.POST.get('customer_phone2')
	try:
		validators.validate_email(Customer_email)
	except:
		messages.error(request, "Please enter correct email!")
		return redirect('manager_new_customer')
	order = Customer_name[:4] + Part_name[:4]
	dead = parse_date(Deadline)
	print(Part_name)
	print(datetime.today())
	parts_name = parts.objects.get(part_name = Part_name)
#order_id, acceptance_status, date_of_transport
	try:
		customer = requirement(order_id = order,
						customer_name = Customer_name,
						part_name = parts_name,
						quantity = Quantity,
						order_date = datetime.today(),
						date_of_transport = dead,
						acceptance_status = '0',
						deadline = dead,
						customer_email=Customer_email,
						customer_phone1 = Customer_phone1,
						customer_phone2 = Customer_phone2)
		customer.save()
		messages.success(request, "Customer Added Successfully!")
		return redirect('manager_new_customer')
	except Exception as e:
			print(e)
			messages.error(request, "Failed to Add Customer!")
			return redirect('manager_new_customer')

def manager_view_orders(request):
	customer = requirement.objects.all()
	context = {
		"customer":customer
	}
	return render(request, "inventory/manager_template/manager_view_orders.html", context)

def manager_add_rejections(request):
	rejections_pending = rejections.objects.filter(operation_status = '0')
	context= {
		"rejections_pending" : rejections_pending
	}

	return render(request, "inventory/manager_template/manager_add_rejections.html", context)

def manager_add_rejections_save(request):
	if request.method != "POST":
		messages.error(request, "Method Not Allowed!")
		return redirect('manager_add_rejections')
	else:
		Order_id = request.POST.get('Order_id')
		Rejection_date =request.POST.get('Rejection_date')
		Rejection_amount =int(request.POST.get('Rejection_amount'))
		Operations_required =request.POST.get('Operations_required')

	rejection = parse_date(Rejection_date)
	order = requirement.objects.get(order_id = Order_id)
	operation = Operations.objects.get(operation_name = Operations_required)
	try:
		Rejection = rejections(order_id = order,
							rejection_date = rejection,
							rejection_amount =Rejection_amount,
							operations_required =operation, operation_status = '0')
		Rejection.save()
		messages.success(request, "Rejection Added Successfully!")
		return redirect('manager_add_rejections')
	except:
            messages.error(request, "Failed to Add Rejection!")
            return redirect('manager_add_rejections')

def manager_add_tools(request):
	tools_all = tools.objects.all()
	context = {
		"tools_all" : tools_all
	}

	return render(request, "inventory/manager_template/manager_add_tools.html", context)

def manager_add_tools_save(request):
	if request.method != "POST":
		messages.error(request, "Method Not Allowed!")
		return redirect('manager_add_tools')
	else:
		Tool_name = request.POST.get('tool_name')
		Tool_life =int(request.POST.get('tool_life'))
		Price =request.POST.get('price')

	try:
		tool = tools(tool_name = Tool_name, tool_life = Tool_life, price = Price, bought_on = datetime.today())
		tool.save()
		messages.success(request, "Tool Added Successfully!")
		return redirect('manager_add_tools')
	except:
            messages.error(request, "Failed to Add Tool!")
            return redirect('manager_add_tools')

def manager_update_tools(request):
	tools_all = tools.objects.all()
	context = {
		"tools_all" : tools_all
	}

	return render(request, "inventory/manager_template/manager_update_tools.html", context)

def manager_update_tools_save(request):
	if request.method != "POST":
		messages.error(request, "Method Not Allowed!")
		return redirect('manager_update_tools')
	else:
		Tool_name = request.POST.get('tool_name')
		part_manufacture = int(request.POST.get('parts_manufactured'))
		polish =request.POST.get('polished')

	try:
		tool = tools.objects.get(tool_name = Tool_name)
		num = tool.parts_manufactured
		if (num != None):
			num += part_manufacture
		else:
			num = part_manufacture
		if(polish == "Yes"):
			pol = tool.num_polished
			if(pol != None):
				pol += 1
				
			else:
				pol = 1
			tool.num_polished = pol
			tool.parts_manufactured = num
			tool.last_polished_on = datetime.today()
		else:
			tool.parts_manufactured = num
		tool.save()
		messages.success(request, "Tool Updated Successfully!")
		return redirect('manager_update_tools')
	except:
            messages.error(request, "Failed to Update Tool!")
            return redirect('manager_update_tools')

def manager_view_tools(request):
	all_tools = tools.objects.all()
	context = {
		"all_tools": all_tools
	}

	return render(request, "inventory/manager_template/manager_view_tools.html", context)

def manager_view_productions(request):
	production = parts.objects.all()
	context = {
		"production" : production
	}

	return render(request, "inventory/manager_template/manager_view_productions.html", context)

def manager_view_parts(request):
	all_parts = parts.objects.all().distinct()
	context = {
		"all_parts": all_parts
	}

	return render(request, "inventory/manager_template/manager_view_parts.html", context)

def manager_view_rejections(request):
	rejections_pending = rejections.objects.all()
	context = {
		"rejections_pending":rejections_pending
	}

	return render(request, "inventory/manager_template/manager_view_rejections.html", context)

def manager_view_operations(request):
	all_operations = Operations.objects.all().distinct()
	context = {
		"all_operations": all_operations
	}

	return render(request, "inventory/manager_template/manager_view_operations.html", context)

def manager_add_parts(request):
	all_parts = parts.objects.all()
	context = {
		"all_parts": all_parts
	}

	return render(request, "inventory/manager_template/manager_add_parts.html", context)

def manager_add_part_save(request):
	if request.method != "POST":
		messages.error(request, "Method Not Allowed!")
		return redirect('manager_add_part_save')
	else:
		Part_name = request.POST.get('part_name')
		Part_price = float(request.POST.get('price'))

	try:
		part = parts(part_name = Part_name, price = Part_price)
		part.save()
		messages.success(request, "Part Added Successfully!")
		return redirect('manager_add_parts')
	except:
            messages.error(request, "Failed to Add Part!")

            return redirect('manager_add_parts')

def manager_get_production_on(request):
	production = completed_processes.objects.all()

	context = {
		"production" : production
	}

	return render(request, "inventory/manager_template/manager_get_production_on.html", context)

def manager_update_production_today(request):
	producn = targets.objects.all()

	context = {
		"production" : producn
	}
	
	return render(request, 'inventory/manager_template/manager_update_production.html', context)

def manager_update_production_today_save(request):
	if request.method != "POST":
		HttpResponse("Invalid Method.")
	else:
		Order_id =  request.POST.get('order_id')
		Operation_lead = request.POST.get('operation_lead')

	require = requirement.objects.get(order_id = Order_id)
	x = require.deadline
	days = datetime.today() - x
	remaining_target = require.quantity - completed_processes.objects.filter(order_id = Order_id).aggregate(Sum('quantity'))['quantity__sum']
	expected_avg = remaining_target/days
	current_avg = completed_processes.objects.filter(order_id = Order_id).aggregate(Sum('quantity'))['quantity__sum']/(datetime.today() - require.order_date)
	Order = requirement.objects.get(order_id = Order_id)

	operate = manufacturers.objects.get(operation_lead = Operation_lead)

	try:
			target = targets(order_id = Order, 
										operation_lead = operate, 
										production = completed_processes.objects.filter(order_id = Order_id).aggregate(Sum('quantity'))['quantity__sum'],
										current_average = current_avg,
										expected_average = expected_avg, date_of_production = datetime.today())
			target.save()
			messages.success(request, "Target Updated Successfully.")
			return HttpResponseRedirect(reverse("manager_update_production_today",
                                                kwargs={"order_id":Order_id}))
	except:
			messages.error(request, "Failed to Update Price.")
			return HttpResponseRedirect(reverse("manager_update_production_today",
                                                kwargs={"order_id":Order_id}))

def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
 
    context={
        "user": user
    }
    return render(request, 'inventory/manager_template/admin_profile.html', context)
 
def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('admin_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
 
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('admin_profile')
  
def manager_change_price(request):
	all_parts = parts.objects.all()
	context = {
		"all_parts": all_parts
	}

	return render(request, "inventory/manager_template/manager_change_price.html", context)

def manager_change_price_save(request):
	if request.method != "POST":
		HttpResponse("Invalid Method.")
	else:
		Part_name = request.POST.get('part_name')
		part_price = float(request.POST.get('part_price'))

		try:
			part = parts.objects.get(part_name = Part_name)
			part.price = part_price
			part.save()
			messages.success(request, "Price Updated Successfully.")
			return HttpResponseRedirect(reverse("manager_change_price",
                                                kwargs={"price":part_price}))
		except:
			messages.error(request, "Failed to Update Price.")
			return HttpResponseRedirect(reverse("manager_change_price",
                                                kwargs={"price":part_price}))

def manager_delete_parts(request):
	part = parts.objects.all()
	context = {
		"part" : part
	}

	return render(request, "inventory/manager_template/manager_delete_parts.html", context)

def manager_delete_parts_save(request):
	Part_name = request.POST.get('part_name')
	part = parts.objects.get(part_name = Part_name)
	try:
		part.delete()
		messages.success(request, "Part Deleted Successfully.")
		return redirect('manager_delete_parts')
	except:
		messages.error(request, "Failed to Delete Part.")
		return redirect('manager_delete_parts')

def change_rejection_status(request):
	rejections_pending = rejections.objects.all()
	context = {
		"rejections_pending":rejections_pending
	}

	return render(request, "inventory/manager_template/change_rejection_status.html", context)

def change_rejection_status_save(request):
	Order_id = request.POST.get('order_id')
	Operations_required = request.POST.get('op_req')
	try:
			order = rejections.objects.get(order_id = Order_id, operations_required = Operations_required)
			order.operation_status = '1'
			order.save()
			messages.success(request, "Updated Successfully.")
			return HttpResponseRedirect(reverse("change_rejection_status",
                                                kwargs={"order_id":Order_id, "operations_required":Operations_required}))
	except:
			messages.error(request, "Failed to Update.")
			return HttpResponseRedirect(reverse("change_rejection_status",
                                                kwargs={"order_id":Order_id, "operations_required":Operations_required}))


def manager_update_lead(request):
	leads = manufacturers.objects.all()
	context = {
		"leads" : leads
	}

	return render(request, "inventory/manager_template/manager_update_lead.html", context)

def  manager_update_lead_save(request):
	if request.method != "POST":
		messages.error(request, "Method Not Allowed!")
		return redirect('manager_add_part_save')
	else:
		lead_name = request.POST.get('lead')
		Lead_contact = request.POST.get('lead_contact')
		Lead_email = request.POST.get('lead_email')

	try:
		manufac = manufacturers(lead = lead_name, lead_contact = Lead_contact, lead_email = Lead_email)
		manufac.save()
		messages.success(request, "Lead Added Successfully!")
		return redirect('manager_home')
	except:
            messages.error(request, "Failed to Add Lead!")
            return redirect('manager_home')
