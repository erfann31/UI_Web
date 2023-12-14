from django.shortcuts import render


def main_view(request):
    return render(request, 'main.html')

def search_view(request):
    return render(request, 'search.html')
