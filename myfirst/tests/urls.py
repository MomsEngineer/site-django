from django.urls import path
from . import views

app_name = 'tests'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:test_id>/', views.detail, name = 'detail'),
    path('<int:test_id>/leave_comment/', views.comment, name = 'comment'),
]
