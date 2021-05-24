from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from cowrywise.sample_app.models import UUIDStore
from cowrywise.sample_app.serializers import UUIDStoreSerializer


class UUIDTests(APITestCase):

    def test_uuid_list_view(self):
        url = reverse('uuid_list')
        response = self.client.get(url, format='json')
        obj = UUIDStore.objects.all()
        serializer = UUIDStoreSerializer(obj, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
