
from django.contrib import admin
from django.urls import path, include
from . import views
from .import ManagerViews, StaffViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('login', views.loginUser, name="login"),
    path('logout_user', views.logout_user, name="logout_user"),

    #URLs for managers

    path('manager_home/', ManagerViews.manager_home, name="manager_home"),
    path('new_customer/', ManagerViews.new_customer, name="new_customer"),
    path('add_rejections/', ManagerViews.add_rejections, name="add_rejections"),
    path('update_tools/', ManagerViews.update_tools, name="update_tools"),
    path('view_tools/', ManagerViews.view_tools, name="view_tools"),
    path('view_productions/', ManagerViews.view_productions,
        name="view_productions"),
    path('view_parts/', ManagerViews.view_inventory, name="view_inventory"),
    path('view_rejections/', ManagerViews.view_rejections,
        name="view_rejections"),
    path('view_operations/', ManagerViews.view_operations,
        name="view_operations"),
    path('add_parts/', ManagerViews.add_parts, name = "add_parts"),
    path('get_production_on', ManagerViews.get_production_on,
        name="get_production_on"),

    #URLs for workers

    path('staff_home/', StaffViews.staff_home, nmae = "staff_home"),
    path('staff_view_customer/', StaffViews.view_customer, name="view_customers"),
    path('staff_update_tools/', StaffViews.update_tools, name="update_tools"),
    path('staff_view_rejections/', StaffViews.staff_view_rejections,
        name="staff_view_rejections"),
    path('staff_view_tools/', StaffViews.staff_view_tools,
        name="staff_view_tools"),
    path('staff_view_productions', StaffViews.staff_view_productions,
        name="staff_view_productions"),
    path('staff_update_production_today',
        StaffViews.staff_update_production_today, 
        name="staff_update_production_today")
]