from django.contrib import admin
from .models import Pessoa, Animal,BanhoeTosa,Login

# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Animal)
admin.site.register(BanhoeTosa)
admin.site.register(Login)