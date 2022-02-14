from django.contrib import admin

# Added these lines. - Arica

from .models import Todo

admin.site.register(Todo)
