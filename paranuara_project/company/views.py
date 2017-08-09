from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Company, Employee
from .serializers import (EmployeeSerializer, EmployeeAttributeSerializer,
                          EmployeeFavoriteFoodSerializer)


class EmployeeListView(APIView):
    def get(self, request, format=None):
        """
        Given a company, this API returns all of their employees.
        If no company given, return 400 Bad Request with proper error message.

        GET - This returns a list of employees - /employee?company=company_name
        """
        company = get_object_or_404(Company,
                                    name=request.query_params.get('company'))
        employees = Employee.objects.filter(company=company)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


class EmployeeAttributeListView(APIView):
    def get(self, request, format=None):
        """
        Given two people provide their info and friends in common
        Given one people provide list of fruits and vegetable they like

        GET - /employee/attribute/?person1=username&person2=username
        GET - /employee/attribute/?person=username
        """
        person = request.query_params.get('person')
        person1 = request.query_params.get('person1')
        person2 = request.query_params.get('person2')

        if person1 and person2:
            emp1 = get_object_or_404(Employee, username=person1)
            emp2 = get_object_or_404(Employee, username=person2)
            emp1_serializer = EmployeeAttributeSerializer(emp1)
            emp2_serializer = EmployeeAttributeSerializer(emp2)
            common_friends = Employee.objects.filter(eye_color='brown',
                                                     has_died='False')
            common_friends_serializer = EmployeeAttributeSerializer(
                common_friends, many=True)
            return Response({'person1': emp1_serializer.data,
                             'person2': emp2_serializer.data,
                             'common_friends': common_friends_serializer.data})

        elif person:
            emp = get_object_or_404(Employee, username=person)
            emp_serializer = EmployeeFavoriteFoodSerializer(emp)
            return Response(emp_serializer.data)

        # If no argument supplied, return 400 with error message
        return Response({'error': 'Unrecognized argument.'}, status=400)
