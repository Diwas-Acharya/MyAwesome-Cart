from django.contrib import admin

# Register your models here.
from .models import product,mycontact,myOrder,OrderUpdate

admin.site.register(product)
admin.site.register(mycontact)
admin.site.register(myOrder)
admin.site.register(OrderUpdate)
