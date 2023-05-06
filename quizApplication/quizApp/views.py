from django.shortcuts import render

# viewsler
# anasayfa viewsi

def index(request):
    return render(request, 'index.html')