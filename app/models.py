from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Currency(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class UserAsset(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='user_assets')
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=19, decimal_places=10)

    class Meta:
        unique_together = (("profile", "currency"),)

    def __str__(self):
        return f"{str(self.profile)} ({str(self.currency)})"
