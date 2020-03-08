from rest_framework import viewsets

from ToDone.models import Task
from ToDone.permissions import IsOwner
from ToDone.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsOwner, ]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
