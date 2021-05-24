import uuid

from django.http import JsonResponse

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from cowrywise.sample_app.models import UUIDStore
from cowrywise.sample_app.serializers import UUIDStoreSerializer


class UUIDAPIView(GenericAPIView):
    serializer_class = UUIDStoreSerializer
    queryset = UUIDStore
    def get(self, request, *args, **kwargs):
        try:
            generate_uuid = uuid.uuid4()
            uuids = UUIDStore.objects.create(random_uuid=generate_uuid)
            obj = self.queryset.objects.all()
            serializer = self.get_serializer(obj, many=True, context=self.get_serializer_context())
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as _:
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def server_error(request, *args, **kwargs):
    """
    Generic 500 error handler.
    """
    data = {
        'error': 'Internal Server error'
    }
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def not_found_request(request, exception, *args, **kwargs):
    """
    Generic 400 error handler.
    """
    data = {
        'error': 'api endpoint not found'
    }
    return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)
