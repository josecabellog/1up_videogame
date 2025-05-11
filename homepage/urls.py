from django.urls import path
from .views import HomePageView, AboutPageView, CategoriesPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name= 'about'),
    path('categories/', CategoriesPageView.as_view(), name= 'categories'),
    path('contact/', ContactPageView.as_view(), name= 'contact'),
]