from django.contrib import admin
from . models import BikeModel,User

# Register models
admin.site.register(BikeModel)
admin.site.register(User)