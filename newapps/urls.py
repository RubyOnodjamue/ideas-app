
from django.urls import path

from . import views 

urlpatterns = [

    path('', views.home, name=""),

    path('register', views.register, name="register"),

    path('login', views.login, name="login"),

    path('user-logout', views.user_logout, name="user-logout"),

    # CRUD

    path('controlpanel', views.controlpanel, name="controlpanel"),

    path('add-idea', views.add_idea, name="create-record"),

    path('update-idea/<int:pk>', views.update_idea, name='update-idea'),

    path('record/<int:pk>', views.singular_record, name="record"),

    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),

    

]
