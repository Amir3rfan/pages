from django.urls import path
from .views import HomePageview, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageview.as_view(), name='home'),
]