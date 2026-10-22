from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    SKILL_TYPE_CHOICES = [
        ('offer', 'Offering'),
        ('request', 'Requesting'),
    ]
    
    # This line is now active and correctly links a Skill to a User.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    skill_type = models.CharField(max_length=10, choices=SKILL_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} ({self.get_skill_type_display()}) by {self.user.username}"
