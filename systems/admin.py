from django.contrib import admin
from .models import NumericSystem, NumericSection, AlgebraicSystem, AlgebraicSection, AlgebraicSubsection


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


class AlgebraicSectionInline(admin.StackedInline):
	model = AlgebraicSubsection
	extra = 0


class AlgebraicSectionAdmin(admin.ModelAdmin):
	inlines = [AlgebraicSectionInline]



admin.site.register(NumericSystem, NumericAdmin)
admin.site.register(AlgebraicSystem, AlgebraicAdmin)
admin.site.register(AlgebraicSection, AlgebraicSectionAdmin)