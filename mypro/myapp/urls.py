

from django.urls import path
from myapp import views


urlpatterns = [
    path('home/',views.home),
    path('homei/',views.savedata,name="savedata"),
    path('homeii/',views.savedata2,name="savedata2"),
    path('cse/',views.cse,name='cse'),
    path('chemical/',views.chemical,name='chemical'),
    path('mech/',views.mech,name='mech'),
    path('entc/',views.entc,name='entc'),
    path('it/',views.it,name='it'),
    path('textile/',views.textile,name='textile'),
    path('production/',views.production,name='production'),
    path('instru/',views.instru,name='instru'),
    path('civil/',views.civil,name='civil'),
    path('electrical/',views.electrical,name='electrical')
    
]


