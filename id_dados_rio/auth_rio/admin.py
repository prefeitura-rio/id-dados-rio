# -*- coding: utf-8 -*-
from django.contrib import admin

from id_dados_rio.auth_rio.models import (
    Domain,
    Token,
    Access,
)


class AccessInline(admin.TabularInline):
    model = Access


class DomainAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "is_active")
    inlines = [AccessInline]


class TokenAdmin(admin.ModelAdmin):
    list_display = ("user", "domain", "is_active")
    inlines = [AccessInline]


class AccessAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "success", "domain")


admin.site.register(Domain, DomainAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(Access, AccessAdmin)
