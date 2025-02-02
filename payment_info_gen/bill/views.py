from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
payments = [
    {
        'id': 1,
        'payment_method': 'PayPal',
        'amount': 100,
        'status': 'success',
        'payment_date': '2022-01-01',
        'payment_time': '10:00:00',
        'client': 'John Doe'
    },
    {
        'id': 2,
        'payment_method': 'Stripe',
        'amount': 200,
        'status': 'success',
        'payment_date': '2022-01-02',
        'payment_time': '11:00:00',
        'client': 'Jane Doe'
    },
    {
        'id': 3,
        'payment_method': 'PayPal',
        'amount': 300,
        'status': 'success',
        'payment_date': '2022-01-03',
        'payment_time': '12:00:00',
        'client': 'John Doe'
    },

]

def home(request):
    context = {
        'payments': payments
    }
    return render(request, 'bill/home.html', context)

def about(request):
    return render(request, 'bill/about.html')