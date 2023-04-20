from django.urls import path
from .views import ContactFormView, AboutView


urlpatterns = [
    path('', ContactFormView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
]
