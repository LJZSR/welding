from django.conf.urls import url
from receive import views

urlpatterns = [
    url(r'^sound/$', views.sound, name='sound'),
    url(r'^current/$', views.current, name='current'),
    url(r'^voltage/$', views.voltage, name='voltage'),
    url(r'^CCD_Input/$', views.CCD_Input, name='CCD_Input'),
    url(r'^DAQ_Input/$', views.DAQ_Input, name='DAQ_Input'),
    url(r'^Robot_Input/$', views.Robot_Input, name='Robot_Input'),
    url(r'^image_refresh/$', views.image_refresh, name='image_refresh'),
    url(r'^current_refresh/$', views.current_refresh, name='current_refresh'),
    url(r'^sound_refresh/$', views.sound_refresh, name='sound_refresh'),
    url(r'^voltage_refresh/$', views.voltage_refresh, name='voltage_refresh'),
    url(r'^robot_refresh/$', views.robot_refresh, name='robot_refresh'),
    url(r'^show/$', views.show, name='show'),
    url(r'^output/$', views.output, name='output')
    ]
