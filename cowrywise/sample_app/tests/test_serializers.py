from django.test import TestCase

from rest_framework.test import APIRequestFactory
from rest_framework.request import Request


from cowrywise.sample_app.serializers import UUIDStoreSerializer
from .factories import UUIDFactory


factory = APIRequestFactory()


class TestSerializer(TestCase):

    def test_user_serializer(self):
        proto_uuid = UUIDFactory.build()
        request = Request(factory.get("/"))
        serializer = UUIDStoreSerializer(data=
            {
            "random_uuid": proto_uuid.random_uuid,
            },
            context={"request": request}
        )
        self.assertTrue(serializer.is_valid(), msg="Data is valid")
        self.assertEqual(serializer.validated_data["random_uuid"], proto_uuid.random_uuid, msg="both equals")

        # creating a user
        serializer.save()

         # The user with proto_user params already exists,
        # hence cannot be created.
        serializer = UUIDStoreSerializer(data=
            {
            "random_uuid": proto_uuid.random_uuid,
            },
            context={"request": request}
        )


        self.assertFalse(serializer.is_valid())
        self.assertTrue(len(serializer.errors) == 1)
        self.assertIn("random_uuid", serializer.errors)

