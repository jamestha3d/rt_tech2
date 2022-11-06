from django.contrib import admin
from django.db import models

# Create your models here.

"""
Employee:
- First name
- Last name
- Position
- Salary
- Age
- Department
Department:
- Name
- Chief of the department
- List of employees, related to this department
Company
- Consists of departments
"""
class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    position = models.CharField(max_length=200)
    salary = models.IntegerField()
    age = models.IntegerField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE, blank=True, null=True, related_name="members")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Department(models.Model):
    name = models.CharField(max_length=64)
    chief = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name="dept_headed")
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank = True, related_name="departments")
    

    def employee_counter(self):
        return self.members.all().count()
    
    def list_employees(self):
        members = self.members.all()
        names = []
        for member in members:
            names.append(f"{member}")
        return names

    def salary_sum(self):
        members = self.members.all()
        sum = 0
        for member in members:
            sum += member.salary
        return sum

    def __str__(self):
        return f"{self.name}"
   
    

class Company(models.Model):
    name = models.CharField(max_length=64)

    
    def __str__(self):
        return f"{self.name}"

    @admin.display(description="Departments")
    def departments(self):
        return self.departments.all()

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'departments')
