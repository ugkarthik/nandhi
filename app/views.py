from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse

from .forms import MembershipForm
from .models import Membership, Contact

class HomeView(TemplateView):

    template_name = 'app/home.html'


class AboutUsView(TemplateView):
    template_name = 'app/aboutus.html'

class ContactUsView(CreateView):
    template_name = 'app/contactus.html'
    model = Contact
    success_url = "/membership/success/"
    fields = ('name', 'email', 'phone', 'message')


class MembersView(CreateView):
    template_name = 'app/members.html'
    model = Membership
    success_url = "/membership/success/"
    fields = ('name', 'email', 'phone', 'business_location', 'business_description')


class BlogView(TemplateView):
    template_name = 'app/blog.html'


class MessageSubmitView(TemplateView):
    template_name = 'app/message_submit_output.html'