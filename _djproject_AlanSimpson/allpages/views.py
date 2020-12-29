from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'allpages/index.html')

def about_view(request):
    return render(request, 'allpages/about.html')

def privacy_view(request):
    return render(request, 'allpages/privacy.html')
