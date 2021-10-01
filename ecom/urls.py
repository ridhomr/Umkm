from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from dashboard import views
from .views import  loginView, dashboard, logoutView, tentangjualin, informasikontak
from catalog import views


urlpatterns = [
    path('dashboard/', include('dashboard.urls')),
    path('login-admin/', loginView,  name="login"),
    path('logout/', logoutView,  name="logout"),
    path('dashboard/', dashboard,  name="dashboard"),

    
    #path('customerlogin', LoginView.as_view(template_name='dashboard/customerlogin.html'),name='customerlogin'),
    #path('customer-home', customer_home_view, name='customer-home'),
    #path('afterlogin', afterlogin_view, name='afterlogin'),
    path('my-profile/', views.my_profile_view, name='my-profile'),
    path('edit-profile/', views.edit_profile_view, name='edit-profile'),


    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('catalog.urls')),

    path('tentang/',  tentangjualin, name="tentangjualin"),
    path('kontak/',  informasikontak, name="informasikontak"),

    path('dashboard/notifikasi/', views.view_feedback_view,name='view-feedback'),
    path('dashboard/contact/', views.view_contact_view,name='view-contact'),
    
    path('send-feedback/', views.send_feedback_view,name='send-feedback'),
    path('send-contact/', views.contactus_view,name='send-contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
