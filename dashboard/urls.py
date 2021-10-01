from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'dashboard'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=views.index, name='index'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
