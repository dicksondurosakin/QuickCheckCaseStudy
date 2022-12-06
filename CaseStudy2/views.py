from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
from rest_framework import generics
import requests
from CaseStudy2.models import News
from django.core.paginator import Paginator
from CaseStudy2.api.serializers import NewsSerializer
# Create your views here.


def get_news(request):
    print("you refreshed the page")
    # I want to know the maximum number of items in the database
    url = "https://hacker-news.firebaseio.com/v0/maxitem.json"
    payload = "{}"
    response = requests.request("GET", url, data=payload)
    max_item = response.json()
    print(max_item)

    # get the filter by type keyword
    item_type = request.GET.get('type')
    search_item = request.GET.get('search')

    if search_item != None:
        news_list = News.objects.all().filter(
            text__icontains=search_item).order_by('-id')
    elif item_type == None or item_type == "all":
        news_list = News.objects.all().order_by('-id')
    else:
        news_list = News.objects.all().filter(type=item_type).order_by('-id')

    # paginate
    paginator = Paginator(news_list, 10)
    page_number = request.GET.get('page', 1)
    news = paginator.page(page_number)
    return render(request, 'CaseStudy2/index.html', {'news': news})
