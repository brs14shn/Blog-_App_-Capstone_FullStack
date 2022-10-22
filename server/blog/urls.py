

from django.urls import path,include
from .views import (
    CategoryViews,
)

urlpatterns = [
    path("category/",CategoryViews.as_view()),
  
]
