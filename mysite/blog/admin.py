from django.contrib import admin
from blog.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    # extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question info',               {'fields': ['question']}),
        ('Date info', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_filter = ['pub_date']
    list_display = ('question', 'pub_date', 'was_published_recently')
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice)