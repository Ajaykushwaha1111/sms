from django.urls import path
from . import views
urlpatterns = [
    path('',views.details, name='details'),
    path('add/',views.addCustomer, name='addCustomer'),
    path('edit/<int:id>/',views.editCustomer, name='editcus'),
    path('delete/<int:id>/',views.deleteCustomer, name='delete'),
    path('view/<slug>/<int:id>/',views.viewCustomer, name='view'),

]

