from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages
from django.db.models import Q

# Create your views here.


from django.shortcuts import render
from .forms import EmployeeForm

def EmployeeView(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee created successfully!")
            return redirect('employee_list')
    
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

    
    
    
def EmployeeListView(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(
            Q(employee_id__icontains=query) |
            Q(emploee_name__icontains=query) |
            Q(employee_email__icontains=query) |
            Q(employee_contact__icontains=query)
        )
    else:
        employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
    


# Update and Delete Views

def EmployeeUpdateView(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully!")
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})



def EmployeeDeleteView(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, "Employee deleted successfully!")
        return redirect('employee_list')
    return render(request, 'employee_delete_confirm.html', {'employee': employee})








