from rest_framework.serializers import ModelSerializer
from .models import User

class UserOverviewSerializer(ModelSerializer) :
    class Meta :
        model = User
        # fields = "__all__"

        fields = (
            # "id",
            "username",
            "name",
            # "email",
        )

class UserRequestSerializer(ModelSerializer) :
    class Meta : 
        model = User
        fields = (
            "username",
            "name",
            "email",
            "password",
        )

class UserSerializer(ModelSerializer) :
    class Meta :
        model = User
        fields = "__all__"

        # fields = (
        #     "id",
        #     "username",
        #     "password",
        #     "name",
        #     "email",
        # )