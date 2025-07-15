from django.db import models
from users.models import User

class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_system = models.CharField(max_length=255)
    compliance_standard = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Assessment on {self.target_system} by {self.user.username}"
    

class AssessmentResult(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='detailed_results')
    standard = models.CharField(max_length=50)  # NEW: OWASP or CIS
    result_data = models.JSONField()
    risk_score = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for Assessment on {self.assessment.target_system} with Risk Score {self.risk_score}"
