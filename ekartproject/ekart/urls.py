from . import views
from django.urls import path

app_name='ekart'


urlpatterns = [

    path('', views.categories, name='categorypage'),
    path('<slug:c_slug>/', views.categories, name='productsbycategory'),
    path('<slug:c_slug>/<slug:p_slug>', views.prodetails, name='productdetails'),

]
