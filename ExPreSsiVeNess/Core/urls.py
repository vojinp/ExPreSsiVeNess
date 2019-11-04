from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'visualize/(?P<visualizer>\w+)', views.showVisualizer)
]