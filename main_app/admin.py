from django.contrib import admin

# Register your models here.
from django.contrib import admin
# import your models here
from .models import Burger, Feeding
from .models import Happymeal
from .models import User
# Register your models here
admin.site.register(Burger)
admin.site.register(Feeding)
admin.site.register(Happymeal)

