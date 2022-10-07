from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from datetime import datetime
from .models import *

def manager_home(request):
	manager_obj = Manager.objects.get(admin = request.user.id)
	production_today = parts.objects.filter(mfd_date = datetime.today())
	rejections_pending = rejections.objects.filter(operations_status = '0')
	pending_customers = customer.objects.filter(deadline__lte=datetime.today())

	context = {
		"production_today" = production_today,
		"rejections_pending" = rejections_pending,
		"pending_customers" = pending_customers
	}

	return render(request, "manager_template/manger_home_page.html")

def new_customer(request):
	manager_obj = Managers.objects.get(admin=request.user.id) 
	customer_name = customer.objects.all()
	context = {
		"name":customer_name
	}
	return render(request, "manager_template/new_cutomer.html", context)

def add_rejections(request):
	manager_obj = Managers.objects.get(admin=request.user.id)
	rejections_pending = rejections.objects.filter(operations_status = '0')
	context= {
		"rejections_pending" : rejections_pending
	}

	return render(request, "manager_template/manager_add_rejections.html", context)

def update_tools(request):
	manager_obj = Managers.objects.get(admin=request.user.id)
	tools_all = tools.objects.all()
	context = {
		"tools_all" : tools_all
	}

	return render(request, "manager_template/manager_update_tools.html", context)

def view_tools(request):
	manager_obj = Managers.objects.get(admin = request.user.id)
	all_tools = tools.objects.all()
	context = {
		"all_tools": all_tools
	}

	return render(request, "manager_template/manager_view_tools.html", context)

def view_productions(request):
	manager_obj = Managers.objects.get(admin = request.user.id)
	production = parts.objects.all()
	context = {
		"production" = production
	}

	return render(request, "manager_template/manager_view_producitons.html", context)

def view_parts(request):
	manager_obj = Managers.objects.get(admin = request.user.id)
	all_parts = parts.objects.all().distinct()
	context = {
		"all_parts": all_parts
	}

	return render(request, "manager_template/manager_view_parts.html", context)

def view_rejections(request):
	manager_obj = Managers.objects.get(admin = request.user.id)
	rejections_pending = rejections.objects.all()
	context = {
		"rejections_pending":rejections_pending
	}

	return render(request, "manager_template/manager_view_rejections.html", context)

def view_operations(request):
	manager_obj = Managers.objects.get(admin = request.user.id)
	all_operations = Operations.objects.all().distinct()
	context = {
		"all_operations": all_operations
	}

	return render(request, "manager_template/manager_view_operations.html", context)

def view_tools(request):
	manager_obj = Managers.objects.get(admin = request.user.id)
	all_tools = tools.objects.all()
	context = {
		"all_tools": all_tools
	}

	return render(request, "manager_template/manager_view_tools", context)

def add_parts(request):
	manager_obj = Managers.objects.get(admin = request.user.id)
	all_parts = parts.objects.all().distinct()
	context = {
		"all_parts": all_parts
	}

	return render(request, "manager_template/manager_add_parts.html", context)


def get_production_on(request):
	manager_obj = Managers.objects.get(admin = request.user.id)
	production = parts.objects.all()

	context = {
		"production" = production
	}

	return render(request, "manager_template/manager_get_produciton_on.html", context)
