from django.contrib.auth import get_user_model
import factory

class UserFactory(factory.DjangoModelFactory):
   last_name = factory.Faker('name')
   username = factory.Faker('email')
   email = factory.Faker('email')
   password = factory.PostGenerationMethodCall('set_password', '123456')
   is_active = True

   class Meta:
       model = get_user_model()
