from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from employees.models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from .paginations import CustomPagination
from rest_framework.permissions import IsAuthenticated, AllowAny

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def listEmployees(request):
    #include pagination
    paginator = CustomPagination()
    employees = Employee.objects.all().order_by('id')
    result = paginator.paginate_queryset(employees, request)
    employee_serializer = EmployeeSerializer(result, many=True)
    return paginator.get_paginated_response(employee_serializer.data)

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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addEmployee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return Response("Employee successfully deleted")

@api_view(['GET'])
def listDepartments(request):
    depts = Department.objects.all()
    dept_serializer = DepartmentSerializer(depts, many=True)
   
    return Response(dept_serializer.data)
