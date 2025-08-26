from django.contrib import admin

# Register your models here.
from .models import canscan


class canscanAdmin(admin.ModelAdmin):
    list_display = ('Recycling_type', 'Green_points_earned', 'Bin_opened')

# Register your models here.


admin.site.register(canscan, canscanAdmin)
