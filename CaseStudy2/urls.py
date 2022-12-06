from django.urls import path, include
from . import views
from CaseStudy2.viewsets import NewsViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('news', NewsViewset)

app_name = "case_study"
urlpatterns = [
    path('', views.get_news, name='get_news'),
    path('api/', include(router.urls)),

]
