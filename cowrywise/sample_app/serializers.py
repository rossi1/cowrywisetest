from rest_framework import serializers

from cowrywise.sample_app.models import UUIDStore

class UUIDStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UUIDStore
        fields = ("id", "random_uuid", "time_stamp")

    def to_representation(self, instance):
        return {str(instance.time_stamp): str(instance.random_uuid)}
