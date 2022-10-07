from django.shortcuts import render,HttpResponse, redirect,HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from .models import *
from django.contrib import messages

def home(request):
    return render(request, 'home.html')
 
 
def contact(request):
    return render(request, 'contact.html')
 
 
def loginUser(request):
    return render(request, 'login_page.html')
 
def doLogin(request):
     
    print("here")
    email_id = request.GET.get('email')
    password = request.GET.get('password')
    # user_type = request.GET.get('user_type')
    print(email_id)
    print(password)
    print(request.user)
    if not (email_id and password):
        messages.error(request, "Please provide all the details!!")
        return render(request, 'login_page.html')
 
    user = CustomUser.objects.filter(email=email_id, password=password).last()
    if not user:
        messages.error(request, 'Invalid Login Credentials!!')
        return render(request, 'login_page.html')
 
    login(request, user)
    print(request.user)
 
    if user.user_type == CustomUser.STUDENT:
        return redirect('student_home/')
    elif user.user_type == CustomUser.STAFF:
        return redirect('staff_home/')
    elif user.user_type == CustomUser.HOD:
        return redirect('admin_home/')
 
    return render(request, 'home.html')
 
     
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
 
def get_user_type_from_email(email_id):
    """
    Returns CustomUser.user_type corresponding to the given email address
    email_id should be in following format:
    eg.: 'abhishek.staff@jecrc.com'
    """
    try:
        email_id = email_id.split('@')[0]
        email_user_type = email_id.split('.')[1]
        return CustomUser.EMAIL_TO_USER_TYPE_MAP[email_user_type]
    except:
        return None
