from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


# THIS CLASS WAS TAKEN FROM CODE INSTITUTE'S MINI PROJECT
# User profile model for maintaining default
# merch delivery information and order history.
class UserProfile(models.Model):
    # This field is to specify each user can only have one profile.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # These fields are delivery information we want the user to be able
    # to provide defaults for.
    # We want this fields to be optional hence the blank and null true.
    default_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True,
                                            blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True,
                                   blank=True)

    def __str__(self):
        return self.user.username


# Each time a user object is saved we either create a profile if it
# has just been created or update an existing one.
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
