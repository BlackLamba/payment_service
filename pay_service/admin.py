from django.contrib import admin
from .models import Client, Payment

@admin.register(Client)
class Client(admin.ModelAdmin):
	list_display = ("id", "last_name", "first_name", "country")
	search_fields = ("first_name", "last_name", "country")

@admin.register(Payment)
class Payment(admin.ModelAdmin):
	list_display = ("id", "payer", "amount", "percent", "pay_date")
	list_filter = ('percent', 'pay_date')
	search_fields = ('payer__first_name', 'payer__last_name')