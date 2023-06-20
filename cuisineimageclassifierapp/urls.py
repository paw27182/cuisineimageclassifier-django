from django.urls import path
from .views import CuisineImageClassifierClass
from .views import appmain

urlpatterns = [
    path('cuisineimageclassifierapp/', CuisineImageClassifierClass.as_view()),  # classed-based view
    path('cuisineimageclassifierapp/appmain/', appmain)
]
