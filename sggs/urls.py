"""sggs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#from django.contrib import admin
#from django.urls import path

#urlpatterns = [
 #   path('admin/', admin.site.urls),
#]
from django.contrib import admin
from django.urls import path

from student.views import view_record,view_rec2,view_stud

# from student.views import view_django


from django.conf.urls import url
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
#from . import  settings
#from django.contrib.staticfiles.urls import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 #from django.contrib import admin
#from django.urls import path

from student import forms

from student import views
from django.contrib.auth.views import LoginView


#   https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html    REPORTS GEN

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^hello1/', view_hello),
    #url(r'^hello20/', view_hello_20),
    #url(r'^record/', view_record,),
    # url(r'^django/', view_django),
    #url(r'^rec2/', view_rec2),
    path('1/', view_record, name = "template1"), 
    path('', view_rec2, name = "template2"), 
     path('3/', view_stud, name = "template3"), 
     path('2/', views.index,name='login'),
     path('accounts/', include('django.contrib.auth.urls')),
path('accounts/login/', LoginView.as_view(authentication_form=forms.OTPAuthenticationForm), name="login"),
path('accounts/login/', name='login')
path('accounts/logout/', name='logout')
path('accounts/password_change/', name='password_change')
path('accounts/password_change/done/', name='password_change_done')
path('accounts/password_reset/', name='password_reset')
path('accounts/password_reset/done/',name='password_reset_done')
path('accounts/reset/<uidb64>/<token>/', name='password_reset_confirm')
path('accounts/reset/done/', name='password_reset_complete')

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

