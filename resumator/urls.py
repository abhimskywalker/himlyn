from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from resume.models import Template, Category, Title, Bullet


from django.contrib import admin
admin.autodiscover()


admin.site.register(Template)
admin.site.register(Category)
admin.site.register(Title)
admin.site.register(Bullet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'resumator.views.home', name='home'),
    # url(r'^resumator/', include('resumator.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^resume/', include('resume.urls')),
)
