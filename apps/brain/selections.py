# We'll use our models.
from apps.brain.models import Network, Layer, Pool, Neuron, Link


class Select:
    """
    The `Selections` class provides easy ways of 
    selecting sets of layers, pools, neurons, and links.

    """

    @staticmethod
    def find(criterion, list):
        """
        This method finds an item in a list that matches the 
        specified criteria. The criteria is a function which 
        takes an item as an argument and returns True or False.

        """
        for item in list:
            if criterion(item):
                return item

    @staticmethod
    def layers_in(network):
        """
        Retrieves all layers in the specified network.

        """
        return Layer.objects.filter(network=network).order_by('level')

    @staticmethod
    def pools_in(layer):
        """
        Retrieves all layers in the specified layer.

        """
        return Pool.objects.filter(layer=layer)

    @staticmethod
    def next(layer):
        """
        Retrieves the next highest layer.

        """
        return Layer.objects.filter(level=layer.level+1)

    @staticmethod
    def previous(layer):
        """
        Retrieves the previous lower layer.

        """
        return Layer.objects.filter(level=layer.level-1)

    @staticmethod
    def neurons_in(pool):
        """
        Retrieves all neurons in a pool.

        """
        return Neuron.objects.filter(pool=pool)

    @staticmethod
    def links_from(neuron):
        """
        Retrieves all links coming out of the specified neuron.

        """
        return Link.objects.filter(linked_from=neuron)

    @staticmethod
    def link_between(neuron1, neuron2):
        """
        Retrieves a link between two neurons.

        """
        return Link.objects.get(linked_from=neuron1, linked_to=neuron2)

    @staticmethod
    def links_to(neuron):
        """
        Retrieves all links coming into the specified neuron.

        """
        return Link.objects.filter(linked_to=neuron)
