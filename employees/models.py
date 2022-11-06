
from django.db import models

# Create your models here.
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
        return self.members.all()

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

    def departments(self):
        return self.departments.all()
