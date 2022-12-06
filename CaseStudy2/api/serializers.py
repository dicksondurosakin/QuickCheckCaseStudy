from rest_framework import serializers
from CaseStudy2.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
