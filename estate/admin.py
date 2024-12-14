from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(State)
admin.site.register(City)
admin.site.register(PropertyType)
admin.site.register(Property)
admin.site.register(Enquiry)
admin.site.register(Feedback)
admin.site.register(UserType)