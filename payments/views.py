from django.shortcuts import render
from payments.models import Donation

def Pay(request):
	var = Donation.objects.filter()
	return render(request,'payments/payment.html',{'var':var})


def payment_completed(request):
	return render(request,'payments/payment-completed.html',{})
	

def payment_failed(request):
	return render(request,'payments/payment-failed.html',{})
	

