from django.contrib import admin
from .models import Assessment, AssessmentResult
from django.utils.safestring import mark_safe
import json

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'target_system', 'compliance_standard', 'created_at')
    search_fields = ('target_system', 'user__username', 'compliance_standard')


@admin.register(AssessmentResult)
class AssessmentResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'assessment', 'risk_score', 'completed_at', 'short_result_data')
    readonly_fields = ('formatted_result_data',)

    def short_result_data(self, obj):
        if obj.result_data:
            return str(obj.result_data)[:75] + "..."
        return "No Data"

    short_result_data.short_description = 'Result Data Preview'

    def formatted_result_data(self, obj):
        if obj.result_data:
            return mark_safe(f'<pre>{json.dumps(obj.result_data, indent=2)}</pre>')
        return "No Data Available"

    formatted_result_data.short_description = 'Full Result Data'