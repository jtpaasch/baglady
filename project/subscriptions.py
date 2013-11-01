# We'll use the pubsub module to listen for messages.
from pubsub import pub


# Convert info about the scribble into info a neuron can use.
def convert_scribble_to_neuron(details):
    print 'New scribble'

# Listen for broadcasts about new scribbles.
pub.subscribe(convert_scribble_to_neuron, 'new scribble')
