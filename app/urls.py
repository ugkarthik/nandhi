from django.urls import path

from .views import HomeView, BlogView, AboutUsView, MembersView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("aboutus/", AboutUsView.as_view(), name="aboutus"),
    path("members/", MembersView.as_view(), name="members"),
    path("blogs/", BlogView.as_view(), name="blogs"),
]