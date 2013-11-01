# We'll need the Selections class.
from apps.brain.selections import Selections


class Growth:
    """
    The `Growth` class manages the growth of networks,
    e.g., when new neurons are added. 

    """

    @staticmethod
    def add_neuron(details):
        print 'Adding neuron...'

    @staticmethod
    def add_links(neuron):
        print 'Adding links...'

    @staticmethod
    def grow_network():
        print 'Growing network...'
