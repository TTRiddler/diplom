from django.contrib import admin
from .models import NumericSystem, NumericSection, AlgebraicSystem, AlgebraicSection


class NumericInline(admin.StackedInline):
	model = NumericSection
	extra = 0


class NumericAdmin(admin.ModelAdmin):
	inlines = [NumericInline]


class AlgebraicInline(admin.StackedInline):
	model = AlgebraicSection
	extra = 0


class AlgebraicAdmin(admin.ModelAdmin):
	inlines = [AlgebraicInline]


admin.site.register(NumericSystem, NumericAdmin)
admin.site.register(AlgebraicSystem, AlgebraicAdmin)