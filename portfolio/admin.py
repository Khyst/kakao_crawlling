from django.contrib import admin
from .models import Portfolio
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter  # 모듈 불러오기


# Register your models here.
# admin.py
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'image', 'description']
    """list_filter = ('gender',
        ('hire_date', DateRangeFilter),
        ('birth_date', DateRangeFilter),
    )"""
    search_fields = ['title', 'description']

#admin.site.register(Portfolio)
admin.site.register(Portfolio, PortfolioAdmin)


