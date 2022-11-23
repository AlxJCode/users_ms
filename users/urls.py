from django.urls import path
from users.api_views.data_views import *


urlpatterns = [

    # System users
    path('data/', DataView.as_view()),
]