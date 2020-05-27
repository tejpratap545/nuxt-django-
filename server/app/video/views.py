from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action


class tagviewset(viewsets.ModelViewSet):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()


class videosviewset(viewsets.ModelViewSet):
    serializer_class = VideoSerializers
    queryset = video.objects.all()
    parser_classes = [JSONParser]
    @action(methods=['GET'], detail=True, url_path='Tag', url_name='tag name')
    def Tag(self, request, pk=None):
        tag = self.get_object()
        print(tag)
        tags = tag.tags
        serializer = TagSerializers(tags,  many=True)
        print(serializer)
        return Response(serializer.data, status=200)
