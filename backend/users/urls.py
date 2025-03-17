from django.urls import path, include
from django.views.generic import TemplateView
from users.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
]
