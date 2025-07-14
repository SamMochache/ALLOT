from django.db import models

class Threat(models.Model):
    threat_type = models.CharField(max_length=255)
    description = models.TextField()
    source = models.CharField(max_length=255)
    risk_score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.threat_type