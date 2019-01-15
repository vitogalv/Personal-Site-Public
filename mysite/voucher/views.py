from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Redemption, RedemptionForm
from django.urls import reverse

# Create your views here.
def voucher(request):
    return render(request, 'voucher/voucher.html', {})

def redeem(request):
    if request.method == 'POST':
        form = RedemptionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except ValueError:
                return render(request, 'voucher/redeem.html', {'error_message':"All fields must be filled in"})
            return HttpResponseRedirect(reverse('success'))
    else:
        form = RedemptionForm()
    return render(request, 'voucher/redeem.html', {'form':form})

def success(request):
    return render(request, 'voucher/success.html', {})
