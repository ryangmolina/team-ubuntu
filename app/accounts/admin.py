from django.contrib import admin

from .models import Account, Profile


class AccountAdmin(admin.ModelAdmin):

    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_active',
    )

    list_filter = (
        'is_active',
    )


admin.site.register(Account, AccountAdmin)
admin.site.register(Profile)