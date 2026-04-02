from django.contrib import admin

from core.models import NewsletterSubscriber


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    ordering = ('-created_at',)
