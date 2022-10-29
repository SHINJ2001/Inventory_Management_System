from django.shortcuts import render, redirect
from datetime import datetime
from .models import *

def staff_home_page(request):
	production_today = parts.objects.filter(mfd_date=datetime.today)
	
	context = {
		"production_today" : production_today
	}

	return render(request, "staff_template/staff_home_page.html", context)

def staff_view_customer(request):
	customers = requirement.objects.all()

	context = {
		"customers" : customers
	}
	return render(request, 'staff_template/staff_view_customer.html', context)

	
def staff_update_tools(request):
	tool = tools.objects.all()

	context = {
		"tool" : tool
	}

	return render(request, 'staff_template/staff_update_tools.html', context)

def staff_view_rejections(request):
	rejection = rejections.objects.all()

	context = {
		"rejection" : rejection
	}

	return render(request, 'staff_template/staff_view_rejections.html', context)

def staff_view_tools(request):
	tool = tools.objects.all()

	context = {
		"tool" : tool
	}

	return render(request, 'staff_template/staff_view_tools.html', context)

def staff_view_productions(request):
	producn = targets.objects.all()

	context = {
		"production" : producn
	}
	return render(request, 'staff_template/staff_view_productions.html', context)

def staff_update_processes(request):
	processes = completed_processes.objects.all()

	context = {
		"processes" : processes
	}

	return render(request, 'staff_template/staff_update_processes.html', context)