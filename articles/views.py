from django.shortcuts import render
from .models import Article

def article_list(request):
     article = Article.objects.all().order_by('date')
     return render(request, 'Articles/aticle_list.html', {'articles':article})


def about(request):
     return render(request, 'Articles/about.html')
