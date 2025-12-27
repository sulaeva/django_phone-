from django.contrib import admin

from .models import Phone

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price')
    list_filter = ('brand', 'price', 'model')
    search_fields = ('brand', 'model', 'price')


admin.site.register(Phone, PhoneAdmin)

