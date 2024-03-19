from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'rating',
        'content',
        'created_at',
    )

    ordering = ('created_at',)


admin.site.register(Review, ReviewAdmin)
