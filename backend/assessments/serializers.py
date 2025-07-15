from rest_framework import serializers
from .models import Assessment, AssessmentResult

class AssessmentSerializer(serializers.ModelSerializer):
    latest_risk_score = serializers.SerializerMethodField()
    latest_standard = serializers.SerializerMethodField()   # NEW

    class Meta:
        model = Assessment
        fields = '__all__'  # or ['id', 'user', ..., 'latest_risk_score']

    def get_latest_risk_score(self, obj):
        latest_result = obj.detailed_results.order_by('-completed_at').first()
        return int(latest_result.risk_score) if latest_result and latest_result.risk_score is not None else None
    
    def get_latest_standard(self, obj):
        latest_result = obj.detailed_results.order_by('-completed_at').first()
        return latest_result.standard if latest_result else None


class AssessmentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentResult
        fields = '__all__'