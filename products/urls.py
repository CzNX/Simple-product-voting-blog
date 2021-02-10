from . import views
from django.urls import path

urlpatterns = [

    path('create/',views.create,name='create'),
    path('<int:product_id>/',views.detail,name='detail'),
    path('upvote/<int:product_id>/',views.upvote,name='upvote'),


]
