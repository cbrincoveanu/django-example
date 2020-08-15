from django.contrib import admin

from .models import Currency, Profile, UserAsset

admin.site.register(Currency)
admin.site.register(Profile)
admin.site.register(UserAsset)
