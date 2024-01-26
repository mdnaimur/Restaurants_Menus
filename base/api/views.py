from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Employees

from .serializers import EmployeesSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET/api',
        'GET/api/employee',
        'GET/api/employee/:id',
    ]
    return Response(routes)

# all employess data can achive 
@api_view(['GET'])
def getAllEmployee(request):
    employees = Employees.objects.all()
    serializer = EmployeesSerializer(employees,many = True)
    return Response(serializer.data)

# each employess data can achive 
@api_view(['GET'])
def getEmployee(request,pk):
    employee = Employees.objects.get(id = pk)
    serializer = EmployeesSerializer(employee,many = False)
    return Response(serializer.data)