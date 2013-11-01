# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AbstractBrainModel'
        db.create_table(u'brain_abstractbrainmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'brain', ['AbstractBrainModel'])

        # Adding model 'Network'
        db.create_table(u'brain_network', (
            (u'abstractbrainmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['brain.AbstractBrainModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('learning_rate', self.gf('django.db.models.fields.FloatField')(default=1)),
        ))
        db.send_create_signal(u'brain', ['Network'])

        # Adding model 'Layer'
        db.create_table(u'brain_layer', (
            (u'abstractbrainmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['brain.AbstractBrainModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('network', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brain.Network'])),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
        ))
        db.send_create_signal(u'brain', ['Layer'])

        # Adding model 'Pool'
        db.create_table(u'brain_pool', (
            (u'abstractbrainmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['brain.AbstractBrainModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('layer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brain.Layer'])),
        ))
        db.send_create_signal(u'brain', ['Pool'])

        # Adding model 'Neuron'
        db.create_table(u'brain_neuron', (
            (u'abstractbrainmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['brain.AbstractBrainModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('pool', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brain.Pool'])),
            ('bias', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('group_key', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'brain', ['Neuron'])

        # Adding model 'Link'
        db.create_table(u'brain_link', (
            (u'abstractbrainmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['brain.AbstractBrainModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('linked_from', self.gf('django.db.models.fields.related.ForeignKey')(related_name='linked_from', to=orm['brain.Neuron'])),
            ('linked_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='linked_to', to=orm['brain.Neuron'])),
            ('weight', self.gf('django.db.models.fields.FloatField')(default=0.5060005041778005)),
        ))
        db.send_create_signal(u'brain', ['Link'])


    def backwards(self, orm):
        # Deleting model 'AbstractBrainModel'
        db.delete_table(u'brain_abstractbrainmodel')

        # Deleting model 'Network'
        db.delete_table(u'brain_network')

        # Deleting model 'Layer'
        db.delete_table(u'brain_layer')

        # Deleting model 'Pool'
        db.delete_table(u'brain_pool')

        # Deleting model 'Neuron'
        db.delete_table(u'brain_neuron')

        # Deleting model 'Link'
        db.delete_table(u'brain_link')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'brain.abstractbrainmodel': {
            'Meta': {'object_name': 'AbstractBrainModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'brain.layer': {
            'Meta': {'object_name': 'Layer', '_ormbases': [u'brain.AbstractBrainModel']},
            u'abstractbrainmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['brain.AbstractBrainModel']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brain.Network']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'brain.link': {
            'Meta': {'object_name': 'Link', '_ormbases': [u'brain.AbstractBrainModel']},
            u'abstractbrainmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['brain.AbstractBrainModel']", 'unique': 'True', 'primary_key': 'True'}),
            'linked_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'linked_from'", 'to': u"orm['brain.Neuron']"}),
            'linked_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'linked_to'", 'to': u"orm['brain.Neuron']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'weight': ('django.db.models.fields.FloatField', [], {'default': '0.12564705683766442'})
        },
        u'brain.network': {
            'Meta': {'object_name': 'Network', '_ormbases': [u'brain.AbstractBrainModel']},
            u'abstractbrainmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['brain.AbstractBrainModel']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'learning_rate': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'brain.neuron': {
            'Meta': {'object_name': 'Neuron', '_ormbases': [u'brain.AbstractBrainModel']},
            u'abstractbrainmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['brain.AbstractBrainModel']", 'unique': 'True', 'primary_key': 'True'}),
            'bias': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'group_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'pool': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brain.Pool']"})
        },
        u'brain.pool': {
            'Meta': {'object_name': 'Pool', '_ormbases': [u'brain.AbstractBrainModel']},
            u'abstractbrainmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['brain.AbstractBrainModel']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'layer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brain.Layer']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['brain']