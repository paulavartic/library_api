from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('library.urls', namespace='library')),
    path('users/', include('users.urls', namespace='users')),
]
