from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
#URL: http://127.0.0.1:8000/post/1/
#Django expects an integer value and will transfer 
# it to a view as a variable called pk.
