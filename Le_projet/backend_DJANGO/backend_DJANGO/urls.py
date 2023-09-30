from django.contrib import admin
from django.urls import path
from backoffice.views import my_view, pokepage, signout
from backoffice.views import login
from backoffice.views import home
from backoffice.views import liste_contrats
urlpatterns = [
    path('admin/', admin.site.urls),

    path('signout', signout, name='signout'),


    path('', login, name='login'),
    path('home/', home, name='home'),

    path('liste_contrats/', liste_contrats, name='liste_contrats'),
    path('pokepage/', pokepage, name='pokepage'),
    
    path('myview/', my_view, name='my_view'),
]
