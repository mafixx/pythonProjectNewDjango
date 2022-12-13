from django.urls import path

from .views import index

app_name = "finances"

urlpatterns = [
    path("", index, name="index")

]
