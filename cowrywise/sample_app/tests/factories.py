import uuid
from factory import DjangoModelFactory, Faker
from cowrywise.sample_app.models import UUIDStore



class UUIDFactory(DjangoModelFactory):

    random_uuid = uuid.uuid4()
    class Meta:
        model = UUIDStore
