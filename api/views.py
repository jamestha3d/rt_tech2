from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
#from rest_framework.generics import GenericAPIView
from employees.models import *
from .serializers import *
#from rest_framework.pagination import PageNumberPagination
from .paginations import CustomPagination
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='get',
    operation_summary="List all Employees",
    operation_description="This returns a list of all  Employees"
)
@api_view(['GET',])
@permission_classes([IsAuthenticated])
def listEmployees(request):
    #include pagination
    paginator = CustomPagination()
    employees = Employee.objects.all().order_by('id')
    result = paginator.paginate_queryset(employees, request)
    employee_serializer = EmployeeSerializer(result, many=True)
    return paginator.get_paginated_response(employee_serializer.data)


@swagger_auto_schema(
    method='get',
    operation_summary="Search for an Employee",
    operation_description="This searches for an employee in a department using the employee last name and the department id"
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def searchEmployee(request, last_name, dept_id):
    paginator = CustomPagination()
    dept = Department.objects.get(id=dept_id)
    employees = dept.members.all().filter(last_name = last_name).order_by('id')
    result = paginator.paginate_queryset(employees, request)
    if employees:
        if len(employees) > 1:
            employee_serializer = EmployeeSerializer(result, many=True)
            return paginator.get_paginated_response(employee_serializer.data)
        else:
            employee_serializer = EmployeeSerializer(employees[0], many=False)
            return paginator.get_paginated_response(employee_serializer.data)
        
        
    else:
        return Response("Employee not found")

@swagger_auto_schema(
    method='post',
    operation_summary="Add an employee",
    operation_description="Add an employee"
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addEmployee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@swagger_auto_schema(
    method='delete',
    operation_summary="delete employee",
    operation_description="Delete employee by employee id"
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return Response("Employee successfully deleted")


@swagger_auto_schema(
    method='get',
    operation_summary="List all Departments",
    operation_description="This returns a list of all Departments"
)
@api_view(['GET'])
def listDepartments(request):
    depts = Department.objects.all()
    dept_serializer = DepartmentSerializer(depts, many=True)
   
    return Response(dept_serializer.data)
