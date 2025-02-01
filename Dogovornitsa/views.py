from django.shortcuts import render

def templates_home(request):
    return render(request, 'pages/home.html')