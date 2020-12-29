from django.urls import path
from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

'''
path("", views.home, name="home"),
'''

urlpatterns = [
    path("", home_list_view, name="home"),  # Replace the existing path for ""
    path("hello/<name>", views.hello_there, name="hello_there"),   # This is a route
    path("Hello/<name>", views.hello_there, name="hello_there"),   # To be resistant to wrong spelling
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
]