from django.conf.urls import patterns, include, url

# Use django's built-in admin.
from django.contrib import admin
admin.autodiscover()

# Import tastypie.
from tastypie.api import Api
from apps.baglady.api import BagResource, CategoryResource, ScribbleResource

# Register the resources with the API.
api_v1 = Api(api_name='v1')
api_v1.register(BagResource())
api_v1.register(CategoryResource())
api_v1.register(ScribbleResource())

# Define our url patterns/routes.
urlpatterns = patterns('',

    # Include the admin urls.
    url(r'^admin/', include(admin.site.urls)),

    # Include the Tastypie urls.
    url(r'^api/', include(api_v1.urls))

)
