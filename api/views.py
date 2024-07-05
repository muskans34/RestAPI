
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from base.models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def user_projects(self, request):
        user = request.user
        projects = user.projects.all()
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)
