from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'custom_sentiment_fetch'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=views.custom_sentiment, name='custom_sentiment'),
    
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
