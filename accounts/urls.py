from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('<username>/', views.UserDetail.as_view()),
]