from django.db import models
from fractal_database.models import ReplicatedModel
from Mapapp.models import ServiceArea


class AlertModel(ReplicatedModel):
    alert_name = models.CharField(max_length=200, unique=True)
    statusChoices = [
        ("ACTIVE", "Active"),
        ("RESOLVED", "Resolved"),
    ]
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=statusChoices, default="ACTIVE")

    created_at = models.DateTimeField(auto_now_add=True)


class AlertServiceModel(ReplicatedModel):
    alert = models.ForeignKey(AlertModel, on_delete=models.CASCADE)
    service_area = models.ForeignKey(ServiceArea, on_delete=models.CASCADE)
