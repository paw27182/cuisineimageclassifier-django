from django.urls import path
from .views import CuisineImageClassifierClass
from .views import execute

urlpatterns = [
    path('cuisineimageclassifierapp/', CuisineImageClassifierClass.as_view()),  # classed-based view
    path('cuisineimageclassifierapp/execute/', execute)
]
