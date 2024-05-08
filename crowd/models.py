from django.db import models


class CrowdDensity(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    density = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Crowd Density: {self.density} at {self.timestamp}"
