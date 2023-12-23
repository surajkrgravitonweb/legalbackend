# from .serializers import UserSerializers
from .serializers import UserSerializers, UserLoginSerializer

from .models import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import Response


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class AuthUserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'email': serializer.data['email'],
                'role': serializer.data['role']
            }

            return Response(response, status=status_code)
        

from rest_framework import generics
from .models import *
from .serializers import *

class UserFormListCreateView(generics.ListCreateAPIView):
    queryset = UserForm.objects.all()
    serializer_class = UserFormSerializer

class UserFormDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserForm.objects.all()
    serializer_class = UserFormSerializer

class UserFormDocumentCreateView(generics.ListCreateAPIView):
    queryset = UserFormDocument.objects.all()
    serializer_class = UserFormDocumentSerializer

class UserFormDocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserFormDocument.objects.all()
    serializer_class = UserFormDocumentSerializer




class AllPagesApiListCreateView(generics.ListCreateAPIView):
    queryset = AllPagesApi.objects.all()
    serializer_class = AllPagesApiSerializer

from rest_framework import viewsets
class UserOutputViewSet(viewsets.ModelViewSet):
    queryset = UserOutput.objects.all()
    serializer_class = UserOutputSerializer

class AllPAgesByAgentControlViewSet(viewsets.ModelViewSet):
    queryset = AllPAgesByAgentControl.objects.all()
    serializer_class = AllPAgesByAgentControlSerializer







# not used
class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
