# We'll use django's base models.
from django.db import models

# We'll use django's built-in User class too.
from django.contrib.auth.models import User

# We'll need random numbers to initialize weights.
from random import random


class AbstractBrainModel(models.Model):
    """
    This class provides some basic functionality for subclasses.

    """

    def save(self, *args, **kwargs):
        """
        This method is called whenever anybody tries to save the model.

        """

        # If no name, generate one.
        if not self.name:
            label = self.__class__.__name__.lower()
            self.name = label + '-' + str(self.id)

        # Now save it.
        super(AbstractBrainModel, self).save(*args, **kwargs)


class Network(AbstractBrainModel):
    """
    The `Network` class represents a neural network.

    """

    # A name for the network.
    name = models.CharField("Name", max_length=255, blank=True)

    # An optional description.
    description = models.CharField("Description", max_length=255, blank=True)

    # Who owns this network?
    owner = models.ForeignKey(User)

    # An optional learning rate.
    learning_rate = models.FloatField("Learning rate", default=1,
        help_text="A rate of 1.0 has no effect")

    def __unicode__(self):
        return self.name


class Layer(AbstractBrainModel):
    """
    The `Layer` class represents a layer in a network.

    """

    # A name for the layer.
    name = models.CharField("Name", max_length=255, blank=True)

    # An optional description.
    description = models.CharField("Description", max_length=255, blank=True)

    # Who owns this network?
    owner = models.ForeignKey(User)

    # Which network does this layer belong to?
    network = models.ForeignKey(Network)

    # Which level in the stack of layers does this layer occupy?
    # Note: 0 is the bottom layer (input layer).
    level = models.PositiveIntegerField(unique=True)

    def __unicode__(self):
        return self.name


class Pool(AbstractBrainModel):
    """
    The `Pool` class represents a pool of neurons 
    (i.e., neurons of the same type).

    """

    # A name for the pool.
    name = models.CharField("Name", max_length=255, blank=True)

    # An optional description.
    description = models.CharField("Description", max_length=255, blank=True)

    # Who owns this pool?
    owner = models.ForeignKey(User)

    # Which layer does this pool belong in?
    layer = models.ForeignKey(Layer)

    def __unicode__(self):
        return self.name


class Neuron(AbstractBrainModel):
    """
    The `Neuron` class represents a neuron.

    """

    # A name for the neuron.
    name = models.CharField("Name", max_length=255, blank=True)

    # An optional description.
    description = models.CharField("Description", max_length=255, blank=True)

    # Who owns this neuron?
    owner = models.ForeignKey(User)

    # Which pool does this neuron belong in?
    pool = models.ForeignKey(Pool)

    # An optional bias (the weight of the bias).
    bias = models.FloatField("Bias weight", default=0,
        help_text="A weight of 0 has no effect")

    # An optional key that neurons can be grouped by.
    group_key = models.CharField("Group key", max_length=255, blank=True)

    def __unicode__(self):
        return self.name


class Link(AbstractBrainModel):
    """
    The `Link` class represents a connection between neurons.

    """

    # A name for the link.
    name = models.CharField("Name", max_length=255, blank=True)

    # Who owns this link?
    owner = models.ForeignKey(User)

    # Which neuron is this linked from?
    linked_from = models.ForeignKey(Neuron, related_name="linked_from")

    # Which neuron is this linked to?
    linked_to = models.ForeignKey(Neuron, related_name="linked_to")

    # What is the weight of this link?
    weight = models.FloatField("Weight", default=random)

    def __unicode__(self):
        from_name = '|' + self.linked_from.name + '|'
        to_name = '|' + self.linked_to.name + '|'
        return 'link-' + from_name  + '-' + to_name

