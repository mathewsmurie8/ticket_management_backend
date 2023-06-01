import json
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Ticket
from .serializers import TicketSerializer, LoginSerializer, UserSerializer


class UsersView(APIView):
    def get(self, request, format=None):
        users = User.objects.all().annotate()
        serializer = UserSerializer(users, many=True)
        data = json.dumps(serializer.data)
        return Response(json.loads(data))


class TicketList(APIView):
    querset = Ticket.objects.all()
    serializer = TicketSerializer
    def get(self, request, format=None):
        tickets = Ticket.objects.all().annotate()
        serializer = TicketSerializer(tickets, many=True)
        data = json.dumps(serializer.data)
        return Response(json.loads(data))

    def post(self, request, format=None):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDetail(APIView):
    """
    Retrieve, update or delete a ticket instance.
    """

    def get_object(self, pk):
        try:
            return Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    def put(self, request, pk, format=None): #todo: Add error handling
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ticket = self.get_object(pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterView(generics.ListCreateAPIView): #todo: Add error handling
    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')
        user, _ = User.objects.get_or_create(
            username=username, email=email, first_name=first_name, last_name=last_name, is_staff=True)
        user.set_password(password)
        content_type = ContentType.objects.get_for_model(Ticket)
        permissions = Permission.objects.filter(content_type=content_type)
        for permission in permissions:
            user.user_permissions.add(permission)
        user.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username, 'userid': user.id}, status=status.HTTP_201_CREATED)


class LoginView(generics.ListCreateAPIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            responseData = {'token': token.key, 'username': user.username, 'userid': user.id}
            return Response(responseData, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class DashboardView(APIView):
    def get(self, request, format=None):
        dashboard_payload = []
        users = User.objects.all()
        for user in users:
            number_of_tickets = Ticket.objects.filter(assigned_user=user).count()
            user_ticket_payload = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'username': user.username,
                'number_of_tickets': number_of_tickets
            }
            dashboard_payload.append(user_ticket_payload)
        return Response(dashboard_payload, status=status.HTTP_200_OK)
