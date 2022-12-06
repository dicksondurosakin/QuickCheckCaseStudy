from rest_framework import viewsets
from CaseStudy2.models import News
from .api import serializers


class NewsViewset(viewsets.ModelViewSet):

    queryset = News.objects.all()[:100]
    serializer_class = serializers.NewsSerializer
