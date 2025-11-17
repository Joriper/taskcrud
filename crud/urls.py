from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("user/api/list_task",list_task),
    path("user/api/task/<int:_id>",UpdateandCreate.as_view()),
    path("user/api/task",UpdateandCreate.as_view()),
    path("user/api/delete/<int:_id>",delete_task),
    path("user/api/get_task/<int:_id>",get_task),
    path('',index)
]