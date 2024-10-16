# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView

app_name = 'djangoapp'
urlpatterns = [
    
    
    # path for dealer view
    # path for dealer details view

    path(route='register', view=views.register, name='register'),
    path(route='login', view=views.login_user, name='login'),
    path(route='logout', view=views.logout_request, name='logout'),
    path(route='get_cars', view=views.get_cars, name='get_cars'),

    # path for dealer reviews view
    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
