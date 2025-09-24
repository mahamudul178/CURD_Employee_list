from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["employee_id", "emploee_name", "employee_email", "employee_contact"]

        widgets = {
            "employee_id": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Employee ID"}),
            "emploee_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Full Name"}),
            "employee_email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email"}),
            "employee_contact": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Contact Number"}),
        }

    def clean_employee_id(self):
        employee_id = self.cleaned_data.get('employee_id')
        if Employee.objects.filter(employee_id=employee_id).exists():
            raise forms.ValidationError("This Employee ID already exists!")
        return employee_id
    
    
    def clean_employee_email(self):
        employee_email = self.cleaned_data.get('employee_email')
        if Employee.objects.filter(employee_email=employee_email).exists():
            raise forms.ValidationError("This Email already exists!")
        return employee_email