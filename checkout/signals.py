# Post in this case means "after", so this implies these
# signals are sent to the entire application by django
# after a model instance is saved or deleted respectively.
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


# THESE TWO FUNCTIONS WERE TAKEN FROM CODE INSTITUTE'S MINI PROJECT
# Receiver decorator to execute this function anytime
# the post_save signal is sent from the OrderLineItem model.
@receiver(post_save, sender=OrderLineItem)
# This function will handle signals from the post_save event.
# So "sender" refers to the sender of the signal, in our case
# OrderLineItem. "Instance" refers to the instance of the model
# that sent it. "Created" is a boolean sent by Django referring
# to whether this is a new instance or one being updated.
# "**kwargs" refers to any keyword arguments.
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    # Access instance.order which refers to the order this
    # specific line item is related to, and call the update
    # total method on it.
    instance.order.update_total()


# This is to handle updating the various totals when
# a line item is deleted.
# The created parameter is absent because is not sent
# by this signal.
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
