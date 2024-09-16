from django.urls import path
from . import views
from django.urls import path, include
from quotes.views import register

urlpatterns = [
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quotes/', include('quotes.urls')),
    path('accounts/register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')), 
]