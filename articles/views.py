from django.shortcuts import render

def home(request):
     return render(request, 'Articles/aticle_list.html')


def about(request):
     return render(request, 'Articles/about.html')
