from rest_framework import serializers

from ToDone.models import Task


class TaskSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        task = Task.objects.create(
            owner=self.context['request'].user,
            text=validated_data['text'])
        return task

    class Meta:
        model = Task
        exclude = ['owner', ]
