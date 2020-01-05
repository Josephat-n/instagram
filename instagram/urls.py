from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('insta.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('login/', LoginView.as_view(template_name= '/'), name='user_login'),
]