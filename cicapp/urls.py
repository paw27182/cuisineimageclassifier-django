from django.urls import path

from .views import CuisineImageClassifierClass, appmain, index_view

urlpatterns = [
    path('', index_view),
    path('cicapp/', CuisineImageClassifierClass.as_view()),  # classed-based view
    path('cicapp/appmain/', appmain)
]
