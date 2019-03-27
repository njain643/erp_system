from django.urls import path
from . import views

app_name = 'admin_app'

urlpatterns = [
    path('login/',views.loginadmin,name='login'),
    path('logout/',views.logout,name='logout'),
    path('dashboard',views.admindashboard,name='admindashboard'),
    path('upload/',views.upload),
    path('download/',views.download),
    path('textfile/',views.downloadtextfile,name='downloadtextfile'),
    path('pdffile/', views.downloadpdffile, name='downloadpdffile'),
    path('generatepdf/', views.generatepdf, name='generatepdf'),

]