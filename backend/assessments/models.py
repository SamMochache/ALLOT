from django.db import models
from users.models import User

class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_system = models.CharField(max_length=255)
    compliance_standard = models.CharField(max_length=255)
    results = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Assessment on {self.target_system} by {self.user.username}"