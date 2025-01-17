from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')

def making_order(request):
    return render(request, 'pages/making-order.html')

def templates(request):
    return render(request, 'pages/templates.html')