from rest_framework import serializers
from .models import *


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class VideoSerializers(serializers.ModelSerializer):
    tag_id = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=Tag.objects.all(), source='tags')

    class Meta:
        model = video
        fields = ('__all__')
