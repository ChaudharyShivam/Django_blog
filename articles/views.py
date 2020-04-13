from django.shortcuts import render

def article_list(request):
     return render(request, 'Articles/aticle_list.html')


def about(request):
     return render(request, 'Articles/about.html')
