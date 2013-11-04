# We'll need our Selections class.
from apps.brain.selections import Select

# We'll need the exp() function from the math module.
from math import exp

class Computation:
    """
    The `Computation` class manages the computations that
    happen in networks (e.g., propagation, activation, etc).

    """

    @staticmethod
    def activate(network, inputs=[]):
        """
        Activate a network: give it inputs, get its output.
 
        """

        # Build the network in memory. 
        net = Computation.build_network(network)

        # Run the inputs through the network to get the outputs.
        outputs = Computation.activate_network(net, inputs)

        # Find the output layer neurons that lit up.
        top_level = len(outputs) - 1
        top_layer = outputs[top_level]
        results = []
        for index, neuron in enumerate(top_layer):
            if Computation.threshold(neuron.output):
                results.append(neuron)

        return results

    @staticmethod
    def build_network(network):
        layers = []
        for layer in Select.layers_in(network):
            neuron_list = []
            for pool in Select.pools_in(layer):
                for neuron in Select.neurons_in(pool):
                    neuron_list.append(neuron)
            layers.append(neuron_list)
        return layers

    @staticmethod
    def activate_network(layers, inputs=[]):

        for layer, neurons in enumerate(layers):
            is_input_layer = layer is 0
            for index, neuron in enumerate(neurons):
                if is_input_layer:
                    neuron.output = 1 if neuron.name in inputs else 0
                else:
                    weights = []
                    outputs = []
                    for i, node in enumerate(layers[layer - 1]):
                        outputs.append(node.output)
                        link = Select.link_between(node, neuron)
                        weights.append(link.weight)
                    weighted_sum = Computation.sum(outputs, weights)
                    neuron.output = Computation.activation(weighted_sum)
        return layers

    @staticmethod
    def backprop(layers, outputs=[], learning_rate=1):

        for layer, neurons in reversed(list(enumerate(layers))):
            is_input_layer = layer is 0
            is_top_layer = layer is len(layers) - 1
            if is_top_layer:
                for index, neuron in enumerate(neurons):
                    s = neuron.output * (1 - neuron.output)
                    neuron.ideal_output = 1 if neuron.name in outputs else 0
                    neuron.error = (neuron.ideal_output - neuron.output) * s
                    for i, node in enumerate(layers[layer - 1]):
                        link = Select.link_between(node, neuron)
                        link.weight += ((neuron.error * node.output) * learning_rate)
                        link.save()
            elif is_top_layer and not is_input_layer:
                for index, neuron in enumerate(neurons):
                    error_sum = 0
                    s = neuron.output * (1 - output.neuron)
                    for i, node in enumerate(layers[layer + 1]):
                        link = Select.link_between(neuron, node)
                        error_sum += node.error * link.weight
                    neuron.error = error_sum * s
                    for i, node in enumerate(layers[layer - 1]):
                        link = Select.link_between(node, neuron)
                        link.weight += ((neuron.error * node.output) * learning_rate)
                        link.save()

        return layers

    @staticmethod
    def train(layers, inputs, outputs, iterations=10):
        for i in range(0, iterations):
            for j, input in enumerate(inputs):
                layers = Computation.activate_network(layers, inputs[j])
                layers = Computation.backprop(layers, outputs[j])
        return layers

    @staticmethod
    def sum(outputs, weights, bias=0):
        sum = 0
        for i, item in enumerate(outputs):
            sum += (outputs[i] * weights[i])
        sum += bias
        return sum

    @staticmethod
    def activation(weighted_sum):
        return Computation.sigmoid(weighted_sum)

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + exp(-x))

    @staticmethod
    def threshold(x):
        return x > 0.5


