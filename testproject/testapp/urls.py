from django.urls import path
from . import views

urlpatterns = [
    path("", views.testapp, name='tenant_app'),
    path('<int:tenant_id>/', views.tenant_details, name='tenant_details'),
]
