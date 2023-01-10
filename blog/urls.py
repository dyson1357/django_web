from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    # CBV 버전 코드
    path('', views.PostList.as_view()),

    # FBV 버전 코드
    # path('', views.index),
]
