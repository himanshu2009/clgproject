"""mypro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""





from django.contrib import admin
from django.urls import path, re_path
from enroll import views
from django.urls import include



urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('myapp.urls')),


     path('admin/', admin.site.urls),
    # path('add/',views.add),
    #  path('add/addrecord/', views.addrecord, name='addrecord'),
    # path('', views.index, name='index'),
    # path('', views.add_show,name="addandshow"),
    path('delete/<int:id>/',views.delete_data,name="deletedata"),
    path('<int:id>/',views.update_data,name="updatedata"),
    # re_path(r'^departments/(?P<departmentName>[\w\s]+)/$',views.picksub,name="picksub"),
    # path('home/<my_id>',views.show_details,name="detail"),
     path('subject/<data>',views.picksub,name="picksub"),
     path('semester/<int:d>/',views.picksem,name="picksem"),
    
    path('', views.display_subjects, name='display_subjects'),
    path('app/', views.student_form, name='student_form'),
]






