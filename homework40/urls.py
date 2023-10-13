from django.contrib import admin
from django.urls import path
from HW40.views import account, home,profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qwerty/', home, name='home'),
    path('account/', account, name='account'),
    path('profile/', profile, name='profile'),

]
