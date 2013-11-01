# We'll use django's built-in models.
from django.db import models

# We'll use django's built-in User model.
from django.contrib.auth.models import User

# For regular expressions
import re

# For sending emails. 
from django.core.mail import send_mail

# For broadcasting messages project wide.
from pubsub import pub

# The pubsub module needs to know who's subscribed.
import project.subscriptions


class Bag(models.Model):
    """
    The `Bag` class represents a bag
    to stuff scribbles into.

    """

    # A name for the bag.
    name = models.CharField("Name", max_length=50)

    # A description for the bag.
    description = models.CharField("Bag description", max_length=200, blank=True)

    # Who owns this bag?
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    """
    The `Category` class identifies the type of scribble 
    that gets stuffed into a bag.

    """

    # A name for the category.
    name = models.CharField("Name", max_length=50)

    # A description for the category.
    description = models.CharField("Description", max_length=200, blank=True)

    # Who owns this category?
    owner = models.ForeignKey(User)

    # Which bag does this category belong to?
    bag = models.ForeignKey(Bag)

    # A regex pattern that matches valid scribbles for this category.
    valid_pattern = models.CharField("Valid pattern", max_length=500, blank=True, help_text="A regex pattern that matches valid scribbles for this category")

    def __unicode__(self):
        return self.name

    class Meta:
        """
        This handles meta-level properties of the class.

        """

        # How do we display this class in the plural?
        verbose_name_plural = 'Categories'


class Scribble(models.Model):
    """
    The `Scribble` class represents scribbles that get stuffed into bags.

    """

    # What is the content of this scribble?
    content = models.CharField("Content", max_length=100, blank=True)

    # Which category does this scribble belong under?
    category = models.ForeignKey(Category)

    # What time was the scribble sent?
    time_sent = models.IntegerField("Time Sent (UTC)", max_length=100, blank=True, help_text="The time the scribble was sent, as a UTC time stamp")

    # What time was the scribble received?
    time_received = models.DateTimeField("Time received", auto_now=True)

    # Who owns this scribble?
    owner = models.ForeignKey(User)

    # What group of scribbles does this belong to?
    group_key = models.CharField("Group key", max_length=100, blank=True, help_text="An identifier for the group this scribble belongs to")

    # What session does this scribble belong to?
    session_key = models.CharField("Session key", max_length=100, blank=True, help_text="An identifier for the session this scribble belongs to")

    def __unicode__(self):
        return self.group_key + ' ' + str(self.category) + ' ' + self.content

    def save(self, *args, **kwargs):
        """
        This method is called whenever anybody tries to save this model.

        """

        # Check that the data is valid.
        self.check_validation()

        # Now save the scribble
        super(Scribble, self).save(*args, **kwargs)

        # Broadcast that we've saved a scribble.
        pub.sendMessage('new scribble', details=self)

    def check_validation(self):
        """
        Checks the scribble against its category's pattern.
        If it doesn't match, an email gets sent.

        """

        # Check if the submitted content matches the valid pattern
        # recorded for the category.
        pattern = self.category.valid_pattern
        subject = self.content
        match = re.search(pattern, subject)

        # If no match, send an email.
        if match is None:
            subject_line = 'Baglady scribble error'
            message = 'The %s %s did not match the pattern %s' % (self.category.name, subject, pattern)
            send_to = ['jt@nara.me']
            sent_from = 'baglady@nara.me'
            send_mail(subject_line, message, sent_from, send_to, fail_silently=False)


