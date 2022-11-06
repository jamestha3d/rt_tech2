from rest_framework import serializers
from employees.models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):

    #add extra fields to serialized output
    employee_counter = serializers.SerializerMethodField()
    salary_sum = serializers.SerializerMethodField()

    #methods for the extra fields
    def get_employee_counter(self, employee):
        return employee.employee_counter()

    def get_salary_sum(self, employee):
        return employee.salary_sum()

    class Meta:
        model = Department
        fields = '__all__' 
        

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'