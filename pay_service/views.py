from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from .models import Payment

def index(request):
	return render(request, "pay_service/index.html")

def payments_api(request):
	payments = Payment.objects.select_related("payer").order_by("pay_date")

	scatter = [
		{
			"x": p.pay_date.isoformat(),
			"y": float(p.amount),
			"payer_name": f"{p.payer.last_name} {p.payer.first_name}"
		}
		for p in payments
	]

	grouped = (
		Payment.objects
		.values("payer__first_name", "payer__last_name")
		.annotate(total_amount=Sum("amount"))
		.order_by("payer__last_name")
	)

	labels = [f"{g["payer__last_name"]} {g["payer__first_name"]}" for g in grouped]
	values = [float(g['total_amount']) for g in grouped]

	return JsonResponse({
		"scatter": scatter,
		"bars": {"labels": labels, "values": values}
	})
