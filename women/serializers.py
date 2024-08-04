from rest_framework import serializers
from .models import Women


class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title', 'cat_id')

        # fields = "__all__"   #todo Вывести все записи