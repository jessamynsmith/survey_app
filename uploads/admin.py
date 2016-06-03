from django.contrib import admin

# Register your models here.
from .models import Survey

class SurveyAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "title"]
	class Meta:
		model = Survey



admin.site.register(Survey, SurveyAdmin)