from rest_framework import serializers
from .models import Board
from users.serializers import UserOverviewSerializer

class BoardOverviewSerializer(serializers.ModelSerializer) :
    author = UserOverviewSerializer(read_only=True)

    class Meta : 
        model = Board
       
        fields = (
            "pk",
            "title",
            "author",
            "created_at"
        )

class BoardRequestSerializer(serializers.ModelSerializer) :
    author = UserOverviewSerializer(read_only=True)

    class Meta :
        model = Board
        fields = (
            "author",
            "title",
            "content",
            "loadedfile",
        )

class BoardSerializer(serializers.ModelSerializer) :
    author = UserOverviewSerializer(read_only=True)

    class Meta : 
        model = Board
        fields = "__all__"
        # depth = 1


        # exclude = (
        #     'code',
        # )