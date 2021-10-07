from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import AdminRenderer
from . serializer import UserSerializer, CandidatesSerializer, GroupSerializer
from . models import Candidates
from django_filters import rest_framework as filters


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [AdminRenderer]
    filterset_fields = ('username', 'email',)



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [AdminRenderer]
    filterset_fields = ('name', 'url',)



class CandidatesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows candidates to be viewed or edited.
    """
    queryset = Candidates.objects.all().order_by('-created_at')
    serializer_class = CandidatesSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [AdminRenderer]
    filterset_fields = ('title', 'skills', 'nationality', 'age')