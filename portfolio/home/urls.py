from django.contrib import admin
from django.urls import path,include
from home import views
#DJANGO header constumazation
admin.site.site_header="Developer Vamsi"
admin.site.site_title="Welcome to Vamsi's Dashboard"
admin.site.index_title="Welcome to this Portal"

urlpatterns = [
    #path("admin/", admin.site.urls),
    path("home", views.home,name="home"),
    path("about", views.about,name="about"),
    path("projects", views.projects,name="projects"),   
    path("contact", views.contact,name="contact"),
    ]