from rest_framework import serializers
from todo_app.models import task


class taskserializer(serializers.ModelSerializer):
    class Meta:
        model=task
        fields='__all__'
