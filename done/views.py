from django.shortcuts import render,redirect
from .models import Employee, ROLE_CHOICES
from django.contrib import messages
from django.core.paginator import Paginator 


def role_management(request):
    roles = Employee.objects.values('role', 'is_active').distinct()
    return render(request, 'role_management.html', {"roles": roles})


def toggle_role(request, role):
    role_obj = Employee.objects.filter(role=role).first()
    if role_obj:
        role_obj.is_active = not role_obj.is_active
        role_obj.save()
    return redirect('done:role_management')
    
     

def home(request):
    emp = Employee.objects.all()
    paginator = Paginator(emp, 3)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    start_index = (page.number - 1) * paginator.per_page
    for index, e in enumerate(page, start=start_index + 1):
        e.continuous_number = index

# page.number = 1
# paginator.per_page = 3

# start_index = (1 - 1) * 3
# start_index = 0

# Iteration:
# - Employee A:
#   index = start_index + 1 = 0 + 1 = 1
#   continuous_number = 1

# - Employee B:
#   index = start_index + 2 = 0 + 2 = 2
#   continuous_number = 2

    
    
    return render(request, 'home.html', {'page':page, 'messages': messages.get_messages(request)})


def emp_add(request):
    if request.method == 'POST':
        # retreive the user data
        emp_code = request.POST.get('emp_code')
        emp_role = request.POST.get('emp_role')
        emp_name = request.POST.get('emp_name')
        emp_email = request.POST.get('emp_email')
        emp_address = request.POST.get('emp_address')
        emp_phone = request.POST.get('emp_phone')

        # create a object for models
        e = Employee()
        e.code = emp_code
        e.role = emp_role
        e.name = emp_name
        e.email = emp_email
        e.address = emp_address
        e.phone = emp_phone

        e.save()


        messages.success(request, 'The employee is added successfully.')

        return redirect('home')
    code = Employee.generate_code()
    active_roles = [choice[0] for choice in ROLE_CHOICES if not Employee.objects.filter(role=choice[0], is_active=False).exists()]
    return render(request, 'emp_add.html', {'code':code, 'active_roles': active_roles})

# 


def delete_emp(request, code):
        e = Employee.objects.get(code=code)
        e.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('home')


def update_emp(request, code):
    emp = Employee.objects.get(code=code)
    if request.method == "POST":
        emp_role = request.POST.get('emp_role')
        emp_name = request.POST.get('emp_name')
        emp_email = request.POST.get('emp_email')
        emp_address = request.POST.get('emp_address')
        emp_phone = request.POST.get('emp_phone')

        emp.role = emp_role
        emp.name = emp_name
        emp.email = emp_email
        emp.address = emp_address
        emp.phone = emp_phone

        emp.save()

        messages.success(request, 'The employee is updated successfully.')
        return redirect('home')

    else:
         return render(request, 'update_emp.html', {'emp':emp})