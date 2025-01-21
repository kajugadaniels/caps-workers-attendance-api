from base.models import *
from account.models import *
from base.serializers import *
from django.http import Http404
from account.serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class getUsers(APIView):
    """
    Retrieve a list of all users.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            message = {"detail": "Successfully retrieved all users."}
            return Response(
                {"data": serializer.data, "message": message},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            message = {
                "detail": "An error occurred while retrieving users.",
                "error": str(e),
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class addUser(APIView):
    """
    Create a new user.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = {"detail": "User created successfully."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_201_CREATED
                )
            else:
                message = {
                    "detail": "Error creating user. Please check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while creating the user.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class showUser(APIView):
    """
    Retrieve detailed information about a specific user.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404(f"User with id {id} does not exist.")

    def get(self, request, id, format=None):
        try:
            user = self.get_object(id)
            serializer = UserSerializer(user)
            message = {"detail": "User retrieved successfully."}
            return Response(
                {"data": serializer.data, "message": message},
                status=status.HTTP_200_OK
            )
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An error occurred while retrieving the user.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class editUser(APIView):
    """
    Update an existing user completely (PUT) or partially (PATCH).
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404(f"User with id {id} does not exist.")

    def put(self, request, id, format=None):
        """
        Handle complete update of a user.
        """
        try:
            user = self.get_object(id)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = {"detail": "User updated successfully."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_200_OK
                )
            else:
                message = {
                    "detail": "Error updating user. Please check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while updating the user.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, id, format=None):
        """
        Handle partial update of a user.
        """
        try:
            user = self.get_object(id)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                message = {"detail": "User updated successfully."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_200_OK
                )
            else:
                message = {
                    "detail": "Error updating user. Please check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while updating the user.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class deleteUser(APIView):
    """
    Delete a specific user.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404(f"User with id {id} does not exist.")

    def delete(self, request, id, format=None):
        try:
            user = self.get_object(id)
            user.delete()
            message = {"detail": "User deleted successfully."}
            return Response({"message": message}, status=status.HTTP_200_OK)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while deleting the user.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class getEmployees(APIView):
    """
    Retrieve a list of all employees.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            message = {"detail": "Successfully retrieved all employees."}
            return Response(
                {"data": serializer.data, "message": message},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            message = {
                "detail": "An error occurred while retrieving employees.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class addEmployee(APIView):
    """
    Create a new employee.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()  # calls create() in EmployeeSerializer
                message = {"detail": "Employee created successfully."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_201_CREATED
                )
            else:
                message = {
                    "detail": "Error creating employee. Please check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while creating the employee.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class showEmployee(APIView):
    """
    Retrieve detailed information about a specific employee.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404(f"Employee with id {id} does not exist.")

    def get(self, request, id, format=None):
        try:
            employee = self.get_object(id)
            serializer = EmployeeSerializer(employee)
            message = {"detail": "Employee retrieved successfully."}
            return Response(
                {"data": serializer.data, "message": message},
                status=status.HTTP_200_OK
            )
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An error occurred while retrieving the employee.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class editEmployee(APIView):
    """
    Update an existing employee completely (PUT) or partially (PATCH).
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404(f"Employee with id {id} does not exist.")

    def put(self, request, id, format=None):
        """
        Handle complete update of an employee.
        """
        try:
            employee = self.get_object(id)
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()  # calls update() in EmployeeSerializer
                message = {"detail": "Employee updated successfully (full update)."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_200_OK
                )
            else:
                message = {
                    "detail": "Error updating employee. Please check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while updating the employee.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, id, format=None):
        """
        Handle partial update of an employee.
        """
        try:
            employee = self.get_object(id)
            serializer = EmployeeSerializer(employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()  # calls update() in EmployeeSerializer
                message = {"detail": "Employee updated successfully (partial update)."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_200_OK
                )
            else:
                message = {
                    "detail": "Error updating employee. Please check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while updating the employee.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class deleteEmployee(APIView):
    """
    Delete a specific employee.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404(f"Employee with id {id} does not exist.")

    def delete(self, request, id, format=None):
        try:
            employee = self.get_object(id)
            employee.delete()
            message = {"detail": "Employee deleted successfully."}
            return Response({"message": message}, status=status.HTTP_200_OK)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while deleting the employee.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class getAttendances(APIView):
    """
    Retrieve a list of all attendance records.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            attendances = Attendance.objects.select_related('employee').all()
            serializer = AttendanceSerializer(attendances, many=True)
            message = {"detail": "Successfully retrieved all attendance records."}
            return Response(
                {"data": serializer.data, "message": message},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            message = {
                "detail": "An error occurred while retrieving attendance records.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class addAttendance(APIView):
    """
    Create a new attendance record for an employee based on finger_id.
    Enforces the 12-hour rule:
      - If the employee last tapped within 12 hours, raise an error.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            finger_id = request.data.get('finger_id', None)
            if not finger_id:
                return Response({
                    "message": {
                        "detail": "finger_id is required to record attendance."
                    }
                }, status=status.HTTP_400_BAD_REQUEST)

            # Retrieve employee via the provided finger_id
            try:
                employee = Employee.objects.get(finger_id=finger_id)
            except Employee.DoesNotExist:
                return Response({
                    "message": {
                        "detail": f"No employee found with finger_id={finger_id}"
                    }
                }, status=status.HTTP_404_NOT_FOUND)

            # Check if the last attendance was within 12 hours
            last_attendance = Attendance.objects.filter(employee=employee).order_by('-time_in').first()
            if last_attendance:
                time_diff = timezone.now() - last_attendance.time_in
                if time_diff < timedelta(hours=12):
                    return Response({
                        "message": {
                            "detail": (
                                f"You have already tapped in the last 12 hours. "
                                f"Please wait at least {12 - time_diff.seconds//3600} more hour(s)."
                            )
                        }
                    }, status=status.HTTP_400_BAD_REQUEST)

            # Build data for AttendanceSerializer:
            data = {
                "employee": employee.id,
                "finger_id": finger_id,
                "salary_snapshot": str(employee.salary),  # must be string for DecimalField
            }

            serializer = AttendanceSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                message = {"detail": "Attendance recorded successfully."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_201_CREATED
                )
            else:
                message = {
                    "detail": "Error creating attendance. Please check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while creating the attendance record.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class showAttendance(APIView):
    """
    Retrieve a specific attendance record by ID.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Attendance.objects.get(id=id)
        except Attendance.DoesNotExist:
            raise Http404(f"Attendance record with id {id} does not exist.")

    def get(self, request, id, format=None):
        try:
            attendance = self.get_object(id)
            serializer = AttendanceSerializer(attendance)
            message = {"detail": "Attendance record retrieved successfully."}
            return Response(
                {"data": serializer.data, "message": message},
                status=status.HTTP_200_OK
            )
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An error occurred while retrieving the attendance record.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class editAttendance(APIView):
    """
    Update an existing attendance record completely (PUT) or partially (PATCH).
    Typically, you might not change the time_in for an attendance record,
    but let's keep it open in case you need corrections or updates.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Attendance.objects.get(id=id)
        except Attendance.DoesNotExist:
            raise Http404(f"Attendance record with id {id} does not exist.")

    def put(self, request, id, format=None):
        """
        Full update of an attendance record.
        """
        try:
            attendance = self.get_object(id)
            serializer = AttendanceSerializer(attendance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = {"detail": "Attendance record fully updated successfully."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_200_OK
                )
            else:
                message = {
                    "detail": "Error updating attendance record. Check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while updating the attendance record.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, id, format=None):
        """
        Partial update of an attendance record.
        """
        try:
            attendance = self.get_object(id)
            serializer = AttendanceSerializer(attendance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                message = {"detail": "Attendance record partially updated successfully."}
                return Response(
                    {"data": serializer.data, "message": message},
                    status=status.HTTP_200_OK
                )
            else:
                message = {
                    "detail": "Error updating attendance record. Check the fields.",
                    "errors": serializer.errors
                }
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while updating the attendance record.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class deleteAttendance(APIView):
    """
    Delete a specific attendance record by ID.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Attendance.objects.get(id=id)
        except Attendance.DoesNotExist:
            raise Http404(f"Attendance record with id {id} does not exist.")

    def delete(self, request, id, format=None):
        try:
            attendance = self.get_object(id)
            attendance.delete()
            message = {"detail": "Attendance record deleted successfully."}
            return Response({"message": message}, status=status.HTTP_200_OK)
        except Http404 as e:
            message = {"detail": str(e)}
            return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = {
                "detail": "An unexpected error occurred while deleting the attendance record.",
                "error": str(e)
            }
            return Response({"message": message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
