from rest_framework import serializers
from employees.models import *

class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField(many=False)
    class Meta:
        model = Employee
        fields = '__all__'
    
    

class DepartmentSerializer(serializers.ModelSerializer):
    #replace related string field id with name  
    chief = serializers.StringRelatedField(many=False)
    company = serializers.StringRelatedField(many=False)
    #add extra fields to serialized output
    employee_counter = serializers.SerializerMethodField()
    salary_sum = serializers.SerializerMethodField()
    list_employees = serializers.SerializerMethodField()

    #methods for the extra fields
    def get_employee_counter(self, employee):
        return employee.employee_counter()

    def get_salary_sum(self, employee):
        return employee.salary_sum()

    def get_list_employees(self, employee):
        return employee.list_employees()

    class Meta:
        model = Department
        fields = '__all__' 
        

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'