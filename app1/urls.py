# app1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    # path('download-portfolio/', views.download_portfolio, name='download_portfolio'),




# urlpatterns = [
    path('', views.home, name='home'),
    # path('contact/', views.contact, name='contact'),
    # path('download-portfolio/', views.download_portfolio, name='download_portfolio'),
    path('admin-login/', views.admin_login, name='admin_login'),
    # path('cv/', views.cv_page, name='cv_page'),
    path('portfolio/download/', views.download_portfolio_pdf, name='download_portfolio'),
    path('contact/', views.contact, name='contact'),

]