from django.contrib import admin
from .models import StreamingService, SocialLink, Track

admin.site.register(StreamingService)
admin.site.register(SocialLink)
admin.site.register(Track)
