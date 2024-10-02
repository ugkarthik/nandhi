from django.urls import path

from .views import HomeView, BlogView, AboutUsView, MembersView, MessageSubmitView, ContactUsView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("aboutus/", AboutUsView.as_view(), name="about-us"),
    path("contact-us/", ContactUsView.as_view(), name="contact-us"),
    path("members/", MembersView.as_view(), name="members"),
    path("blogs/", BlogView.as_view(), name="blogs"),
    path("membership/success/", MessageSubmitView.as_view(), name="form-submit-message"),
]