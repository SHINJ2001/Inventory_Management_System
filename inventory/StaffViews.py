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


def staff_home_page(request):
	production_today = completed_processes.objects.filter(date = datetime.today()).count()
	pending_customers_count = requirement.objects.filter(acceptance_status =
            '0').count()
	context = {
		"production_today" : production_today,
		"pending_customers_count":pending_customers_count
	}

	return render(request, "inventory/staff_template/home_content.html", context)

def staff_profile(request):
	user = CustomUser.objects.get(request.user.id)
	staff = Staff.objects.get(admin=user)

def staff_view_customer(request):
	customer = requirement.objects.all()

	context = {
		"customer" : customer
	}
	return render(request, 'inventory/staff_template/staff_view_customer.html', context)

	
def staff_update_tools(request):
	tool = tools.objects.all()

	context = {
		"tool" : tool
	}

	return render(request, 'inventory/staff_template/staff_update_tools.html', context)

def staff_update_tools_save(request):
	if request.method != "POST":
		messages.error(request, "Method Not Allowed!")
		return redirect('staff_update_tools')
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
		return redirect('staff_update_tools')
	except:
            messages.error(request, "Failed to Update Tool!")
            return redirect('staff_update_tools')

def staff_view_rejections(request):
	rejections_pending = rejections.objects.all()

	context = {
		"rejections_pending" : rejections_pending
	}

	return render(request, 'inventory/staff_template/staff_view_rejections.html', context)

def staff_view_tools(request):
	tool = tools.objects.all()

	context = {
		"tool" : tool
	}

	return render(request, 'inventory/staff_template/staff_view_tools.html', context)

def staff_view_productions(request):
	production = targets.objects.all()

	context = {
		"production" : production
	}
	return render(request, 'inventory/staff_template/staff_view_productions.html', context)

def staff_update_processes(request):
	processes = completed_processes.objects.all()

	context = {
		"processes" : processes
	}

	return render(request, 'inventory/staff_template/staff_update_processes.html', context)

def staff_update_processes_save(request):
	if request.method != "POST":
		messages.error(request, "Method Not Allowed!")
		return redirect('staff_update_tools')
	else:
		order = request.POST.get('Order_id')
		part = request.POST.get('part_name')
		quantity =int(request.POST.get('quantity'))
		opern = request.POST.get('operation_name')
	
	try:
		ord = requirement.objects.get(order_id = order)
		prt = parts.objects.get(part_name = part)
		oper = { 
			"Procuring Raw Material" : "1", 
	 "Cleaning" : "2",
	 "Heating" : "3",
	 "Shaping" : "4",
	 "Cooling" : "5", 
	 "Cutting" : "6",
	 "Resting" : "7",
	 "Polishing" : "8",
	 "Packing" : "9"
		}
		x = oper[opern]
		process = completed_processes(part_name = prt, operation_name = x,
										total_produced = quantity, date = datetime.today(),
										order_id = ord
										)
		process.save()
		messages.success(request, "Tool Updated Successfully!")
		return redirect('staff_update_processes')
	except:
            messages.error(request, "Failed to Update Tool!")
            return redirect('staff_update_processes')


def staff_change_status(request, order):
	ord = requirement.objects.get(order_id = order)

	try:
		ord.acceptance_status = '1'
		ord.save()
		messages.success(request, "status changed Successfully!")
		return redirect('staff_view_customer')
	except:
		messages.error(request, "Failed to change status!")
		return redirect('staff_view_customer')

def staff_delete_rejections(request, order, oper):
	rejection = rejections.objects.get(order_id=order, operations_required = oper)
	try:
		rejection.delete()
		messages.success(request, "Staff Deleted Successfully.")
		return redirect('staff_view_rejections')
	except:
		messages.error(request, "Failed to Delete Staff.")
		return redirect('staff_view_rejections')
 
def staff_change_rejection_status_save(request, order, oper):
	try:
			order = rejections.objects.get(order_id = order, operations_required = oper)
			order.operation_status = '1'
			order.save()
			messages.success(request, "Updated Successfully.")
			return HttpResponseRedirect(reverse("staff_view_rejections",
                                                kwargs={"order_id":order, "operations_required":oper}))
	except:
			messages.error(request, "Failed to Update.")
			return HttpResponseRedirect(reverse("change_rejection_status",
                                                kwargs={"order_id":order, "operations_required":oper}))
