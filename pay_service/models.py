from django.db import models

class Client(models.Model):
	first_name = models.CharField("Имя", max_length=120)
	last_name = models.CharField("Фамилия", max_length=120)
	country = models.CharField("Страна", max_length=120)

	objects = models.Manager()

	class Meta:
		verbose_name = "Клиент"
		verbose_name_plural = "Клиенты"

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

class Payment(models.Model):
	payer = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="payments", verbose_name="Плательщик")
	amount = models.DecimalField("Сумма",max_digits=10, decimal_places=2)
	percent = models.IntegerField("Процент")
	pay_date = models.DateTimeField("Дата платежа")

	objects = models.Manager()

	class Meta:
		verbose_name = "Платеж"
		verbose_name_plural = "Платежи"
		ordering = ['pay_date']

	def __str__(self):
		return f"{self.payer} - {self.amount}"

