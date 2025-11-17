from django.urls import path
from . import views

app_name = "pay_service"

urlpatterns = [
	path("", views.index, name="index"),
	path("api/payments", views.payments_api, name="payments_api"),
]