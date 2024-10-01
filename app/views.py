from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):

    template_name = 'app/home.html'


class AboutUsView(TemplateView):
    template_name = 'app/aboutus.html'


class MembersView(TemplateView):
    template_name = 'app/members.html'


class BlogView(TemplateView):
    template_name = 'app/blog.html'